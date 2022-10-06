FROM python:3.6

COPY ./GrupoDAS

WORKDIR GrupoDAS

CMD ["ptthon3", "hello.py"]
