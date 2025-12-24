FROM python:3.11-slim

# Set working dir
WORKDIR /usr/src/app

# Install pip dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and data
COPY app ./app

# Expose port (optional, for documentation)
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]