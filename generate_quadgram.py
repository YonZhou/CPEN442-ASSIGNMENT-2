import re

regex = re.compile('[^a-zA-Z]')

text_file = open('./raw_quadgram_playfair.txt', encoding="utf-8")
data = text_file.read().replace('\n', '')
data = regex.sub('', data)
data = data.upper()

## get all 4 length substrings
length_4_substrings = [data[x:x+4] for x in range(len(data)-3)]

quadgram_map = {}
for substring in length_4_substrings:
    if substring in quadgram_map:
        quadgram_map[substring] = quadgram_map[substring] + 1
    else:
        quadgram_map[substring] = 1

quadgram_map = sorted(quadgram_map.items(), key=lambda x: x[1], reverse=True)

with open('quadgram_generated_playfair.txt', 'a') as file_to_write:
    for element in quadgram_map:
        file_to_write.write(str(element[0]) + ' ' + str(element[1]) + '\n')


