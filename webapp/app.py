#!/usr/bin/python3
import json as j
import matplotlib.pyplot as plot
import numpy as np
from flask import Flask, Response, json, redirect, render_template, request, url_for
import centremass as c
import nnet as nn
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def predict():
  if(request.method == 'GET'):
    return url_for('.index.html')
  r = request.json
  
  va = dict(r).values()
  r  = np.array(list(va)).reshape(250,250,4)
  arr = r[:,:,3:4]
  arr = np.asarray(arr.astype(np.uint8))
  gray = cv2.cvtColor(arr, 0, 0)
  arr = cv2.resize(gray, dsize=(28,28),dst=arr,interpolation=cv2.INTER_CUBIC )
  arr= arr[:,:,0:1]

  # centered =  c.center_of_mass(request.json)
  num =  nn.get_prediction(arr)
  print(num)  
  answer= str(num)

  return render_template('predict.html' , answer=num, id=45, color="red")