# INI3: Strings and Lists

# Given: a string at most 200 letters and four integers a, b, c, d
# Return: slice of this string from indices a through b, c through d (space
# in between), inclusively. 
# s[b], s[d] in slice

def strSlice(s, a, b, c, d):
    return s[a:b+1], s[c:d+1]

ros_f = open("/Users/ . . . /Downloads/rosalind_ini3.txt")
s = ros_f.readline().rstrip()
a, b, c, d = map(int, ros_f.readline().rstrip().rsplit())
sp1, sp2 = strSlice(s, a, b, c, d)
print(sp1, sp2)
