import cv2
import matplotlib.pyplot as plot
import numpy as np
from flask import Flask, json, render_template, request
import recognition.nnet as nn
from wsgiref import simple_server
import centremass as center
from PIL import Image, ImageOps

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print(request.headers)
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
  print(request.headers)
  r = request.json
  r  = np.array(r).reshape(200,200).astype(np.uint8)
  
  size = lambda x,y : (int((x / y) * 20), 20) if (x <= y) else (20,int(( y / x) * 20))
  
  img = Image.fromarray(r)
  img = img.crop(img.getbbox())
  
  (x, y) = int(img.size[0]), int(img.size[1])
  r  = cv2.resize(np.array(img),dsize=size(x,y) ,dst=r,interpolation=cv2.INTER_AREA   )
  
  pos = 13 - int(r.shape[1]/2), 13 - int(r.shape[0]/2)
  
  img = Image.new(mode='L', size=(28,28), color=0)
  img.paste(Image.fromarray(r), box=pos)
  
  num =  nn.get_prediction(img)
  print(num)  
  answer= str(num)
  
  return answer

# Adopted from  https://stackoverflow.com/questions/31400769/bounding-box-of-numpy-array
# def bbox2(img):
#     rows = np.any(img, axis=1)
#     cols = np.any(img, axis=0)
#     rmin, rmax = np.where(rows)[0][[0, -1]]
#     cmin, cmax = np.where(cols)[0][[0, -1]]
#     i = np.array(img[rmin:rmax,cmin:cmax])
#     return i

# def get_bounding_box(x):
#     """ Calculates the bounding box of a ndarray"""
#     mask = x == 0
#     bbox = []
#     all_axis = np.arange(x.ndim)
#     for kdim in all_axis:
#         nk_dim = np.delete(all_axis, kdim)
#         mask_i = mask.all(axis=tuple(nk_dim))
#         dmask_i = np.diff(mask_i)
#         idx_i = np.nonzero(dmask_i)[0]
#         if len(idx_i) != 2:
#             raise ValueError('Algorithm failed, {} does not have 2 elements!'.format(idx_i))
#         bbox.append(slice(idx_i[0]+1, idx_i[1]+1))
#     img = (x[bbox]>0)
#     return img

if __name__ == "__main__":
  server = simple_server.WSGIServer(('127.0.0.1', 8000), simple_server.WSGIRequestHandler)
  server.set_app(app)
  print("Listening on:  http://" +  server.server_address[0] + ':' +  str(server.server_address[1]))
  server.serve_forever()
