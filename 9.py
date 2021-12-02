# A9. Python program to Sort a List of Tuples in Increasing Order by the Second element in Each Tuple.
#
# Input:
# list of tuples: (2,30,6),(10,6,9)(20,25,40,100)
#
# Output:
# List of tuples: (10,6,9),(20,25,40,100),(2,30,6)
#
# Explanation:
# 2nd elements are 30,6,25 in output. If we arrange them in ascending order it will be 6,25,30


def sort_tuple(tup):
    tup.sort(key = lambda x : x[1])
    return tup


tup = []
n = int(input("Enter the no of touple: "))
while(n > 0):
    l = int(input("Enter the length of touple: "))
    list = []
    while(l > 0):
        l = l - 1
        x = int(input())
        list.append(x)
    
    tup.append(tuple(list))
    n = n - 1
    
# tup = [(2,30,6),(10,6,9),(20,25,40,100)]
print(tup)
print(sort_tuple(tup))