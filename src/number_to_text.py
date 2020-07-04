# -*- coding: utf-8 -*-

import utils

def split_number(n:int):
    n_rev = str(n)[::-1]
    splited = [n_rev[i:i+3][::-1] for i in range(0,30,3)]
    respose = [int(i) for i in splited[::-1] if i]
    return respose

def decompose_number(n:int):
    if n >= 100:
        return (int(n/100)*100, n%100)
    elif n >= 10:
        return (int(n/10)*10, n%10)
    else:
        return (None, n)

def convert_hundreds(n:int)->str:
    converted = utils.number_map.get(str(n))
    if converted is None:
        (n1, n2) = decompose_number(n)
        if n1 == 100:
            return f"{utils.number_map[f'{n1}s']} e {convert_hundreds(n2)}"
        else:
            return f"{utils.number_map[str(n1)]} e {convert_hundreds(n2)}"
    else:
        return converted

def convert(n:int)->str:
    response = []
    if n == 0:
        return "zero"
    chunks = split_number(n)
    for i, chunk in enumerate(chunks):
        chunk_id = len(chunks) - i - 1
        if chunk_id > 0:
            if chunk == 1:
                milliards = " " + utils.number_map[f'1e{chunk_id*3}']
            else:
                milliards = " " + utils.number_map[f'1e{chunk_id*3}s']
        else:
            milliards = ""
        if chunk > 0:
            if chunk_id == 0 and chunk <= 100 and len(chunks) > 1:
                response.append("e " + convert_hundreds(chunk) + milliards)
            else:
                response.append(convert_hundreds(chunk) + milliards)
    return " ".join(response)
