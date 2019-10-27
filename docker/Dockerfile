FROM python:3.8-alpine

COPY ./ /app

WORKDIR /app

RUN pip3 install -e .

ENV SHELL=/bin/bash

RUN create_alias test ls

CMD ["test", "exit 0"]