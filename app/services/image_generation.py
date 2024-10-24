import os
import base64
import logging
import replicate
from app.config import settings


class ImageGenerationService:
    @staticmethod
    async def generate_image(prompt: str) -> str:
        """
        Generate an image using the Replicate API and return the image URL or base64 data.
        """
        input_data = {
            "width": 768,
            "height": 768,
            "prompt": prompt,
            "scheduler": "K_EULER",
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "num_inference_steps": 50
        }

        client = replicate.Client(api_token=settings.replicate_api_token)

        try:
            output = client.run(
                "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
                input=input_data
            )

            # Log the output received from the Replicate API
            logging.info(f"Output from Replicate: {output}")

            # Check if output contains FileOutput or base64 string
            if isinstance(output, list) and len(output) > 0:
                # If FileOutput object, extract the base64 string or URL
                if isinstance(output[0], replicate.helpers.FileOutput):
                    # Access URL (or base64 if available in FileOutput)
                    return output[0].url
                else:
                    # If base64 string, return it directly
                    return output[0]
            else:
                raise RuntimeError("Unexpected output format from image generation.")

        except Exception as e:
            logging.error(f"Error during image generation: {e}")
            raise RuntimeError(f"Error during image generation: {e}")


    @staticmethod
    async def convert_base64_to_image(base64_str: str, output_file_name: str) -> str:
        """
        Convert the base64 string to an image file and return the file path.
        """
        # Decode the base64 string
        try:
            if base64_str.startswith("data:image/png;base64,"):
                base64_str = base64_str.split(",")[1]  # Extract the base64 part
            image_data = base64.b64decode(base64_str)

            # Specify the output directory and filename
            output_dir = "images"  # Ensure this directory exists or create it
            os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
            image_path = os.path.join(output_dir, output_file_name)

            # Write the image data to a file
            with open(image_path, "wb") as image_file:
                image_file.write(image_data)

            logging.info(f"Image saved to {image_path}")
            return image_path  # Return the path to the saved image
        except Exception as e:
            logging.error(f"Failed to save image: {e}")
            raise RuntimeError("Failed to save image.")
        
