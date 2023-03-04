FROM python:3.10.10-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI server
EXPOSE 8000

# Run the unit tests with pytest
#RUN pytest

# Run the application with the development server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--workers", "2"]