from scrabble_profil import *
scrabble = Scrabble(load_words())


def test_get_word_score():

        failure = False
        words = {"zzzzzzzz": 0, "it": 2, "was": 6, "scored": 9, "waybill": 42, "outgnaw": 12,
                 "fork": 32}

        for word in words.keys():
            score = scrabble.get_word_score(word)
            if score != words[word]:
                print("NIEPOWODZENIE: test_get_word_score()")
                print("\tOczekiwano {} punktów, a uzyskano '{}' dla słowa '{}'".format(words[word], score, word))
                failure = True
            if not failure:
                print("SUKCES: test_get_word_score()")


def test_get_random_score_from_the_list():
    for i in range(10, 21):
        scrabble.get_random_score_from_the_list(i)


test_get_word_score()
print('----------------------------------------------------------------------')
print('WYLOSOWANE SŁOWA O NAJWYŻSZYM WYNIKU.')
scrabble.get_random_high_score_from_the_list()
print('----------------------------------------------------------------------')
print('WYLOSOWANIE SŁOWA Z WYNIKIEM OD 10 DO 20')
test_get_random_score_from_the_list()
