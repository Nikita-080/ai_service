FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]