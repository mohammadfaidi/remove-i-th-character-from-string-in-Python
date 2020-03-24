

def rmchar():
    oldstr = input ("Enter the word:")
    print("the orignal string:" + oldstr)
    pos = int (input ("Enter the position: "))
    newstr = ""
    for i in range (0, len(oldstr)):
        if i != pos:
            newstr = newstr +  oldstr[i]


    return newstr


while True:
    print("the new string:" + rmchar())











