# RNA: Transcribing DNA into RNA
# Given: A DNA string t having length at most 1000 nt
# Return: The transcribed RNA string of t

def rna_strand(seq):
    rna = {"A": "A", "T": "U", "C": "C", "G": "G"}
    DNA_strand = " "
    for nuc_base in seq:
        rna[nuc_base] = rna.get(nuc_base, 0)
        DNA_strand += rna[nuc_base]
    return DNA_strand


ros_f = open("C:/Users/ . . . /Downloads/rosalind_rna.txt")
seq = ros_f.readline().rstrip()
if ros_f.count > 1000:
    print("s must not be longer than 1000 nt.")
else:
    DNA_strand = rna_strand(seq)
    print(DNA_strand)
