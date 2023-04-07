import pymorphy3


def is_contains_stop_words(string: str, stop_words: list):
    inf_stop_words = []
    morph = pymorphy3.MorphAnalyzer(lang='ru')
    for stop_word in stop_words:
        inf_stop_words.append(morph.parse(stop_word)[0].normal_form)
    for word in string.split():
        inf_word = morph.parse(word)[0].normal_form
        if inf_word in inf_stop_words:
            return True
    return False



