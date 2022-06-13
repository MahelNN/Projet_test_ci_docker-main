FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

# RUN pip install -r requirement.txt

WORKDIR  /home/user/Projet_test_ci_docker_main

COPY . .

CMD ["python3", "main.py"]