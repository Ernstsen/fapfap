from keras.preprocessing.sequence import pad_sequences
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


def generate_text(tokenizer, seed, next_words, model, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
        
        output_word = ""
        for word,index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed += " "+output_word

    return seed


if __name__ == "__main__":

    model = load_model('models/model.h5')
    tokenizer = load(open('models/tokenizer.pkl', 'rb'))
    prediction = generate_text(tokenizer, "hello", 10, model, 15)
    print(prediction)
