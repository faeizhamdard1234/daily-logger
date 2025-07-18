FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir click
ENTRYPOINT ["python", "app.py"]
