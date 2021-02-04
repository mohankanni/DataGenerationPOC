FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# ENV PORT 8081

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
