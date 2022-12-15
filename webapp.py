import numpy as np
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/') # Homepage
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [int(X) for X in request.form.values()]
    print(features)
    final_feat = [np.array(features)]
    print(final_feat)
    print(len(final_feat))
    prediction = model.predict(final_feat)
    print(prediction)
    
    return render_template('result.html', prediction_text='The Price Range of Smartphone is: {}'.format(prediction)) # rendering the predicted result

if __name__ == "__main__":
    app.run(port=8000)