FROM python:3.6.5-slim

# install netcat
RUN apt-get update \
  && apt-get -y install netcat \
  && apt-get clean

RUN apt-get -y install git && \
    apt-get -y install dos2unix && \
    apt-get -y install libgomp1

# set working directory
RUN mkdir -p /usr/src/app && \
    mkdir -p /usr/src/app/data

WORKDIR /usr/src/app

# add entrypoint.sh
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN dos2unix /usr/src/app/entrypoint.sh

RUN pip install  --upgrade pip

# add requirements
COPY requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY project /usr/src/app/project
COPY data/*xlsx /usr/src/app/data/
COPY ./.git /usr/src/app/.git
COPY *.py /usr/src/app/


ENV PYTHONPATH=/usr/src/app/project
EXPOSE 5000
# run server
CMD ["/usr/src/app/entrypoint.sh"]
