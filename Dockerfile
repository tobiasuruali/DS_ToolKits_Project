FROM tensorflow/tensorflow

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

# RUN ls -la
# RUN pwd
CMD ["python", "/app/code/main.py"]