import random
import string
import numpy as np
from math import log

ciphertext = "OFEHKANVISZMEMVUWZVUBGSQUYQLONCHMOUYOWCZELGZVUIGORONMGSMUCSFIMSFMVFLCLCDROUYOFEXGHYANLLNMLLPONCZELEWLNEWHZLPHZHCMVFLCLVHOQHZSIAYEWBYENMVFLCLOKHPQESEORMSWODVREVUXHCTHWONBSLUBFADIVROMAUYORHZOUSFMHOBLPMVFLCLERFUFEPKXSGZLPZOMSWSHZWEHVKXSFNAVUISZLOFONFSLCUXLBURNZSMURFHHZOIOIBSQUQEMUVBNLCLVHOQHZSBOKNENOCLMOSMLSGEXUALXOSEWEWSFCZAVUZBEDOFVAELYUWSHVWIZMUSXONMONMSQECDUEXVGOPUOXORHZSIAYEWBYENMVFLCLKEKVPKHZSBVUZEBQNLXSISRVEGSFXLXSVTVLHGUOSEORSMCDROUYBQOSMOVTNLCLVHOQSDMVFLCLVKYUQADVLWSMMSVGVUNIMFUSISXOFHMHSBXSPKOZSMHZOKNIMCVBNLCLLPZMUSBSQUQEMUSBDERUUOOFOKHCUWOKKTELMOELMZSMONSIGMLPDVWOOUISNPENDVREVUXHCTHWHVWIQLONDEHZRYSMMNNMIWMNGESFURCZELMIRELPOLZVOUMBNLCLEWNAOSONQYSMSXYPIBILNDORSEWEDVWOIVDNPKHZHCSFLSHWZHOILSHAOMSEWEUWMILWONHBONFSBGHVHPEWHCFOGHXPOBRVESDUSBFSPKDVXEGMSMUSHZDEWODENLONBHEHUAADEKOXDMSMISIUSEOWCDEHFEVBHGMVFLCLLPZOSMUSRCOUOSESVXTONLSBXSPKBSQUQEMUORSMURFBNLCLOQNMBHMOWEGHLPYMNLCLVHOQONDEHZVANLCLOKUWKEDOWEBOGMONHZENPUIOFHHZHCDVHUKAWVUYORMSBOHVHPEWHCUSLYHZHCPUIVWOIMCDBZVFGIMVFLCLLPEGWEORSDONHGBSGCXSEGYVMVFLCLNAVUISMVFLCLLPQOKEALHMOUADELUAAUMEHBSFONHZOUORHZWBYVMSHVCLALAMXUCTWEOKHZWEVUDEMFUSHZDEWODENLMVFLCLLPZMUSVYALXMNDDNBWZLOFONHZVWVOGMORMSNMVBEDWOYBNLCLOKGUVFXAYVHZSWEWHCUSLYMVFLCLCLROELMSMCLPZCXSFPWOIHISIVCKYCWEMVFLCLLPRNSFXUAYEWBXALADCYOKBSQMYAORSMHZOISXLWKTDECFUSBVOXOKWTVYKEEWMVFLCLVHOQSDONFSGHILNOUWXSMOHZSIBYIUOWLPYNHAUOYLHZEWLYMVFLCLMSCLWIHZIUVRSILNESLPZMUSLNHBLSWVMOSMURHZENUCELFHHZSEVOBVGZSOKDXEEWQLONMSATNLCLVXCLESGMQEDNRXOIFBNLCLVHOQHZOUSFMHOBLPONFSAYGMUZENHZSIELMOIMCDEVVFWBUSEWESQEKEGZMVFLCLIVHZHCDVHBLSHWZHSFPUVTNLOKNSHBIMHZSUVUQLONHZWEVUEWHZSVHZWEHZOKTGEXISZMNOVBSOESDVLRSMUSGZENORHZSIAYEWBYENHZOREWIHVHMOHZOBHVGXSULYNEDWGUOWUSISOBORMSUWHZOUVEOUDALYRYSMLPZMUSFSPGILNOCLGOUPHZHCXSGHWEQEMUWUVUGHPUOGSMXSPKURCHDNMSTIFKGOMVFLCLISGPMSWSHZWEMVFLCLKEHZOHHCGHINIUVWHZSOZEOQSIELMZSMHVMIZBUSCUALDNXQXKEWMVFLCLHZIBUAISKEYHZYXUZLLWTHXUCHHOIMDECFUSBVOXOKNZSMSFPUEZVUALADUCUADNMBSMMSPMNLCLURBGUSMNOXPUVGELEWRLNVKOFHHZWUUAUMREWOQMOSYBOURYSMEWUAADMVFLCLVHOQHZSIAYEWBYENMVFLCLDVLEHWZHMSUWHVXUBOONCQELZEOUXQMIEUSOPKEHTAUXLBURNZSMVXFOBVZBXVMDVYCBNLCLLPEGWEORHZOUSFMHOBLPIVQUDEKBHAADURFSBGHVHZSVMDZCXSPKVFELDOONONHGSFONGPMVFLCLNAVUISMVFLCLHZWEVUEWNAOWCZIMTAXVZELPQOKEALHMOUADELCDGHEDRYSMIVHZVRVHMZENPLMOXOGHOWORGUOXSUSBNDZMUSMIALDNKEPKCHUOONFSPUETEDKOMNCLXUGUVANLCLHZHCOIGMESZRCXQBDEFNLPVHVTQEORONDEHZRYSMMNMVFLCLURFSHGCXZBUSQBDETLWEVBNLCLUSVHOQMVFLCLGZXPOKTZOIUSLYHCUSZELYADONBGUSKOWZWBAWEFVBLCVUESGMQEDNRXOIFBNLCLLPYLFHHZHCEKHVESZRBWALHMYUOKORCRHPEWHCCLGHWEONFSAYKOFOCHBSLPQPOKONCXFEZYEDUWHVMZSMUSEWUSBOBWZONDKFVUFKFHBSGMXUFHMSMSWYVFWIRLGAOIVUZELPODILINORSEWERPUSEWMSISWBUSEWGZWBHV"
key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def remove_xs(strs):
    return strs.replace('X', '')

