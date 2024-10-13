def isPalindrome(n):
  s = str(n) # string dönüşüm
  return s == s[::-1]
  
def allPalindromes(n1,n2):
  for i in range(n1,n2):
    if isPalindrome(i):
      print(i)

# 0 1 1 2 3 5 8 13 21 ...
def fibonacci(n):
  n0,n1,i = 0,1,1 
  print(n0,n1,end=", ")
  while(i<n):
    n0,n1,i = n1,n0+n1,i+1
    print(n1,end=", ")
  print("") # alt satıra geçer

def divNum(n):
  d = 0
  for i in range(2,n):
    if (n%i == 0): # tam bölünüyorsa
      d = d+1
  return d

def isPrime(n):
  if divNum(n) ==0:
    return True
  else:
    return False

def allPrimes(n):
  for i in range(2,n+1):
    if isPrime(i):
      print(i)

# 6 -> 3,2,1=6
# 28 -> 14,7,4,2,1=28
def isPerfect(n):
  sum = 0
  for i in range(1,n):
    if (n%i==0):
      sum = sum+i
  return n == sum

def allPerfects(n):
  for i in range(1,n+1):
    if isPerfect(i):
      print(i)



tr_cities=["","Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]