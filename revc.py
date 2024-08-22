# REVC: Complementing a Stand of DNA
# Given:  A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

def reverse_comp(seq):
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    DNA_strand = " "
    for nuc_base in seq[::-1]:
        comp[nuc_base] = comp.get(nuc_base, 0)
        DNA_strand += comp[nuc_base]
    return DNA_strand

ros_f = open("/Users/. . . /Downloads/rosalind_revc.txt")
seq = ros_f.readline().rstrip()
if ros_f.count > 1000:
    print("s must not be longer than 1000 bp.")
else:
    DNA_strand = reverse_comp(seq)
    print(DNA_strand)
