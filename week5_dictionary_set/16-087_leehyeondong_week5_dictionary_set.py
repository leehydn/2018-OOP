#=================================================
#  Homework : Dictionary and Set 
#  ID   : 16-087
#  NAME : Lee Hyeondong
#=================================================
import string

###################################################
#################### Problem 1 ####################
###################################################
def P1_LongWords():
    text_file = open("./words.txt", 'r'); data = text_file.read().split()
    counter = 0;
    for i in data:
        if len(i) > 18:
            counter += 1

    text_file.close()
    return counter

print("#1")
print(P1_LongWords())  # 24
print()
###################################################
#################### Problem 2 ####################
###################################################
def P2_WordsWithoutE():
    text_file = open("./words.txt", 'r'); data = text_file.read().split()
    counter = 0;
    for i in data:
        if not 'e' in i.lower():
            counter += 1

    text_file.close()
    return counter

print("#2")
print (P2_WordsWithoutE())  #37641
print()
###################################################
#################### Problem 3 ####################
###################################################
def isAbecedarian(word):
    for i in range(len(word) - 1):
        if word[i] > word[i+1]:
            return False
    return True
    
def P3_Abecedarian():
    text_file = open("./words.txt", 'r'); data = text_file.read().split()
    counter = 0;
    for i in data:
        if isAbecedarian(i):
            counter += 1

    text_file.close()
    return counter

print("#3")
print (P3_Abecedarian())    #596
print()

###################################################
#################### Problem 4 ####################
###################################################
import csv

def P4_BelowEquator():
    data_file = open("./locations.csv", "r")
    data = csv.reader(data_file)
    country_dict = {}
    
    for row in data:
        country_dict[row[1]] = row[2]

    below_list = []
    for i in country_dict:
        try:
            if float(country_dict[i]) < 0:
                below_list.append(i)
        except:
            continue

    data_file.close()
    return below_list

print("#4")
BE = P4_BelowEquator()
print (len(BE) , BE)  # 58 ['Angola', 'Antarctica', ... 'Zimbabwe']  
print()

###################################################
#################### Problem 5 ####################
###################################################

def P5_CountryNames(codes):
    data_file = open("./locations.csv", "r")
    data = csv.reader(data_file)
    country_dict = {}
    
    for row in data:
        country_dict[row[0]] = row[1]
    
    data_file.close()
    return list(map(lambda key: country_dict[key], codes))


# -----for Test -----
print("#5")
codes = ["KR", "BR", "VN", "DE", "AR", "JP", "US"]
print (P5_CountryNames(codes))  # ['Korea, Republic of', 'Brazil', 'Vietnam', 'Germany','Argentina', 'Japan', 'United States']
print()


###################################################
#################### Problem 6 ####################
###################################################
def P6_Temperature():
    new_file = open("./temperature.csv", "w")
    temp = open("./temperature.txt", "r")
    data = []
    for i in temp.readlines():
      data.append(i.split())

    for i in range(len(data)):
      winter = round((float(data[i][0]) + float(data[i][1])) / 2, 2)
      summer = round((float(data[i][6]) + float(data[i][7])) / 2, 2)
      csv.writer(new_file).writerow( [ i+1723, winter , summer ] )

    temp.close()
    new_file.close()
    return 0

print ("#6\nOpen and read file \"temperature.csv\" !!!")
P6_Temperature()
print()
      

###################################################
#################### dictionary ###################
###################################################
def createPronunciationDictionary():
    d = {}
    f = open("cmudict.txt", "r")
    for line in f:
        if line[0] == "#":
            continue
        words = line.split()
        if words[0].isalpha():
            d[words[0].lower()] = "".join(words[1:])
    return d

###################################################
#################### Problem 7 ####################
###################################################

def P7_InverseDictionary(f):
    new_dict = {}
    for i in f.keys():
      if f[i] in new_dict:
        new_dict[f[i]].append(i)
      else:
        new_dict[f[i]] = [i]
    
    return new_dict

