import math

def hypoteneuse (a, b):
    # a = int(input("a"))
    # b = int(input("b"))
    if a <1000 and b <1000:  
        c_sq = pow(a, 2) + pow(b, 2)
        # c = math.sqrt(c_sq)     
    return c_sq

print(hypoteneuse(904, 837))
# ans: 34