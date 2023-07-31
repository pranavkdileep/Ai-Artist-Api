# Use a Python base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the main.py file into the container
COPY main.py .

# Install required dependencies
RUN pip install gradio fastapi uvicorn
RUN mkdir image
# Expose the required port
EXPOSE 7860

# Start the FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
