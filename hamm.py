# HAMM: Counting Point Mutations
# Given two strings 's' and 't' of equal length, the Hamming distance between 's' and 't',  denoted dH(s,t) is the number of corresponding symbols that differ in 's' and 't'
# Given: Two DNA strings 's' and 't' of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t)

def hamming_distance(s, t):
    dist = 0
    idx = 0
    while idx < len(s):
        if s[idx] != t[idx]:
            dist += 1
        idx +=1
    return dist

ros_f = open("/Users/gyalm/Downloads/rosalind_hamm.txt")
s = ros_f.readline().rstrip()
t = ros_f.readline().rstrip()
print(hamming_distance(s,t))