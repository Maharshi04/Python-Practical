# ID : 20CE048
# Name : Maharshi Limbachiya

# AIM: You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. Sample Input: HackerRank.com presents "Pythonist 2".

# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

# github repository link : https://github.com/Maharshi04/Python-Practical/blob/main/Pract5.py

# 1st method to swap cases :
def swap_case(s):
    Output = ''
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower())
        elif(char.islower()==True):
            Output += (char.upper())
        else:
            Output += char
    return Output


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# 2nd method to swap cases :

# str=input()
# str2=str.swapcase()
# print(str2)