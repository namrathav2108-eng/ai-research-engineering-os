from fastapi import FastAPI

app = FastAPI(
    title="AI Research & Engineering OS",
    description="AI-powered research and engineering workspace.",
    version="0.1.0",
)


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
