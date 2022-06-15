FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN echo "Branch I"

WORKDIR  /home/user/Projet_test_ci_docker_main

COPY . .

RUN ls -la > temp1

RUN more < temp1

CMD ["python3", "main.py"]
