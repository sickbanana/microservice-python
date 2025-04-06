FROM python:3.11.7-alpine

WORKDIR /src

COPY ./ /src/app

RUN pip3 install -r app/requirements.txt

EXPOSE 8000

CMD ["python", "-m", "app.main"]