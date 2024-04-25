# FIB: Rabits and Recurrence Relations

# Given: Positive integers n <= 40 and k <= 5
# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation, every pair of reproduction-age 
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

def fibseq(n, k):
    if not n <= 2:
        return fibseq(n-1,k) + k * fibseq(n-2,k)
    elif n<=2:
        return 1
    
    
#ros_f = "C:/Users/ . . . /Downloads/rosalind_fib.txt"
#n, k = ros_f.readline().strip().split(" ")
print(fibseq(29, 3))
         