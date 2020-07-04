# -*- coding: utf-8 -*-

import re
from spellchecker import SpellChecker

import utils

spell = SpellChecker()

def check_spell(text):
    spell.word_frequency.load_words(utils.currency_pt)
    words = [spell.correction(word) for word in text.split(" ")]
    filtered_words = [word for word in words if word in utils.currency_pt]
    return " ".join(filtered_words)

def split_currency(text):
    return re.split("real|reais", text)

def convert_integer(text):
    result = group = 0
    for word in text.split():
        if word in utils.reverse_number_map:
            group += utils.reverse_number_map[word]
        elif word in utils.thousands_map:
            result += max(group, 1) * utils.thousands_map[word]
            group = 0
    result += group
    return result

def convert(text):
    if "real" in text or "reais" in text:
        text_currency = check_spell(text)
        [text_int, text_dec] = split_currency(text_currency)
        value_int = convert_integer(text_int)
        value_dec = convert_integer(text_dec) / 100
        return value_int + value_dec
    elif "centavo" in text:
        return convert_integer(text) / 100
    else:
        return convert_integer(text)


