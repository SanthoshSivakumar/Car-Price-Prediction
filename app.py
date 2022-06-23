from flask import Flask, render_template, request
# import jsonpify
# flask.jsonpify()
import requests
import pickle
import numpy as np
import sklearn

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        print(request)
        km_driven = int(request.form['km_driven'])
        noofyear = int(request.form['noofyear'])
        fuel_diesel = int(request.form['fuel_diesel'])
        seller_type_individual = int(request.form['seller_type_individual'])
        transmission_manual = int(request.form['transmission_manual'])
        
        prediction=model.predict([[km_driven,noofyear,fuel_diesel,seller_type_individual,transmission_manual,]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)