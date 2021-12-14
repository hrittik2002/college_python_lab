# A14. Write a function to generate a random alphanumeric string with 6 characters. There must be one uppercase, 
# one lower case, one digit in the string and all string should start with an uppercase letter.

# Call this function 50 times and find how many generated string starts with 'A'.
import secrets
import string
import random

list = []

def gena():
    size = 6
    N = 5
    ans = ""
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N))
    p = random.choice(string.ascii_uppercase)
    ans = p + res 
    print(ans)
    list.append(ans)

for i in range(50):
    gena()
c = 0
for ele in list:
    if ele[0] == 'A':
        c = c + 1
print(c)
