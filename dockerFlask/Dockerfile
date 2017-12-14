FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev nano

COPY ./requirements.txt /app/requirements.txt
ADD ./templates /app
ADD ./static /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


