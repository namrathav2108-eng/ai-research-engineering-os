from pathlib import Path

import fitz
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Research & Engineering OS",
    description="AI-powered research and engineering workspace.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ai-research-engineering-os",
        "version": "0.1.0",
    }


@app.get("/")
async def root():
    return {
        "message": "AI Research & Engineering OS API",
        "docs": "/docs",
    }


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    safe_filename = Path(file.filename or "document.pdf").name
    file_path = UPLOAD_DIR / safe_filename

    contents = await file.read()
    file_path.write_bytes(contents)

    return {
        "message": "PDF uploaded successfully.",
        "filename": safe_filename,
        "size_bytes": len(contents),
    }


@app.post("/documents/extract")
async def extract_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    contents = await file.read()

    try:
        document = fitz.open(stream=contents, filetype="pdf")

        pages = []
        full_text = []

        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()

            pages.append(
                {
                    "page": page_number,
                    "text": text,
                }
            )

            if text:
                full_text.append(text)

        page_count = len(document)
        document.close()

        return {
            "filename": file.filename,
            "page_count": page_count,
            "text": "\n\n".join(full_text),
            "pages": pages,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Could not extract PDF text: {exc}",
        ) from exc
