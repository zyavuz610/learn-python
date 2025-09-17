"""
Uygulama1: Dosya Birleştirme, dir-1 ve dir-2
"""

import os

dir1, dir2 = "dir-1", "dir-2"
file2 = os.path.join(dir2,"tr.txt")
file_list = sorted(os.listdir(dir1))

if os.path.exists(file2):
  os.remove(file2)

f2 = open(file2,"a")
for file in file_list:
  print(file)
  f1 = open(os.path.join(dir1,file))
  data = f1.read()
  f2.write(data+"\n")
  f1.close()
f2.close()










"""
Diğer Uygulamalar

Uygulama2: İki Şehir arasındaki uzaklık, dir-3
TR için iki paralel arası uzaklık: 111 km
iki meridyen arası uzaklık, 86km

Uygulama3: Toplu dosya isimlendirme, dir-4
  01_a.txt ...
  02_b.txt
  03_ch.txt ...

Uygulama4: verilen bir dizin içerisindeki dosya isimlerini liste halinde başka bir dosyaya yaz
  dir-5 içerisindeki dosyaların listesini dir-6 içerisndeki file-list.txt ye yaz

"""