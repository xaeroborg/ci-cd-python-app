# Dockerfile
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy application files into the container
COPY . /app

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

# Default command to run your application
CMD ["python", "app.py"]
