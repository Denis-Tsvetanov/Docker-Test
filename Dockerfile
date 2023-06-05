FROM python:3.9-slim

WORKDIR /app

COPY main.py .
COPY irislogreg.pkl .

RUN pip install fastapi uvicorn joblib numpy pydantic

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
