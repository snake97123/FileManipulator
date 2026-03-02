FROM python:3.13-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install uv

CMD ["bash"]

