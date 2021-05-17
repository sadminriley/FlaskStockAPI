FROM python:3-alpine

MAINTAINER sadminriley

ADD app.py /

ADD requirements.txt /
ADD .key /

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
