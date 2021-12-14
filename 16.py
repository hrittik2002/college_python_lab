# A16. Write a Python Program which will store selected content of an existing file to a new file.

# Existing file:[Id-marks1-marks2-marks3-marks4-marks5]
# 110011 89 67 75 90 56
# 110101 78 88 50 92 72
# 110102 60 70 56 91 51
# 110201 77 88 60 71 67
# 110202 55 61 71 62 73

# New file will contain the lines with average marks more than 65.

data = open("ReadText.txt" , "r")
store = open("WriteText.txt" , "w")

for line in data:
    line = line.strip()
    information = line.split(" ")
    
    # calculate average
    s = 0
    for i in range(1 , len(information)):
        s = s + int(information[i])
    avg = s / (len(information) - 1)

    if avg > 65:
        store.write(line + "\n")
    
data.close()
store.close()



    

