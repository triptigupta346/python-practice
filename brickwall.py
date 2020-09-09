from collections import defaultdict

input = [[3,5,1,1],
         [2,3,3,2],
         [5,5],
         [4,4,2],
         [1,3,3,3],
         [1,1,6,1,1]]

seen =defaultdict(int)

for i in input:
    k=0
    for j in i[:-1]:
        k += j
        seen[k]+=1


print(len(input)-max(seen.values()))
print(seen)