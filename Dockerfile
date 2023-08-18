FROM python:3.9.12
RUN apt update && apt install -y ffmpeg
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
