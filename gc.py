# type: ignore

# GC: Computing GC content

# Given: At most 10 DNA string in FASTA format (of length at most 1 kbp each)
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; 
# please see the note on absolute error below.

def read_genome(filename):
    genome = {}
    with open(filename, "r") as f:
        label = ""
        for line in f:
            line = line.rstrip()
            if line[0] == ">":
                label = line[::1]
                genome[label] = ""
            else:
                genome[label] += line
    return genome

def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

def find_max_gc_content(filename):
    genome = read_genome(filename)
    max_gc_id = None
    max_gc_content = 0.0
    
    for seq_id in genome:
        max_gc_id = seq_id
        max_gc_content = gc_content(genome[seq_id])
        break
    
    for seq_id in genome:
        content = gc_content(genome[seq_id])
        if content > max_gc_content:
            max_gc_content = content
            max_gc_id = seq_id
    
    return max_gc_id, max_gc_content

filename = "/Users/gyalm/Downloads/rosalind_gc.txt"
max_gc_id, max_gc_content = find_max_gc_content(filename)

print(f"{max_gc_id}\n{max_gc_content:.6f}")