print("#7")
f = {1: 'a', 2:'b', 3 :'c', 4 :'d' , 10:'a' ,20 :'b' }
invf = P7_InverseDictionary(f)
print(invf)   #{'c': [3], 'b': [2, 20], 'a': [1, 10], 'd': [4]}  ==> no order
print()
    
###################################################
#################### Problem 8 ####################
###################################################
def P8_Homophones(n):
    d = createPronunciationDictionary()
    inv = P7_InverseDictionary(d)
    counter = 0

    for key in inv:
       if len(inv[key]) >= n:
           counter += 1

    return counter 

print("#8")
print (P8_Homophones(2))  # 8748
print (P8_Homophones(6))  # 134
print (P8_Homophones(10))  # 5
print()

###################################################
#################### Problem 9 ####################
###################################################
def P9_HomophoneRemovingFirst():
    d = createPronunciationDictionary()
    counter = 0

    for word in d:
        try:
            if d[word] == d[word[1:]]:
                counter += 1
        except:
            continue
    return counter

print("#9")
print (P9_HomophoneRemovingFirst())  #147
print()

###################################################
#################### Problem 10 ####################
###################################################
def P10_HomophoneRemovingSecond():
    d = createPronunciationDictionary()
    counter = 0

    for word in d:
        try:
            if d[word[1:]] == d[word[0] + word[2:]]:
                if d[word] == d[word[1:]]:
                    counter += 1
        except:
            continue
            
    return counter

print("#10")
print  (P10_HomophoneRemovingSecond() ) # 11
print()


###################################################
#################### Problem 11 ################### 
###################################################

def car_dictionary(file_obj):
    new_dict = {}
    for line in file_obj:
        a = line.split()

        year, company = a[0], a[1]
        a.remove(year); a.remove(company)
        model = " ".join(a)
        if company in new_dict:
            new_dict[company].append((year, model))
        else:
            new_dict[company] = [(year, model)]

    return new_dict


def P11_MaxWorstCars(car_dict):
    worst = None; max_num = 0;
    for man in car_dict:
        if len(car_dict[man]) > max_num:
            worst = man
            max_num = len(car_dict[man])

    return worst

print("#11") 
file_obj=open('./cars.txt','r')
car_dict = car_dictionary(file_obj)
worst_manufacturer = P11_MaxWorstCars(car_dict)
print("Worst manufacturer:",worst_manufacturer)
print("Cars:")
for y, m in car_dict[worst_manufacturer]:
    print(y, m)

print()
###################################################
#################### Problem 12 ################### 
###################################################

def P12_CompareFiles ():
    harvard_data = open("./Havard.txt", 'r', encoding='cp949')
    mit_data = open("./MIT.txt", "r", encoding='cp949')
    harvard_wset = set()
    mit_wset = set()

    for line in harvard_data:
        line_list = list(line.split())
        for word in line_list:
            word = word.strip()
            if len(word.strip(string.punctuation).lower()) >= 4:
                harvard_wset.add(word.strip(string.punctuation).lower())
                
    for line in mit_data:
        line_list = list(line.split())
        for word in line_list:
            word = word.strip()
            if len(word.strip(string.punctuation).lower()) >= 4:
                mit_wset.add(word.strip(string.punctuation).lower())

    print("Count of unique words of length 4 or greater")
    print("Harvard: {}, MIT: {}".format(len(harvard_wset), len(mit_wset)))
    print()
    print(" Operations                 Count ")
    print("==================================")
    print("{} {:>27}".format("Union", len(harvard_wset.union(mit_wset))))
    print("{} {:>20}".format("Intersection", len(harvard_wset.intersection(mit_wset))))
    print("{} {:>12}".format("Symmetric Difference", len(harvard_wset.symmetric_difference(mit_wset))))
    print("{} {:>21}".format("Harvard-MIT", len(harvard_wset.difference(mit_wset))))
    print("{} {:>21}".format("MIT-Harvard", len(mit_wset.difference(harvard_wset))))

print("#12")
P12_CompareFiles()