import binascii
import string
import random

found_answer = False
tries = 0

hashed1 = binascii.crc32('fb5229914d191bf3e14389a8826f8dc8'.encode('utf8'))
trial_int = 72661110
while found_answer == False:
    hashed2 = binascii.crc32(str(trial_int).encode('utf8'))
    if tries % 1000000 == 0:
        print(tries)
    if hashed1 == hashed2:
        found_answer = True
        print(trial_int)
        print(hashed2)
        break
    tries = tries + 1
    trial_int = trial_int + 1

print(tries)


