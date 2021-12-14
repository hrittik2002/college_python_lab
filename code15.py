# A15. Write a Python Program to Count the Occurrences of a Word in a Text File.

text = open("MyText.txt" , "r")  # read the text
map = dict()
for line in text:
    line = line.strip()          # remove the leading space
    line = line.lower()          # convert everything to lower case
    words = line.split(" ")      # store every words of the line in a list

    # store frequency of each word in map
    for word in words:
        if word in map:
            map[word] = map[word] +  1
        else:
            map[word] = 1

for key in list(map.keys()):
    print(key , ":" , map[key])
text.close()


