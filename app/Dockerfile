FROM python:3.11-slim

RUN groupadd new_group
RUN useradd --gid new_group --shell /bin/bash --create-home new_user

USER new_user

WORKDIR ~/app
COPY . .

RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt --user

EXPOSE 5000

CMD ["python", "main.py"]