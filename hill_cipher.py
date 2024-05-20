
#import the needed library
from math import sqrt, gcd
import numpy as np
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#take input from user
passW = input("message(in capital letter and with an even length): ")
key = input("key(please enter 4 capital letters): ")
flag = True

#mutiply 2 2x2 matrices
def muptiply(maA, maB):
    test = np.dot(maA, maB)
    result = []
    for i in test:
        result.append(i)
    return result

#calculate the determinant of matrix
def det(mat):
    a, b = mat[0]
    c, d = mat[1]
    return a*d - b*c

#calculate the inverse matrix on Z26
def inverse(mat):
    i = 1
    a, b = mat[0]
    c, d = mat[1]
    de = det(mat)
    while True:
        if ((de*i)%26 == 1):
            de = i
            break
        i+=1

    mat = [[d,-b], [-c,a]]

    if de == 0 :
        print("ero")
    else :
        mat = [[elem * de for elem in row] for row in mat]
    return mat


#change message and key into matrix
def changeToArr(key, passw):
    
    passArr = []
    keyArr= []
    lenghtOfPass = len(passw)
    lenghtOfKey = len(key)
    jump = int(sqrt(lenghtOfKey))

    #chane word and key into matrix
    for i in range(0, lenghtOfPass, jump):
        passArr.append([])
        for j in range(0, jump):
            passArr[int(i/jump)].append(alphabet.index(passw[i + j]))

    for i in range(0, lenghtOfKey, jump):
        keyArr.append([])
        for j in range(0, jump):
            keyArr[int(i/jump)].append(alphabet.index(key[i + j]))
        
    return [keyArr, passArr]



def encode(key, passW):
    global flag #to check if key has inverse on Z26
    keyArr, passArr = changeToArr(key,passW) 
    arr = []
    result = ""
    sizeP = len(passArr)
    if gcd(det(keyArr), 26) != 1:
        flag = False
        return 0

    for i in range(0, sizeP):
        test = muptiply(passArr[i], keyArr)
        sizeT = len(test)
        
        for j in range(0, sizeT):
            test[j] %= 26 
            arr.append(test[j])
    sizeR = len(arr)
    for i in range(0,sizeR ):
        result += alphabet[arr[i]]
    return result

def decode(code, key):
    keyArr, passArr = changeToArr(key, code)
    keyArr = inverse(keyArr)
    arr = []
    sizeP = len(passArr)
    result = ""
    
    
    for i in range(0, sizeP):
        test = muptiply(passArr[i], keyArr)
        sizeT = len(test)
        
        for j in range(0, sizeT):
            test[j] %= 26 
            arr.append(int(test[j]))

        
    sizeR = len(arr)

    for i in range(0,sizeR ):
        result += alphabet[arr[i]]

    return result

def main():
    ale = encode(key, passW)
    if flag:
        print("after encode:", ale)
        print("ogrrinal message:", decode(ale, key))
    else:
        print("Cannot encode and decode, please change your key")

main()