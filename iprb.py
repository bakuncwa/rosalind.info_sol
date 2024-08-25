# IPRB: Mendel's First Law
# Given: Three positive integers k, m, and n, representing a population containing k + m + n organisms
# k individuals are homozygous dominant for a factor
# m are heterozygous
# n are homozygous recessive
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
# (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

def mendels_prb_law(k, m, n):
    # total no. of organisms
    total = k + m + n
    # total no. of combinations to pick organisms
    total_combo = total * (total - 1) 
    # AA x Aa x aa
    dominant_combo = (k * (k - 1)) + (2 * k * m) + (2 * k * n)
    # Aa x Aa 75% dominant phenotype return
    dominant_combo += (m * (m - 1) * 0.75)
    # Aa x aa 50% dominant phenotype return
    dominant_combo += (2* m * n * 0.5)
    # probability of dominant phenotype
    dominant_prb = dominant_combo / total_combo
    
    return dominant_prb

ros_f = open("C:/Users/ . . . /Downloads/rosalind_iprb.txt")
k, m, n = map(int, ros_f.readline().rstrip().rsplit())

print(mendels_prb_law(k, m, n))