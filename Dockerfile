FROM python:3.12-slim

# set working directory
WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libdrm2 \
    libxcb1 \
    libxkbcommon0 \
    libasound2 \
    libexpat1 \
    libdbus-1-3 \
    && rm -rf /var/lib/apt/lists/*


# copy requirements file
COPY requirements.txt .

COPY tests /app/tests

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium
RUN playwright install-deps

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONPATH=/app

# Default command to run tests
CMD ["pytest", "tests/test_signin.py", "-v", "-s"]