# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for PaddleOCR and OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    libgl1-mesa-glx \  # Add the OpenGL library
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install pip and dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
