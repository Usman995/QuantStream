FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY market_data_ingestion.py .

CMD ["python", "market_data_ingestion.py"]