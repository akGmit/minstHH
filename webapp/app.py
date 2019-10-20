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
 
  r = request.json
  r  = np.array(r).reshape(250,250).astype(np.uint8)
  r = cv2.resize(r, dsize=(28,28),dst=r,interpolation=cv2.INTER_CUBIC )
  # plot.imsave('test.png', ~r, cmap='gray')
  num =  nn.get_prediction(r)
  print(num)  
  answer= str(num)
  
  return answer