from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import logging
from test import process_image  # Assuming process_image is the function in test.py that handles OCR

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        detected_text = "connect"
        return JSONResponse(content={"detected_text": detected_text})
        # Ensure the temp directory exists
        temp_dir = "../temp"
        os.makedirs(temp_dir, exist_ok=True)

        # Save the uploaded file
        file_location = os.path.join(temp_dir, file.filename)
        logger.info(file_location)
        with open(file_location, "wb") as f:
            f.write(await file.read())

        # Process the image using the existing OCR functionality
        detected_text = process_image(file_location)

        # Clean up the saved file
        os.remove(file_location)

        logger.info(f"Detected text: {detected_text}")
        print(detected_text)

        return JSONResponse(content={"detected_text": detected_text})

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=500)