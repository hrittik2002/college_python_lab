# A7.Write a program to find all odd length palindromes from a list.

arr = ['121' , '22' , '43134' , '4334', 'abcba' , 'madam']

for i in arr:
    if(len(i)%2 != 0):
        if(i == i[::-1]):
            print(f"{i} is palindrome")