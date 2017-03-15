genome = input().lower()
norm = genome.count('g')+ genome.count('c')
print((norm/len(genome))*100)