# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the Docker container
WORKDIR /app

# Install the required Python libraries
RUN pip install --no-cache-dir streamlit requests

# Copy the local code to the container's working directory
COPY . /app

# Expose port 8501 on which Streamlit runs by default
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
