from itertools import permutations
s=input()
d=permutations(s)
for i in list(d):
  print("".join(i))
