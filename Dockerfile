FROM ubuntu:latest
MAINTAINER Sergey Korolev "ovst91@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install flask
ENV FLASK_APP=count-posts
#ENTRYPOINT ["python"]
#CMD ["count-posts.py"]
