import random

def rand(start , end , num):
    ans = []
    for j in range(num):
        ans.append(random.randint(start , end))
    return ans

def printrange(list):
    range1 = 0
    range2 = 0
    range3 = 0
    range4 = 0
    for ele in list:
        if ele >= 101 and ele <= 125:
            range1 = range1 + 1
        elif ele >= 126 and ele <= 150:
            range2 = range2 + 1
        elif ele >= 151 and ele <= 175:
            range3 = range3 + 1
        elif ele >= 176 and ele <= 200:
            range4 = range4 + 1
    print("Range 101-125 : " , range1)
    print("Range 126-150 : " , range2)
    print("Range 151-175 : " , range3)
    print("Range 176-200 : " , range4)



num = 100
start = 101
end = 200
list = rand(start , end , num)
print(list)
printrange(list)