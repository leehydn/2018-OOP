#=================================================
#  Homework : String
#  ID   : 16-087
#  NAME : Lee Hyeondong
#=================================================

def P1_IsIncreasing (num) :
    data = str(num)
    for i in range(len(data)-1):
        if int(data[i]) > int(data[i+1]):
            return False
    return True


print (P1_IsIncreasing(125678) )   #True
print (P1_IsIncreasing(103481) )   #False

#=================================================

def P2_IsValidPassword (password_str) :
    lowerFlag = False; upperFlag = False; numberFlag = False;
    if len(password_str) > 20 or len(password_str) < 6:
        return False

    for i in password_str:
        index = ord(i)
        if index >= 48 and index <= 57: # number
            numberFlag = True
        if index >= 65 and index <= 90: # uppercase
            upperFlag = True
        if index >= 97 and index <= 122: # lowercase
            lowerFlag = True

    return (numberFlag and upperFlag and lowerFlag)

print( P2_IsValidPassword ("Gohazard123")) #True
print( P2_IsValidPassword ("1234abc"))     #False

#=================================================

def IsPalindrome(s):
    return (s[:(len(s)+1)//2] == s[len(s):len(s)//2-1:-1])

def P3_IsDPalindrome (s):
    for i in s:
        newString = []
        for j in s:
            if j != i:
                newString.append(j)
        if IsPalindrome(newString):
            return True
    return False

print( P3_IsDPalindrome ("abcfddcba"))  #True
print( P3_IsDPalindrome ("bbcddcba"))  #False

#-------------------------------------------------
def P4_IsRotation (s1, s2):
  if len(s1) != len(s2):
    return False

  for i in range(len(s1)):
    if s2 == s1[i:] + s1[:i]:
      return True
  return False

print (P4_IsRotation("honpyt" , "python"))  #True
print (P4_IsRotation("tionvaca", "vacation"))  #True
print (P4_IsRotation("ace" ,"cee")) # False

#=================================================
def toDecimal(s: str):
    temp = 0
    for i in range(len(s)):
        temp += 2 ** (len(s) - i - 1) * int(s[i])
    return temp

def toBinary(n: int):
    return bin(n)[2:]

def P5_AddBinaryNumbers(numbers):
    sum = 0
    for i in numbers:
        sum += toDecimal(i)

    return toBinary(sum)

print ( P5_AddBinaryNumbers( ["101", "1", "11", "0"]) )   # "1001"
print ( P5_AddBinaryNumbers( ["1101101", "110", "1001011", "101110", "110111", "101001", "101", "1", "11", "101101"]) )   # "110000010"



#=================================================

def P6_ExactMatch(text, pattern):
    numArr = []
    for i in range(len(text) - len(pattern) + 2):
        if text[i:i+len(pattern)] == pattern:
            numArr.append(i)

    return numArr

print(P6_ExactMatch ("abcdabcab" , "ab")) #[0,4,7]
print(P6_ExactMatch ("atgaatgcatggatgtaaatgca", "atg"))  #[0,4,8,12,18]
print(P6_ExactMatch ("atgaatgcatggatgtaaatgca", "atgca"))  #[4,18]
print(P6_ExactMatch ("abdbcafc", "abc"))  #[]

#=================================================
def nearMatched(s1, s2):
    difference = 0
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s2[i] != s1[i]:
                difference += 1

        return difference == 1

def P7_NearMatch(text, pattern):
    numArr = []
    for i in range(len(text) - len(pattern) + 2):
        if nearMatched(text[i:i+len(pattern)], pattern):
            numArr.append(i)

    return numArr


print (P7_NearMatch("abdbcafc" , "abc"))   # [0,2,5]
print (P7_NearMatch("atgaatgcatggatgtaaatgca", "atg"))   # [ ]
print (P7_NearMatch("tgaatgcatggatgtaaatgca", "atgca"))   # [7,11]

#=================================================
