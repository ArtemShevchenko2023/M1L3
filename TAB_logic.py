import time
import random
def gen_pass(pass_length):
    elements = "\|~`№%^:()_[];.,+-/*!&$#?=@<>0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    passwor = ""
    for i in range(pass_length):
        passwor += random.choice(elements)
    return passwor
gen_pass(1)
def gen_pas(pass_lengt):
    element = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    passwor = ""

    for k in range(pass_lengt):
        passwor += random.choice(element)
    return passwor
gen_pas(1)
def gen_pa(pass_leng):
    elemen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    passwo = ""

    for g in range(pass_leng):
        passwo += random.choice(elemen)
    return passwo
gen_pa(1)
def gen_p(pass_len):
    eleme = "0123456789"
    passw = ""

    for f in range(pass_len):
        passw += random.choice(eleme)
    return passw
gen_p(1)
def gen_(pass_le):
    elem = "\|~`№%^:()_[];.,+-/*!&$#?=@<>"
    pas = ""

    for q in range(pass_le):
        pas += random.choice(elem)
    return pas
gen_(1)
def localtime():
    seconds = time.time() + 202
    local_time = time.ctime(seconds)
    return local_time
localtime()
def loctime():
    seconds = time.time() + 202 - 3600
    locatime = time.ctime(seconds)
    return locatime
loctime()