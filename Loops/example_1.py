import re


def censor_string(param, param1, param2):
    lst_words = param.split()

    for search_word in param1:
        for word in lst_words:
            if word.startswith(search_word):
                param = param.replace(word, len(word) * param2)

    print(param)


censor_string("Today is a Wednesday!", ["Today", "a"], "-")
