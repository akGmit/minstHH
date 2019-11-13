import cv2
import matplotlib.pyplot as plot
import numpy as np
from flask import Flask, json, render_template, request
import recognition.nnet as nn
from wsgiref import simple_server

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print(request.headers)
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
  print(request.headers)
  r = request.json
  r  = np.array(r).reshape(250,250).astype(np.uint8)
  r = cv2.resize(r, dsize=(28,28),dst=r,interpolation=cv2.INTER_CUBIC )
  num =  nn.get_prediction(r)
  print(num)  
  answer= str(num)
  
  return answer

if __name__ == "__main__":
  server = simple_server.WSGIServer(('', 8000), simple_server.WSGIRequestHandler)
  server.set_app(app)
  server.serve_forever()
