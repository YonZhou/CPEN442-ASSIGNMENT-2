import random
import string
from math import log

ciphertext = "UACVQJMSTGFBMASTDBGFXUQQTTCBXZGZQTGRZFFUSGBHESXUQQTTMJMJTCXUQQTMTBFSEZFJXEZMMIETSTXCZTGITVVUJETWZUNYJSSBAHSEBAHMBSMTQBAZGTCXUQQTBSEBARXUQQTMTBFTCBXZFUSUNXUJGMZBSBMXUQQTMTBFSEZFJXEZMMXUQQTIEUMZZQZFGZTFVSUTHGZZSUZWZGVSEBAHSETSTCBXZMTBFSEZGZMTCTGHZQJMSTGFQBAZAZTGEZGZFUSTAFSEZQUGTCUNSETSBMSEZQUGZSEZGZBMUNQBAZXUQQTSEZCZMMSEZGZBMUNVUJGMFUSUEXUQQTBRAUIZKXCTBQZFTCBXZXUQQTIEUETFAUSTSSZAFZFSUSEBMCTMSGZQTGRXUQQTBSMTWZHZSTDCZFUSBSFUZMASCUURCBRZUAZXUQQTDJSBSBM"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def apply_key(ciphertext_param, key_param):
    translate_table = ciphertext.maketrans(alphabet, key_param)
    decoded_string = ciphertext_param.translate(translate_table)
    return decoded_string

def shuffle_key(key):
    x = random.randint(0, 25)
    y = random.randint(0, 25)
    return swap(key, x, y)

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def init_quadgrams():
    global quadgram_table
    global total_quadgram_count
    global min_quadgram_score
    quadgram_table = {}
    total_quadgram_count = 0
    min_quadgram_score = 0
    quadgram_data = open('./quadgram_generated.txt')
    for line in quadgram_data:
        quadgram, count = line.split(' ')
        quadgram_table[quadgram] = log(float(count))
        total_quadgram_count += int(count)

    min_quadgram_score = 1.0  

def check_score(decoded_string):
    score = 0
##    decoded_string_cleaned = remove_xs(decoded_string)
    decoded_string_cleaned = decoded_string
    length_4_substrings = [decoded_string_cleaned[x:x+4] for x in range(len(decoded_string_cleaned)-3)]
    for substring in length_4_substrings:
        if substring in quadgram_table:
            score = score + quadgram_table[substring]
        else:
            score = score + min_quadgram_score
    return score   

apply_key(ciphertext, key)

best_score = -999999999999999
best_string = ciphertext
best_key = key
parent_key = key

init_quadgrams()

while True:
    tries_without_improving = 0
    parent_key = shuffle_key(parent_key)
    while tries_without_improving < 1000:
        new_key = shuffle_key(parent_key)
        new_decoded_string = apply_key(ciphertext, new_key)
        
        new_score = check_score(new_decoded_string)

        if new_score > best_score:
            print(new_score)
            print(new_decoded_string)
            print(new_key)
            tries_without_improving = 0
            best_score = new_score
            best_string = new_decoded_string
            parent_key = new_key
        else:
            tries_without_improving = tries_without_improving + 1
