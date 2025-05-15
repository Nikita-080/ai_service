FROM python:3.11-slim
WORKDIR /src
COPY requirements.txt /src
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /src
RUN apt update && apt install -y curl
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama serve &
RUN sleep 5
RUN ollama pull qwen2.5:0.5b
RUN ollama run qwen2.5:0.5b
EXPOSE 5000
