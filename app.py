from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import json
import requests

app = Flask(__name__)
model = pickle.load(open('data/model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html', form = createForm())

@app.route('/predict', methods=['POST'])
def predict():
    form_answers = request.form
    final_features = [[]];
    for answer in form_answers:
        final_features[0].append(answer[1])
    prediction = model.predict(final_features)
    if prediction == [1]: 
       output = 'You\'re not divorced'
    else:
        output = 'You will be divorced'

    return render_template('answer.html', answer=output)

def createForm():
    with open('data/questions.json') as json_file:
        data = json.load(json_file)
    questions = data['questions']
    form = ''
    for question in questions:
        id = question['id']
        q = question.get('question')
        form += f""" <div class = "question-holder">
                <p>{id}. {q}</p>

                <input type = "radio" id="strongly-disagree-{id}" name="q{id}" value="0">
                <label for="strongly-disagree-{id}">Strongly Disagree</label>

                <input type = "radio" id="disagree-{id}" name="q{id}" value="1">
                <label for="disagree-{id}">Disagree</label>

                <input type = "radio" id="uncertain-${id}" name="q{id}" value="2">
                <label for="uncertain-{id}">Uncertain</label>

                <input type = "radio" id="agree-{id}" name="q{id}" value="3">
                <label for="agree-{id}">Agree</label>

                <input type = "radio" id="strongly-agree-{id}" name="q{id}" value="4">
                <label for="strongly-agree-{id}">Strongly Agree</label>
            </div>"""
    return form
    
if __name__ == '__main__':
    app.run(debug=True)