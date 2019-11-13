# image
FROM python:3-onbuild


WORKDIR /usr/src/mnistnn/



COPY requirements.txt ./
COPY . ./


RUN pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "/usr/src/mnistnn/app.py"]

