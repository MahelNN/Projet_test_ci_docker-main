FROM ubuntu:latest

RUN apt-get update

RUN apt-get install apt-utils -y

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

WORKDIR  /home/user/Projet_test_ci_docker_main

COPY . .

RUN echo "Branch II"

RUN hostname

RUN pwd; who

CMD ["python3", "main.py"]