def apply_key(ciphertext_param, key_param):
    key_table = np.array(np.array(list(key_param))).reshape(5, 5)
    decoded_string = ""
    for i in range(0, len(ciphertext_param), 2):
##    for i in range(0, 4, 2):  
        char1, char2 = ciphertext_param[i:i+2]
        ## search
        if char1 == "J":
            char1 = "I"
        elif char2 == "J":
            char2 = "I"
            
        ch1rowarr, ch1columnarr =  np.asarray(np.where(key_table == char1))
        ch1_row = ch1rowarr[0]
        ch1_column = ch1columnarr[0]

        ch2rowarr, ch2columnarr =  np.asarray(np.where(key_table == char2))
        ch2_row = ch2rowarr[0]
        ch2_column = ch2columnarr[0]

        if ch1_column == ch2_column:
            decoded_string = decoded_string + key_table[(ch1_row-1) % 5][ch1_column]
            decoded_string = decoded_string + key_table[(ch2_row-1) % 5][ch2_column]
        elif ch1_row == ch2_row:
            decoded_string = decoded_string + key_table[ch1_row][(ch1_column-1) % 5]
            decoded_string = decoded_string + key_table[ch2_row][(ch2_column - 1) % 5]
        else:
            decoded_string = decoded_string + key_table[ch1_row][ch2_column]
            decoded_string = decoded_string + key_table[ch2_row][ch1_column]


    return decoded_string

def num2dto_string(array):
    array2 = array.flatten()
    arraylist = array2.tolist()
    return "".join(arraylist)

def shuffle_two_letters(key_param):
    x = random.randint(0, 24)
    y = random.randint(0, 24)
    return swap(key_param, x, y)

def shuffle_key_parent(key_param):
    option = random.randint(1, 6)
    #print(option)
    key_table = np.array(np.array(list(key_param))).reshape(5, 5)
    if option == 1:
        #swap 2 rows
        row1 = random.randint(0, 4)
        row2 = random.randint(0, 4)
        key_table[[row1, row2]] = key_table[[row2, row1]]
        return num2dto_string(key_table)
    elif option == 2:
        col1 = random.randint(0, 4)
        col2 = random.randint(0, 4)
        #swap 2 columns
        key_table[:,[col1, col2]] = key_table[:,[col2, col1]]
        return num2dto_string(key_table)
    elif option == 3:
        return num2dto_string(np.flip(key_table, 0))
    elif option == 4:
        return num2dto_string(np.flip(key_table, 1))
    elif option == 5:
        #print(key_param)
        #print(key_param[::-1])
        return key_param[::-1]
    else:
        return shuffle_two_letters(key_param)
    
def shuffle_key(key_param):
    option = random.randint(1, 60)
    #print(option)
    key_table = np.array(np.array(list(key_param))).reshape(5, 5)
    if option == 1:
        #swap 2 rows
        row1 = random.randint(0, 4)
        row2 = random.randint(0, 4)
        key_table[[row1, row2]] = key_table[[row2, row1]]
        return num2dto_string(key_table)
    elif option == 2:
        col1 = random.randint(0, 4)
        col2 = random.randint(0, 4)
        #swap 2 columns
        key_table[:,[col1, col2]] = key_table[:,[col2, col1]]
        return num2dto_string(key_table)
    elif option == 3:
        return num2dto_string(np.flip(key_table, 0))
    elif option == 4:
        return num2dto_string(np.flip(key_table, 1))
    elif option == 5:
        #print(key_param)
        #print(key_param[::-1])
        return key_param[::-1]
    else:
        return shuffle_two_letters(key_param)
        
            
    

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
    quadgram_data = open('./quadgram_generated_playfair.txt')
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
    
tries_without_improving = 0
best_score = -999999999999999
best_string = ciphertext
best_key = key

init_quadgrams()

parent_key = key

while True:
    tries_without_improving = 0
    parent_key = shuffle_key_parent(parent_key)
    parent_decoded_string = apply_key(ciphertext, parent_key)
    parent_score = check_score(parent_decoded_string)
    
    while tries_without_improving < 1000:
        #print("Old key: "+parent_key)
        new_key = shuffle_key(parent_key)
        #print("new key: " + new_key)
        new_decoded_string = apply_key(ciphertext, new_key)
        new_score = check_score(new_decoded_string)

        if new_score > parent_score:
            tries_without_improving = 0
            parent_key = new_key
            parent_score = new_score
        else:
            tries_without_improving = tries_without_improving + 1

    print("1000 tries finished")
    if parent_score > best_score:
        best_score = parent_score
        best_key = parent_key

        print(best_score)
        print(best_key)
        print(apply_key(ciphertext, best_key))

