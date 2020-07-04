# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from src import text_to_number, check_spell

def test_check_spell_1():
    assert check_spell("cem reais") == "cem reais"
    assert check_spell("cem reais") == "cem reais"
    assert check_spell("cem reais e vinte centavos") == "cem reais e vinte centavos"
    assert check_spell("cem reais e vinte e um centavo") == "cem reais e vinte e um centavo"
    assert check_spell("cem mil trezentos e cinquenta reais e vinte um centavo") == "cem mil trezentos e cinquenta reais e vinte um centavo"
    assert check_spell("dez centavos") == "dez centavos"

def test_check_spell_2():
    assert check_spell("asubdasd cem reais") == "cem reais"
    assert check_spell("cem askmaslx reais") == "cem reais"
    assert check_spell("cem teste reais e vinte centavos") == "cem reais e vinte centavos"
    assert check_spell("cem reais oaisn e vinte e um centavo") == "cem reais e vinte e um centavo"
    assert check_spell("cem mil trezentos e cinquenta alskda reais e vinte um centavo") == "cem mil trezentos e cinquenta reais e vinte um centavo"
    assert check_spell("dez centavos asdnasn ") == "dez centavos"

def test_convert_6():
    assert text_to_number("cem reais") == 100.0
    assert text_to_number("cem reais e vinte centavos") == 100.2
    assert text_to_number("cem reais e vinte e um centavo") == 100.21
    assert text_to_number("cem mil trezentos e cinquenta reais e vinte um centavo") == 100350.21
    assert text_to_number("dez centavos") == 0.1

def test_convert_1():
    assert text_to_number("um") == 1
    assert text_to_number("dois") == 2
    assert text_to_number("três") == 3
    assert text_to_number("quatro") == 4
    assert text_to_number("cinco") == 5
    assert text_to_number("seis") == 6
    assert text_to_number("sete") == 7
    assert text_to_number("oito") == 8
    assert text_to_number("nove") == 9
    assert text_to_number("dez") == 10
    assert text_to_number("onze") == 11
    assert text_to_number("doze") == 12
    assert text_to_number("treze") == 13
    assert text_to_number("catorze") == 14
    assert text_to_number("quinze") == 15
    assert text_to_number("dezesseis") == 16
    assert text_to_number("dezessete") == 17
    assert text_to_number("dezoito") == 18
    assert text_to_number("dezenove") == 19
    assert text_to_number("vinte") == 20
    assert text_to_number("trinta") == 30
    assert text_to_number("quarenta") == 40
    assert text_to_number("cinquenta") == 50
    assert text_to_number("sessenta") == 60
    assert text_to_number("setenta") == 70
    assert text_to_number("oitenta") == 80
    assert text_to_number("noventa") == 90
    assert text_to_number("cem") == 100
    assert text_to_number("duzentos" ) == 200
    assert text_to_number("trezentos" ) == 300
    assert text_to_number("quatrocentos" ) == 400
    assert text_to_number("quinhentos" ) == 500
    assert text_to_number("seiscentos" ) == 600
    assert text_to_number("setecentos" ) == 700
    assert text_to_number("oitocentos" ) == 800
    assert text_to_number("novecentos" ) == 900

def test_convert_2():
    assert text_to_number("vinte e um") == 21
    assert text_to_number("trinta e dois") == 32
    assert text_to_number("quarenta e três") == 43
    assert text_to_number("cinquenta e quatro") == 54
    assert text_to_number("sessenta e cinco") == 65
    assert text_to_number("setenta e seis") == 76
    assert text_to_number("oitenta e sete") == 87
    assert text_to_number("noventa e oito") == 98

def test_convert_3():
    assert text_to_number("trezentos e vinte e um") == 321
    assert text_to_number("quatrocentos e trinta e dois") == 432
    assert text_to_number("quinhentos e quarenta e três") == 543
    assert text_to_number("seiscentos e cinquenta e quatro") == 654
    assert text_to_number("setecentos e sessenta e cinco") == 765
    assert text_to_number("oitocentos e setenta e seis") == 876
    assert text_to_number("novecentos e oitenta e sete") == 987
    assert text_to_number("cento e noventa e oito") == 198

def test_convert_4():
    assert text_to_number("um mil trezentos e vinte e um") == 1321
    assert text_to_number("dois mil quatrocentos e trinta e dois") == 2432
    assert text_to_number("treze mil quinhentos e quarenta e três") == 13543
    assert text_to_number("duzentos e trinta e quatro mil seiscentos e cinquenta e quatro") == 234654

def test_convert_5():
    assert text_to_number("um milhão um mil trezentos e vinte e um") == 1001321
    assert text_to_number("vinte e um milhões dois mil quatrocentos e trinta e dois") == 21002432
    assert text_to_number("trezentos milhões treze mil quinhentos e quarenta e três") == 300013543