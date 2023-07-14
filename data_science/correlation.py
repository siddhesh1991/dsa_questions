# COrrelation
import math

A = [15,12,8,8,7,7,7,6,5,3]
B = [10,25,17,11,13,17,20,13,9,15]
n = len(A)
muA = sum(A)/n
muB = sum(B)/n

diffA = list(map(lambda x: x - muA, A))
diffB = list(map(lambda x: x - muB, B))

stdA = math.sqrt(sum([d**2 for d in diffA])/n)
stdB = math.sqrt(sum([d**2 for d in diffB])/n)

cov = sum([i*j for i,j in zip(diffA,diffB)])/(n)
k = cov/(stdA*stdB)

print(k)