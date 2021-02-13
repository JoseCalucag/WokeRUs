from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import pandas as pd
import json
from flask import jsonify
import pymongo
import pickle
import numpy as np



app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'WokeRUS'
app.config['MONGO_URI'] = "mongodb://localhost:27017/WokeRUS"
mongo = PyMongo(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def welcome():
       return render_template('classify.html') # jsonify({'result' : output})

@app.route('/', methods=['POST', 'GET'])
def form_post():
       cs = request.form['Credit_Score']
       eml = request.form['Emp_Length']
       dti = request.form['Debt_income_ratio'] #.format(format, val, grouping=False, monetary=False)
       loa = request.form['Loan_Amount']
       # int_features = [cs, eml, dti, loa]
       # final_features = [np.array(int_features)]
       # prediction = model.predict (final_features)
       # if prediction == {Loan_Staus, 1}
       # return 
       return {'Credit_Score':cs, 'Emp_Length':eml, 'Debt_income_ratio':dti, 'Loan_Amount':loa}

# app.route('/trial', methods=['POST'])
# def trial():
#        # for rendering results on HTML GUI
#        int_features = [float(x) for x in request.form.form_post()]
#        final_features = [np.array(int_features)]
#        prediction = model.predict(final_features)
#        if prediction == {Loan_Status 1}:
#               print (f'you are approved for a loan')

       # else:
       #        print (f'sorry try again later')

#             f'approved'.prediction # how do we ask our model to classify approved or not ???
       # return trial #prediction #render_template ('loan.html', prediction_text = 'You have been {}'.output)

# @app.route("/data")
# def dataset():
#        col = mongo.db.file_accepted
#        c = col.find({'Loan_Amount': 3600}, {'_id' : False})
#        trip = [i for i in c]
#        return render_template('data_table.html', c = list({'trip':c}))

@app.route("/dataset")
def dataset():
       col = mongo.db.file_accepted
       c = col.find({'Loan_Amount' : 3600.0}, {'_id' : False})
       data = [i for i in c]
       #return render_template ('CreditScore.html', data = {'trip': trip}) # jsonify({'result' : output})
       return {'data': data}

# 

# @app.route("/loanrisk", methods=['GET'])
# def background_process():
#        Credit_score = request.args.get.form_post('cs')
       # Emp_length = request.args.get('Employment_Length')
       # Debt_income_ratio = request.args.get(((Gross_Monthly_Debt *12)/Annual_Income)* 100)
       # Loan_Amount = request.args.get('Loan_Amount')
       # float_formatter = '{:.2f}'.format
       
       # user_values = [{'Credit_score': cs}] #, {'Emp_length, Debt_income_ratio, Loan_Amount}]
       # return user_values # jsonify({'result' : output})

if __name__ == "__main__":
       app.run(port=8000, debug=True)