# A8.Write a recursive function to find HCF of two numbers. Use the function to find the LCM of set of numbers.

def hcf(a , b):
    if b == 0:
        return a
    else: return hcf(b , a%b)

def lcm(a , b):
    return (a * b) / hcf(a , b)


arr = [8 , 6 , 12 , 18]
sol = lcm(arr[0] , arr[1])
for i in range(2 , len(arr)):
    sol = lcm(sol , arr[i])
    
print(f"LCM = {sol}")
