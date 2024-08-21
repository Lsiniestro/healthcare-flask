import numpy as np
import flask
import pickle
import requests
from flask import Flask, render_template, request





app = Flask(__name__)

model=pickle.load(open('../models/model_xgb.pkl','rb'))

dictionary = {"0":'No Heart Disease', "1":'Heart Disease'}


@app.route('/',methods=['GET','POST'])

def index():
    if request.method == 'POST':
        age = float(request.form['age'])
        ejection_fraction = float(request.form['ejection_fraction'])
        serum_creatinine = float(request.form['serum_creatinine'])
        serum_sodium = float(request.form['serum_sodium'])

        data=[[age,ejection_fraction,serum_creatinine,serum_sodium]]
        prediction = str(model.predict(data)[0])
        pred_dict=dictionary[prediction]
    else:
        pred_dict=None
    

    return render_template('index.html',prediction=pred_dict)