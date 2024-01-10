FROM python:3.11

WORKDIR /code

RUN pip install -U pipenv
COPY Pipfile* /code/
RUN pipenv install --system --ignore-pipfile --deploy

COPY . /code/

CMD [ "python", "main.py" ]
