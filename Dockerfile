# image
FROM python:3-onbuild

WORKDIR /usr/src/mnistnn/

COPY requirements.txt ./
COPY . ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]

