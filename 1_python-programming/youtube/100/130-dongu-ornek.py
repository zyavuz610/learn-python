"""
Problem 3 (130)

tp = (5,2,4,8,9)

min-max = 2,9
eksik sayılar: 3,6,7 ekrana yaz

------------------------
2:**
3:-
4:****
5:*****
6:-
7:-
8:********
9:*********
"""

def func(tp):
  lst = sorted(tp)

  print(lst)
  lst2 = []
  for k in range(lst[0],lst[-1]+1):
    if k in lst:
      print(k,":","*"*k,sep="")
    else:
      print(k,":","-",sep="")
      lst2.append(k)
  return lst2


tp = (5,2,4,8,9)
print("Olmayan Sayılar:",func(tp))
    



