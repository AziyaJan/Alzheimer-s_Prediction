# ==========================
# Alzheimer’s Prediction – Dockerfile
# ==========================

# Use Python 3.13 base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for pandas, numpy, scikit-learn, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy project files
COPY . .

# Expose port (Render will map automatically)
EXPOSE 5000

# Gunicorn entrypoint for Flask app
# -b : bind address
# -w : number of workers (adjust based on resources)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "-w", "4"]
