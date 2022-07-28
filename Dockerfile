FROM python:3.10.5-slim-buster

COPY ./requirements.txt /project/requirements.txt

WORKDIR /project

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /project

ENV FLASK_APP=app.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD [ "python", "app.py"]
