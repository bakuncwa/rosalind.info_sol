# PROT: Translating RNA into protein

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

def mRNA_to_amino_acid(mRNA_seq):
    rna_codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
        'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 
        'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W', 'CUU': 'L', 
        'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 
        'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 
        'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 
        'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 
        'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 
        'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 
        'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 
        'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 
        'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 
        'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 
        'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 
        'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    amino_acid_chain = ""

    for i in range(0, len(mRNA_seq), 3):
        extract_codon = lambda i: mRNA_seq[i:i+3]
        codon = extract_codon(i) 
        
        amino_acid = rna_codon_table.get(codon)
        
        if amino_acid.lower() == "stop":
            return amino_acid_chain
        
        amino_acid_chain += amino_acid
    
    return amino_acid_chain
        
ros_f = open("/Users/ . . . /Downloads/rosalind_prot.txt")
mRNA_seq = ros_f.readline().rstrip()
amino_acid_chain = mRNA_to_amino_acid(mRNA_seq)
print(amino_acid_chain)