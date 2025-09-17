"""
Python 141:
Dosya İşlemleri, os modülü
+ dosya sil
+ dosya yeniden adlandır
+ dosya mı?
+ dosya mevcut mu?
+ dosya boyutu
"""
import os
"""
file = "dir/file1.txt"
if( os.path.exists(file) ):
  print(file," dosyası mevcut")
  os.remove(file)
else:
  print(file, " dosyası mevcu değil")

file2 = "dir/file2.txt"
file2_new = "dir/file1.txt"
os.rename(file2,file2_new)
"""
isfile = os.path.isfile("dir/dir2")
isfile = os.path.isfile("dir/file1.txt")
print(isfile, os.path.getsize("dir/file1.txt"))