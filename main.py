from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker



import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

#engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)



@app.route('/register/<data>',methods=["GET"])
def home(data):
    from sklearn.externals import joblib
    cv = CountVectorizer()
    NB_spam_model = open('NB_spam_model.pkl','rb')
    clf = joblib.load(NB_spam_model)
    data = data.split("%20")
    data = str(data).replace("[","").replace("]","")

    #return data
    #data = cv.fit_transform(data)
    data = [data]
    #return data
    print(data)
    data = cv.transform(data).toarray()
    print(data)
    result = clf.predict(data)
    if result==[0]:
        return "ham"
    else:
        return "spam"
    #return render_template("home.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
