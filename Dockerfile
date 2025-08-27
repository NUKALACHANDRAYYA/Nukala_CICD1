# Use official Python image as base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create a mount point for GCS
# RUN mkdir -p /mnt/gcs

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
