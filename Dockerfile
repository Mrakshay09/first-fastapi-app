FROM python:3.11-slim

WORKDIR /blog

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY blog blog

EXPOSE 8000

CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "8000"]
