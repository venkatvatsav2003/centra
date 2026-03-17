# Use a lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install security updates (OS level scanning/patching)
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for security
RUN useradd -m appuser
USER appuser

# Copy application code
COPY src/ ./src/

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "src/app.py"]
