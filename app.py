#import nltk
#nltk.download('popular')
#from nltk.stem import WordNetLemmatizer
#lemmatizer = WordNetLemmatizer()
import pickle
#import numpy as np

#from keras.models import load_model
#model = load_model('model.h5')
import json
import random
#intents = json.loads(open('data.json').read())
#words = pickle.load(open('texts.pkl','rb'))
#classes = pickle.load(open('labels.pkl','rb'))

def clean_up_sentence(sentence):
    return

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    return

def predict_class(sentence, model):
    return 

def getResponse(ints, intents_json):
    return 'hello'

def chatbot_response(msg):
    return 'hello '+msg


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run()

