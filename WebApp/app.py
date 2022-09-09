from flask import Flask,render_template,redirect,request
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import sklearn
import pickle


app = Flask(__name__)
model = pickle.load(open(r"C:\\Users\\pulki\\Downloads\\Loanfate-master\\Loanfate-master\\WebApp\\model.pkl", "rb"))


@app.route('/')
@cross_origin()
def home():
    return render_template('base.html')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method=="POST":
        Gender = request.form["gender"]
        Married = request.form["married"]
        Education = request.form["education"]
        LoanAmount = request.form["loanamount"]
        Credit_History = request.form["credithistory"]
        Property_Area = request.form["proparea"]
        Total_Income = request.form["totalincome"]
        pred = model.predict([[float(Gender) , float(Married), float(Education), float(LoanAmount), float(Credit_History), float(Property_Area), float(Total_Income)]])
        if pred ==0:
            result = "Your housing loan application is likely to be rejected as per the details you've submitted."
        else:
            result = "Your housing loan application is most likely to be accepted as per the details you've submitted."
        
    return render_template('base.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)