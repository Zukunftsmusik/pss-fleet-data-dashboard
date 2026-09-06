## This file was created by the Google Search AI
# === STAGE 1: Build the Vue Frontend ===
FROM node:22-alpine AS frontend-builder
WORKDIR /build

# Leverage Docker cache for JavaScript dependencies
COPY frontend/package*.json ./
RUN npm install --legacy-peer-deps

# Copy Vue source files and build the production bundle
COPY frontend/ ./
RUN npm run build

# === STAGE 2: Run the Unified FastAPI Application ===
FROM python:3.14-slim
WORKDIR /app

# Optimize Python execution environment inside the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install runtime Python dependencies from exported requirements.txt
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy backend python packages (app and test targets are isolated)
COPY backend/app/ ./app/

# Pull the statically compiled Vue dashboard directly into the runtime context
COPY --from=frontend-builder /build/dist ./frontend/dist

# Expose internal app architecture port (Standard CapRover integration proxy)
EXPOSE 8000

# Execute modern FastAPI production server configuration
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
