FROM python:3.9.12
RUN apt update && apt install -y ffmpeg=7:4.3.4-0+deb11u1
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
