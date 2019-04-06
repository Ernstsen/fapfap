import string, os 

from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import keras.utils as ku 
from tqdm import tqdm
from keras import backend as k

from pickle import dump

# set seeds for reproducability
from tensorflow import set_random_seed
from numpy.random import seed
set_random_seed(2)
seed(1)

import pandas as pd
import numpy as np


import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)


from keras.preprocessing.sequence import pad_sequences
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

def load_model_and_tokenizer():
    model = load_model('models/model.h5')
    tokenizer = load(open('models/tokenizer.pkl', 'rb'))
    return model, tokenizer


def read_dataset(source):
    print('Reading data')
    with open(source, 'r') as dataset:
        return set(dataset.read().split('\n'))


def clean_line(line):
    return ''.join([x.lower() for x in line if x not in string.punctuation])


def clean_data(data):
    print('Cleaning data')
    clean_set = []
    for line in data:
        clean_set.append(clean_line(line))
    return clean_set


def tokenize(tokenizer, corpus):
    print('Tokenizing')

    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1

    token_sequences = []
    for line in tqdm(corpus):
        print(line)
        token_list = tokenizer.texts_to_sequences([line])[0]
        if len(token_list) > 15:
            continue 
        for i in range(1, len(token_list)):
            
            token_sequences.append(token_list[:i+1])
    
    return tokenizer, total_words, token_sequences


def pad_text(token_sequences, total_words):
    print('Padding data')
    max_length = 0 
    for i in tqdm(token_sequences):
        if len(i) > max_length:
            max_length = len(i)
    
    padded_sequences = np.array(pad_sequences(token_sequences,
                                              maxlen=max_length,
                                              padding='pre'))
    predictors, label = padded_sequences[:,:-1], padded_sequences[:,-1]
    label = ku.to_categorical(label, num_classes=total_words)
    return predictors, label, max_length


def second_fit_model(model, predictors, label, e=10, v=2):
    print('Training model')
    model.fit(predictors, label, epochs=e, verbose=v) 
    return model


def save_and_dump(model, tokenizer):
    print('saving model and tokenizer')
    model.save('models/pickup_model.h5')
    dump(tokenizer, 
        open('models/pickup_tokenizer.pkl', 'wb'))   


def post_process():
    if not os.path.isdir('./models'):
        os.mkdir('./models')

    model, tokenizer = load_model_and_tokenizer()

    data = read_dataset('dataset/Pickup.txt')
    
    cleaned_data = clean_data(data)
    
    tokenizer, total_words, training_data = tokenize(tokenizer, cleaned_data)

    predictors, labels, max_len = pad_text(training_data, total_words)

    fitted_model = second_fit_model(model, predictors, labels)

    save_and_dump(fitted_model, tokenizer)
    print('Fucking done again')


if __name__ == "__main__":
    post_process()
