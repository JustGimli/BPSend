FROM python:3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# ENV PRIMARY_CON True
ARG DockerHome="/app"


RUN mkdir -p $DockerHome

RUN pip install --upgrade pip

COPY req.txt req.txt

COPY . ${PATH}
WORKDIR ${PATH}


ENV TOKEN 5337418205:AAF64PcryZpAC61AY0eKNwpBCZD2LVTXA1c
ENV MESSAGE HELLO
ENV USER_ID 1239134441

RUN pip install -r req.txt

CMD [ "python3", "main.py" ]
