
def InclusionExclusion(m,n,prime):
    count = 0
    for i in range (1, m + 1):
        for j in range (0, n):
            if (i % prime[j] == 0):
                count+=1
                break
    
    return count
        