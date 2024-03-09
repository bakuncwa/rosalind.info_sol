# INI6: Working with Dictionaries

# Given: A string 's' of length at most 10000 letters.
#Return: The number of occurrences of each word in 's', 
# where words are separated by spaces. Words are case-sensitive, 
# and the lines in the output can be in any order.

def wordCount(s):
    dictCount = {}
    for x in s.rsplit(" "):
        if not x in dictCount:
            dictCount[x] = dictCount.get(x,0) + 0
        dictCount[x] = dictCount.get(x,0) + 1
    return dictCount
    

try:
    ros_f = open("/Users/ . . . /Downloads/rosalind_ini6.txt")
    try:
        s = ros_f.readline().rstrip()
        if ros_f.count > 3000:
            print("s must not be longer than 3000 characters.")
    except:
        dictCount = wordCount(s)
        for k, v in dictCount.items():
            print(k,v)
except:
    print("File did not open correctly")