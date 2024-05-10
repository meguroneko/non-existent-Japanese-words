def batch_replace(s, rules):
    for k in rules.keys(): s = s.replace(k, rules[k])
    return s

from random import choices, randint
import random

def japanese(count=1):
    syll = ["а", "и", "у", "э", "о", "я", "ю", "ё", "ка", "ки", "ку", "кэ", "ко", "кя", "кю", "кё", "са", "си", "су", "сэ", "со", "ся", "сю", "сё", "та", "ти", "цу", "тэ", "то", "тя", "тю", "тё", "на", "ни", "ну", "нэ", "но", "ня", "ню", "нё", "ха", "хи", "фу", "хэ", "хо", "хя", "хю", "хё", "ма", "ми", "му", "мэ", "мо", "мя", "мю", "мё", "я", "ю", "ё", "ра", "ри", "ру", "рэ", "ро", "ря", "рю", "рё", "ва", "ви", "вэ", "о", "н", "га", "ги", "гу", "гэ", "го", "гя", "гю", "гё", "дза", "дзи", "дзу", "дзэ", "дзо", "дзя", "дзю", "дзё", "да", "дзи", "дзу", "дэ", "до", "дзя", "дзю", "дзё", "ба", "би", "бу", "бэ", "бо", "бя", "бю", "бё", "па", "пи", "пу", "пэ", "по", "пя", "пю", "пё"]
    yoted = list("яёюые")
    unyoted = list("аоуиэ")
    forbidden_ends_of_words = "эы"

    replace_rules = {
        "ая": "оя",
        "оё": "ое",
        "эе": "ое",
        "яа": "а",
        "ёо": "о",
        "юу": "ю",
        "еэ": "е",
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "ээ": "э",
        "яя": "я",
        "ёё": "ё",
        "эё": "ё",
        "юю": "ю",
        "ии": "и",
        "ее": "е"
    }
    c = 0
    words = ""
    while c < count:
        word = choices(syll, k=randint(2, 4))
        if word[0] == 'н': word = word[1:] + ['н']
        if word[-1][-1] in forbidden_ends_of_words: word[-1] = word[-1][:-1] + "а"
        for i in range(len(word)):
            if word[i-1][-1] in yoted and word[i][-1] in yoted:
                word[i] = word[i][:-1] + unyoted[yoted.index(word[i][-1])]
            while word[i-1][:2] == 'дз' and word[i][:2] == 'дз':
                word[i] = random.choice(syll)
        words = f"{words + ', ' if words != '' else ''}{batch_replace(''.join(word), replace_rules)}"
        c += 1
    return words