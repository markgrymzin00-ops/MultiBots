FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends git jq && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

CMD ["sh", "-c", "python main.py"]
