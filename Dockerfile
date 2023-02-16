FROM python:3.11.2-bullseye as builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.11.2-bullseye 

RUN apt-get update

RUN apt-get install -y tesseract-ocr 

RUN apt-get install -y openjdk-11-jre

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local:$PATH

WORKDIR /reverse-scanner

COPY scan.sh . 

RUN chmod +x scan.sh

COPY ./scripts ./scripts

#this keeps the container from exiting right after starting. 
CMD [ "/bin/bash", "-c", "while true; do sleep 3600; done" ] 