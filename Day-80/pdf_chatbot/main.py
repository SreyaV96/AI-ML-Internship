
from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from pypdf import PdfReader
from io import BytesIO
from pathlib import Path
import chromadb
import uuid
import logging
import time


#Initialize FastAPI
app = FastAPI(title="RAG Chatbot")


#Initialize ChromaDB

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="pdf_documents"
)


#Configure HTML templates

templates = Jinja2Templates(directory="templates")


# 4. Configure logging

Path("logs").mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename="logs/chatbot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)


# Split text into chunks

def split_text(text, chunk_size=1000, overlap=150):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# Define request and response models
class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = Field(default_factory=list)



# Home page

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# Upload PDF endpoint


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    start_time = time.perf_counter()
    filename = file.filename or "unknown"

    try:
        # Validate the filename
        if not file.filename or not filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Please upload a PDF file."
            )

        # Read uploaded PDF
        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file is empty."
            )

        # Read PDF from memory
        reader = PdfReader(BytesIO(contents))

        # Extract text from all pages
        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

        # Check extracted text
        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No extractable text found in this PDF."
            )

        # Split text into chunks
        chunks = split_text(text)

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="No usable text chunks were generated."
            )

        # Generate unique IDs
        ids = [
            str(uuid.uuid4())
            for _ in chunks
        ]

        # Create metadata for each chunk
        metadatas = [
            {
                "source": filename,
                "chunk": index
            }
            for index in range(len(chunks))
        ]

        # Store chunks in ChromaDB
        collection.add(
            ids=ids,
            documents=chunks,
            metadatas=metadatas
        )

        # Log successful upload
        logger.info(
            "Upload=%r | Duration=%.3fs | Status=SUCCESS | "
            "Pages=%d | Chunks=%d",
            filename,
            time.perf_counter() - start_time,
            len(reader.pages),
            len(chunks)
        )

        return {
            "message": "PDF uploaded successfully",
            "filename": filename,
            "pages": len(reader.pages),
            "chunks_stored": len(chunks)
        }

    except HTTPException as exc:
        logger.warning(
            "Upload=%r | Duration=%.3fs | Status=FAILURE | "
            "HTTP=%d | Error=%s",
            filename,
            time.perf_counter() - start_time,
            exc.status_code,
            exc.detail
        )
        raise

    except Exception:
        logger.exception(
            "Upload=%r | Duration=%.3fs | Status=FAILURE",
            filename,
            time.perf_counter() - start_time
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to process the PDF."
        )

    finally:
        await file.close()



#  Ask question endpoint
@app.post("/ask", response_model=ChatResponse)
def ask_question(data: QuestionRequest):

    question = data.question.strip()
    start_time = time.perf_counter()

    try:
        # Validate question
        if not question:
            raise HTTPException(
                status_code=400,
                detail="Please enter a question."
            )

        # Check whether documents exist
        total_chunks = collection.count()

        if total_chunks == 0:
            raise HTTPException(
                status_code=400,
                detail="Please upload a PDF first."
            )

        # Retrieve relevant chunks
        results = collection.query(
            query_texts=[question],
            n_results=min(3, total_chunks),
            include=["documents", "metadatas"]
        )

        documents = (results.get("documents") or [[]])[0]
        metadatas = (results.get("metadatas") or [[]])[0]

        # Check retrieval results
        if not documents:
            raise HTTPException(
                status_code=404,
                detail="No relevant text found."
            )

        # Combine retrieved text
        answer = "\n\n".join(documents)

        # Extract unique source filenames
        sources = sorted({
            metadata["source"]
            for metadata in metadatas
            if metadata and metadata.get("source")
        })

        # Log successful question
        logger.info(
            "Question=%r | Duration=%.3fs | Status=SUCCESS | "
            "Sources=%s",
            question,
            time.perf_counter() - start_time,
            sources
        )

        return ChatResponse(
            answer=answer,
            sources=sources
        )

    except HTTPException as exc:
        logger.warning(
            "Question=%r | Duration=%.3fs | Status=FAILURE | "
            "HTTP=%d | Error=%s",
            question,
            time.perf_counter() - start_time,
            exc.status_code,
            exc.detail
        )
        raise

    except Exception:
        logger.exception(
            "Question=%r | Duration=%.3fs | Status=FAILURE",
            question,
            time.perf_counter() - start_time
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to process the question."
        )
