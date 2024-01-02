# INI2: Variables and Some Arithmetic
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths 
# a and b.

import math

def hypoteneuse (a, b):
    if a <1000 and b <1000:  
        c_sq = pow(a, 2) + pow(b, 2)  
    return c_sq

ros_f = open("/Users/ . . /Downloads/rosalind_ini4.txt")
a, b = map(int, ros_f.readline().rstrip().rsplit())
print(hypoteneuse(a, b))

# print(hypoteneuse(904, 837))
# Ans: 34
