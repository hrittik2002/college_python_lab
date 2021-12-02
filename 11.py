# A11. Write function prime_factors() which takes a number as input and return its prime factors as output.
# Write a program which will take a list of integer as input and create a dictionary with number as key and its prime factor as list of integers. 
# sample:
# Input : 20, 25, 36
# output: {20:[2,5],25:[5],36:[2,3]}
import math

def primeFactor(n):
    ans = set()
    while  n % 2 == 0:
        ans.add(2)
        n = n / 2
    for i in range(3 , int(math.sqrt(n))+1 , 2):
        while n % i == 0:
            ans.add(int(i))
            n = n / i
    if n > 2:
        ans.add(int(n))
    return list(ans)

n = int(input("Enter the size of input array: "))
print("Enter the list of numbers")
arr = []
for i in range(0 , n):
    arr.append(int(input()))
ans = {}
for ele in arr:
    x = primeFactor(ele)
    ans[ele] = x;
print(ans)

