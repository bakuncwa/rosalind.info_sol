# DNA: Counting DNA Bases

# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
# the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') 
# is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that 
# the symbols 'A', 'C', 'G', and 'T' occur in s.

def dna_count(s):
    comp = {"A": 0, "C": 0, "G":0, "T": 0}
    for i in s:
        if not i in comp:
            comp[i] = comp.get(i, 0) + 0    
        comp[i] = comp.get(i, 0) + 1
    return comp

try:
    ros_f = open("/Users/ . . . /Downloads/rosalind_dna.txt")
    try:
        s = ros_f.readline().rstrip()
        if ros_f.count > 1000:
            print("s must not exceed 1000 nt.")
    except:
        print(dna_count(s))
except:
    "File did not open correctly."

    
        
        
        
