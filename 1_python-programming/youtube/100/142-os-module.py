"""
Python 142:
Klasör İşlemleri, os modülü
+ çalışma klasörü görüntüle
+ Klasör oluştur
+ Klasör sil
+ çalışma klasörü değiştir
- Klasör içeriğini listele
"""
import os
print(os.getcwd())
os.chdir("yavuz")
print(os.getcwd())
dosyalar = os.listdir()
for f in dosyalar:
  print(f)