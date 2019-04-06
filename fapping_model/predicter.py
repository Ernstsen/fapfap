from keras.preprocessing.sequence import pad_sequences
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


def generate_text(tokenizer, seed, next_words, model, max_sequence_len):
    output = ''
    for _ in range(next_words):
        token_list = pad_sequences([tokenizer.texts_to_sequences(seed)],
                                   maxlen=max_sequence_len-1, 
                                   padding='pre')
        predecticted = model.predict_classes(token_list, verbose=0)
    
        output += ' {}'.format(tokenizer.index_word[predecticted])
    
    return output


if __name__ == "__main__":

    model = load_model('models/model.h5')
    tokenizer = load(open('models/tokenizer.pkl', 'rb'))
