FROM python:3.10.0-slim


RUN mkdir /app
WORKDIR /app
ADD . /app

RUN useradd -ms /bin/bash appuser

ENV PPYTHONDONTWRITEBYTECODE=1
ENV PYTHON BUFFERED

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

USER appuser

CMD ["python", "./main.py"]