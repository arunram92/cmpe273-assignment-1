FROM python:2.7.13
MAINTAINER Your Name "y.arunram@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
CMD ["https://github.com/arunram92/cmpe273-assignment-1"]
