import cv2
import matplotlib.pyplot as plot
import numpy as np
from flask import Flask, json, render_template, request
import recognition.nnet as nn
from wsgiref import simple_server
import centremass as center
from PIL import Image, ImageOps

app = Flask(__name__)
model = nn.get_model()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
  r = request.json

  img = process_image(r)
  
  answer = model.predict_classes(img)[0]
  
  return str(answer)

def process_image(img):
  r  = np.array(img).reshape(200,200).astype(np.uint8)
  
  size = lambda x,y : (int((x / y) * 20), 20) if (x <= y) else (20,int(( y / x) * 20))
  
  img = Image.fromarray(r)
  img = img.crop(img.getbbox())
  
  (x, y) = int(img.size[0]), int(img.size[1])
  r  = cv2.resize(np.array(img),dsize=size(x,y) ,dst=r,interpolation=cv2.INTER_AREA   )
  
  pos = 13 - int(r.shape[1]/2), 13 - int(r.shape[0]/2)
  
  img = Image.new(mode='L', size=(28,28), color=0)
  img.paste(Image.fromarray(r), box=pos)
  
  return  ~np.asarray(img).reshape((1,28,28,1)).astype(np.uint8) / 255.0

if __name__ == "__main__":
  server = simple_server.WSGIServer(('127.0.0.1', 8000), simple_server.WSGIRequestHandler)
  server.set_app(app)
  
  print("Listening on:  http://" +  server.server_address[0] + ':' +  str(server.server_address[1]))
  
  server.serve_forever()
