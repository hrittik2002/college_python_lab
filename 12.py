# A12. Take a list and select the largest sub list with out repeating numbers.
# Sample:
# Input: [2,4,5,2,4,5,7,8,9,10,4,8,6]
# Output:[2,4,5,7,8,9,10,6]





def longestSubarray(a , n):
    ans = []
    for ele in a:
        if ele in ans:
            continue
        else:
            ans.append(ele)
    return ans





n = int(input("Enter the length of input list: "))
arr = []
while(n > 0):
    arr.append(int(input()))
    n = n - 1

k = longestSubarray(arr , n)
print(k)
 