from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))  # ml model loaded

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    f=[float(x) for x in request.form.values()]
    fea=[np.array(f)]
    pred=model.predict(fea)
    return render_template('index.html',predicted_text=f'The predicted crop is {pred[0]}')

if __name__=="__main__":
    app.run(debug=True)