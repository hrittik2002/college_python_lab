# A10. The program takes a string and counts the frequency of words appearing in that string using a dictionary.


sentence = input("Enter your sentence: ")
words = sentence.split()
dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else: dictionary.update({word : 1})

for key in dictionary:
    print("Frequency of" , key , "is" , dictionary[key])
