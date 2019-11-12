FROM python:3
ADD bot.py /

COPY bot.py /
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

CMD ["python3", "./bot.py"]

