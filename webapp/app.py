from flask import Flask, render_template, redirect, Response
from flask import request
from flask import json
import json as j
import centremass as c

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def jsonData():
    centered =  c.center_of_mass(request.json)
    
    print(centered)
    return "DSFSD"