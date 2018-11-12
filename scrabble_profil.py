import random

SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                 for letter in letters.split()}


def load_words():
    print('Ładuje listę wyrazów z pliku...')
    file = open('words.txt', 'r')
    list_words = [word.strip() for word in file]
    print('Załadowano {} wyrazów.'.format(len(list_words)))
    return list_words


class Scrabble(object):

    def __init__(self, list_words):
        if type(list_words) == list:
            self.list_words = list_words
        else:
            raise TypeError('Parametr must be a list')

    def is_valid_word(self, word):
        try:
            if word.upper() in self.list_words:
                print("Słowo '{}' znajduje się w słowniku.".format(word))
                return True
            print("Słowo '{}' nie znajduje się w słowniku.".format(word))
        except AttributeError:
            print('Parametr must be a string')

    def get_word_score(self, word):
        try:
            total = 0
            if not self.is_valid_word(word):
                return False
            for letter in word.upper():
                total += LETTER_SCORES[letter]
            print("Wynik słowa '{}': {}".format(word, total))
            return total
        except TypeError:
            print('Parametr must be a string')

    def get_dict_score_words(self):
        dict_score_words = {}
        for word in self.list_words:
            score = 0
            for letter in word:
                score += LETTER_SCORES[letter]
            if score not in dict_score_words:
                dict_score_words[score] = []
            dict_score_words[score].append(word)
        return dict_score_words

    def get_list_high_score_words(self):
        dict_words = self.get_dict_score_words()
        high_score = max(dict_words)
        return dict_words[high_score]

    def get_random_high_score_from_the_list(self):
        random_word = random.choice(self.get_list_high_score_words())
        print("Słowo o najwyższym wyniku: {}".format(random_word))
        return random_word

    def get_list_words(self, value):
        try:
            dict_words = self.get_dict_score_words()
            return dict_words[value]
        except KeyError:
            print('Argument musi być liczbą lub brak słowa o podanym wyniku.')
            return None

    def get_random_score_from_the_list(self, value):
        try:
            random_word = random.choice(self.get_list_words(value))
            print("Wylosowane słowo z wynikem {}: {}".format(value, random_word))
            return random_word
        except TypeError:
            pass
