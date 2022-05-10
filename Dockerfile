FROM python:3.9.12
RUN cd /etc/apt/ && mv sources.list sources.list.bak && \
    echo "deb http://mirrors.aliyun.com/debian/ bullseye main non-free contrib" >> sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ bullseye main non-free contrib" >> sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security/ bullseye-security main" >> sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian-security/ bullseye-security main" >> sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib" >> sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib" >> sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib" >> sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib" >> sources.list

RUN apt update && apt install -y ffmpeg=7:4.3.4-0+deb11u1
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
