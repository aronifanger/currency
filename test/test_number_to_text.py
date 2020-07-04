# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from src import number_to_text

def test_convert_1():
    assert number_to_text(0) == "zero"
    assert number_to_text(1) == "um"
    assert number_to_text(2) == "dois"
    assert number_to_text(3) == "três"
    assert number_to_text(4) == "quatro"
    assert number_to_text(5) == "cinco"
    assert number_to_text(6) == "seis"
    assert number_to_text(7) == "sete"
    assert number_to_text(8) == "oito"
    assert number_to_text(9) == "nove"
    assert number_to_text(10) == "dez"
    assert number_to_text(11) == "onze"
    assert number_to_text(12) == "doze"
    assert number_to_text(13) == "treze"
    assert number_to_text(14) == "quatorze"
    assert number_to_text(15) == "quinze"
    assert number_to_text(16) == "dezesseis"
    assert number_to_text(17) == "dezessete"
    assert number_to_text(18) == "dezoito"
    assert number_to_text(19) == "dezenove"
    assert number_to_text(20) == "vinte"
    assert number_to_text(30) == "trinta"
    assert number_to_text(40) == "quarenta"
    assert number_to_text(50) == "cinquenta"
    assert number_to_text(60) == "sessenta"
    assert number_to_text(70) == "setenta"
    assert number_to_text(80) == "oitenta"
    assert number_to_text(90) == "noventa"
    assert number_to_text(100) == "cem"
    assert number_to_text(200) == "duzentos" 
    assert number_to_text(300) == "trezentos" 
    assert number_to_text(400) == "quatrocentos" 
    assert number_to_text(500) == "quinhentos" 
    assert number_to_text(600) == "seiscentos" 
    assert number_to_text(700) == "setecentos" 
    assert number_to_text(800) == "oitocentos" 
    assert number_to_text(900) == "novecentos" 

def test_convert_2():
    assert number_to_text(21) == "vinte e um"
    assert number_to_text(32) == "trinta e dois"
    assert number_to_text(43) == "quarenta e três"
    assert number_to_text(54) == "cinquenta e quatro"
    assert number_to_text(65) == "sessenta e cinco"
    assert number_to_text(76) == "setenta e seis"
    assert number_to_text(87) == "oitenta e sete"
    assert number_to_text(98) == "noventa e oito"

def test_convert_3():
    assert number_to_text(321) == "trezentos e vinte e um"
    assert number_to_text(432) == "quatrocentos e trinta e dois"
    assert number_to_text(543) == "quinhentos e quarenta e três"
    assert number_to_text(654) == "seiscentos e cinquenta e quatro"
    assert number_to_text(765) == "setecentos e sessenta e cinco"
    assert number_to_text(876) == "oitocentos e setenta e seis"
    assert number_to_text(987) == "novecentos e oitenta e sete"
    assert number_to_text(198) == "cento e noventa e oito"

def test_convert_4():
    assert number_to_text(1321) == "um mil trezentos e vinte e um"
    assert number_to_text(2432) == "dois mil quatrocentos e trinta e dois"
    assert number_to_text(13543) == "treze mil quinhentos e quarenta e três"
    assert number_to_text(234654) == "duzentos e trinta e quatro mil seiscentos e cinquenta e quatro"

def test_convert_5():
    assert number_to_text(1001321) == "um milhão um mil trezentos e vinte e um"
    assert number_to_text(21002432) == "vinte e um milhões dois mil quatrocentos e trinta e dois"
    assert number_to_text(300013543) == "trezentos milhões treze mil quinhentos e quarenta e três"