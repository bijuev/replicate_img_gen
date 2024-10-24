## Image Generation and Conversion API
This FastAPI application provides an API to generate images using the Replicate API, based on the text promt Replicate API generate the image, that can be saved to image files.

## Features
Generate images based on a prompt using the Stable Diffusion model from Replicate.
Save image files directly from URLs provided by Replicate's API.

## Requirements
Python 3.8+
FastAPI
Replicate API (with a valid API token)

## Setup
Clone the repository and navigate to your project directory:

cd <project-directory>
Install Dependencies

Create and activate a virtual environment, then install the required packages:

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
Or for Windows
venv\Scripts\activate
pip install -r requirements.txt

## Required packages:

fastapi,
uvicorn,
pydantic,
pydantic-settings,
python-dotenv,
replicate,

## Configure Environment Variables
Create a .env file in the root directory and add your Replicate API token:

REPLICATE_API_TOKEN="your-replicate-api-token"

## Run the Application
Start the FastAPI application using Uvicorn:

uvicorn app.routes:app --reload
The app will be running at http://127.0.0.1:8000.

## API Endpoints
1. Generate Image
Endpoint: /generate-image/
Method: POST
Request Body:
prompt: A string describing the image you want to generate (e.g., "a sunset over the mountains").
Response:
image_url: The URL to the generated image.
Example Request:

POST /generate-and-save-image/
{
  "prompt": "an astronaut riding a horse on mars"
}
Example Response:
{
    "image_path": "images/generated_image.png"
}

## How to Test Using Postman
Set the request type to POST.
Use http://127.0.0.1:8000/generate-and-save-image/ as the URL.
In the body, select raw, then JSON, and provide a prompt:

{
  "prompt": "a sunset over the mountains"
}

## License
This project is licensed under the MIT License.