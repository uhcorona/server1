FROM python:2

COPY *.py ./

RUN pip install flask
RUN pip install requests

EXPOSE 4000

CMD ["python", "app.py"]
