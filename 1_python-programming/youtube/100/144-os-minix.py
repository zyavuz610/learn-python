"""
Python Mini Linux - py-minix
"""
import os

while(True):
  girdi = input("py-minix:\> ")
  if(girdi == "q"):
    break
  print("komut: ",girdi)
  girdi = girdi.split()
  if(girdi[0] == "pwd"):
    print(os.getcwd())
  if(girdi[0] == "ls"):
    lst = os.listdir()
    lst = sorted(lst)
    for e in lst:
      if not e.startswith("."):
        print(e)
  if (girdi[0] == "mkdir"):
    os.mkdir(girdi[1])
  if (girdi[0] == "cd"):
    os.chdir(girdi[1])
  if(girdi[0] == "cr"):
    f = open(girdi[1],"xt")
    f.close()
  if(girdi[0] == "sil"):
    os.remove(girdi[1])
  if(girdi[0] == "rename"):
    os.rename(girdi[1],girdi[2])
    

print("Güle güle!...")