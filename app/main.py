from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Replicate Image Generation API",
    description="API to fine-tune models and generate images using Replicate",
    version="1.0.0",
)

# Include API routes
app.include_router(router)

