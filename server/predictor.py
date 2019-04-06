import random
from pickle import load

from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


class Predictor:
    __instance = None

    @staticmethod
    def getInstance(model_path, token_path):
        """ Static access method. """
        if Predictor.__instance is None:
            Predictor.__instance = Predictor(model_path, token_path)
        return Predictor.__instance

    def __init__(self, model_path, token_path):
        self.model = load_model(model_path)
        self.tokenizer = load(open(token_path, 'rb'))
        self.max = len(self.tokenizer.word_index.items())

    def generate_text(self, seed, next_words, max_sequence_len):
        for i in range(next_words):
            token_list = self.tokenizer.texts_to_sequences([seed])[0]
            token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
            predicted = self.model.predict_classes(token_list, verbose=0)

            output_word = ""
            for word, index in self.tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            seed += " " + output_word

        return seed

    def predict(self):
        return self.generate_text(self.getSeed(), 5, 15)

    def getSeed(self):
        rand_index = random.randint(0, self.max)
        print(str(rand_index))
        seed = self.tokenizer.index_word.get(rand_index)
        print(seed)
        return seed


if __name__ == "__main__":
    pred = Predictor.getInstance('fapping_model/models/model.h5', 'fapping_model/models/tokenizer.pkl')
    # model = load_model('fapping_model/models/model.h5')
    # tokenizer = load(open('fapping_model/models/tokenizer.pkl', 'rb'))
    # prediction = generate_text(tokenizer, "hello", 10, model, 15)
    # print(prediction)
    predict = pred.predict()
    print(predict)
