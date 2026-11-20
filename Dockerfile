# Builds the API and demo page as one container, for example for Google Cloud Run.
# NOT FOR CLINICAL USE. A demonstration and proof of concept only.
FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Cloud Run says which port to listen on in $PORT (8080 if not set).
ENV PORT=8080
CMD ["sh", "-c", "exec uvicorn api.server:app --host 0.0.0.0 --port ${PORT:-8080}"]
