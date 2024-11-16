"""

Problem 1: (128)
tp = (3,-1,4,3,6,-2,-5,-1)
max,min product, ardışıl 2 elemanın çarpımları arasında max ve min bul

"""

tp = (3,-1,4,3,6,-2,-5,-1)
lst = []

for i in range(len(tp)-1):
  m = tp[i] * tp[i+1]
  lst.append(m)

print(lst)
print("min:",min(lst))
print("max:",max(lst))