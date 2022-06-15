FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN echo "Main branch"

WORKDIR  /home/Projet_test_ci_docker_main

COPY . .

RUN ls -la > temp

RUN more < temp

CMD ["python3", "main.py"]
