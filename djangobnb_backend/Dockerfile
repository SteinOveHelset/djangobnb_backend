FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/djangobnb_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/djangobnb_backend/entrypoint.sh
RUN chmod +x /usr/src/djangobnb_backend/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/djangobnb_backend/entrypoint.sh" ]