import logging
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from app.services.image_generation import ImageGenerationService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a request model
class ImageGenerationRequest(BaseModel):
    prompt: str


# Define a response model
class ImageResponse(BaseModel):
    image_path: str

router = APIRouter()


@router.post("/generate-and-save-image/", response_model=ImageResponse)
async def generate_and_save_image(request: ImageGenerationRequest):
    """
    This endpoint generates an image from the prompt, converts it from base64, 
    and saves it directly to the 'images' folder in one step.
    """
    logger.info("Received request to generate and save image with prompt: %s", request.prompt)
    try:
        # Step 1: Generate the image in base64 format
        base64_image = await ImageGenerationService.generate_image(request.prompt)

        # Step 2: Convert the base64 string to an image and save it
        output_image_path = "generated_image.png"  # Or customize the name based on the prompt
        image_path = await ImageGenerationService.convert_base64_to_image(base64_image, output_image_path)

        logger.info(f"Image successfully saved at: {image_path}")
        return ImageResponse(image_path=image_path)

    except Exception as e:
        logger.error(f"Error during the image generation or conversion process: {e}")
        raise HTTPException(status_code=400, detail=str(e))


# Initialize FastAPI and include the router
app = FastAPI()
app.include_router(router)

