FROM python:3.7.2

WORKDIR /usr/src/app/

<<<<<<< HEAD
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
=======
COPY scripts/install_dependencies.sh /usr/src/app/scripts/install_dependencies.sh
COPY requirements.txt /usr/src/app/
RUN scripts/install_dependencies.sh

COPY . /usr/src/app/
>>>>>>> working
