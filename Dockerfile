FROM tensorflow/tensorflow:2.7.0

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN apt-get update
RUN yes | apt install libpq-dev -y
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

# RUN ls -la
# RUN pwd


CMD ["python", "flask_app/app.py"]