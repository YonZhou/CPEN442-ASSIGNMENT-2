import binascii
import string
import random

def random_string():
    length = 8
    return ''.join(random.choice(string.ascii_letters) for x in range(length))

found_answer = False
tries = 0
hash_cache = {}
while found_answer == False:
    text = random_string()
    hashed1 = binascii.crc32(text.encode('utf8'))

    text2 = random_string()
    hashed2 = binascii.crc32(text2.encode('utf8'))

    if hashed1 in hash_cache:
        if hash_cache[hashed1] != text:
            found_answer = True
            print(hashed1)
            print(text)
            print(hash_cache[hashed1])
    else:
        hash_cache[hashed1] = text

    if hashed2 in hash_cache:
        if hash_cache[hashed2] != text2:
            found_answer = True
            print(hashed2)
            print(text2)
            print(hash_cache[hashed2])
    else:
        hash_cache[hashed2] = text2

        
    if tries % 10000 == 0:
        print(tries)
    tries = tries + 1
    if hashed1 == hashed2 and text != text2:
        found_answer = True
        print(text)
        print(text2)
        print(hashed1)
        print(hashed2)
        break

print(tries)


