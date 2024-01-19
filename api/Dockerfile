FROM python:3.12.1-slim

WORKDIR /api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]