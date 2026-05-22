FROM python:3.12-alpine

WORKDIR /app

COPY requiremens.txt /app/

RUN python -m pip install --upgrade pip

RUN pip install -r requiremens.txt

COPY . /app/

CMD [ "python" , "bot,py" , "app.py" ]