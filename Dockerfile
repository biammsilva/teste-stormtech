FROM python:3
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver"]
