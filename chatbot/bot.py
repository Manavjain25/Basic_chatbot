import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model

with open('personal.json') as file:
    data = json.load(file)
training_sentences = []
training_labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    
    
vocab_size = 10000
embedding_dim = 16
max_len = 20
trunc_type = 'post'
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
tokenizer.fit_on_texts(training_sentences)

enc = LabelEncoder()
enc.fit(training_labels)
training_labels = enc.transform(training_labels)

my_model =  load_model('My_modal/my_modal.h5')

def user(string):
    result = my_model.predict(pad_sequences(tokenizer.texts_to_sequences([string]),
                                             truncating=trunc_type, maxlen=max_len))
    category = enc.inverse_transform([np.argmax(result)])
    for i in data['intents']:
        if i['tag']==category:
            # if category!=['city']:
            print(i['responses'])
            return np.random.choice(i['responses'])
            # else:
            #     return(i['responses'][0])
        