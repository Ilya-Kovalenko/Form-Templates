FROM python:3.11-slim-buster
WORKDIR /code
COPY . /code/
RUN pip install --no-cache-dir -r /code/requirements.txt
EXPOSE 8000
CMD ["python3", "server.py"]