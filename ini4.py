# INI4: Conditions and Loops
# Given: Two positive integers a and b (a<b<10000)
# Return: The sum of all odd integers from a through b, inclusively.

def odd_total(a, b):
    return sum([i for i in range(a, b) if i % 2 == 1])

ros_f = open("/Users/ . . /Downloads/rosalind_ini4.txt")
a, b = map(int, ros_f.readline().rstrip().rsplit())
print(odd_total(a, b))
