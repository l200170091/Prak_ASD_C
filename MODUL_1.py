#No 1
def segitiga() :
    for i in range(5) :
        for j in range (i+1) :
            print("*",end=' ')
        print()
    return(i)
segitiga()

#No2
def kotak(a,b):
    for i in range(a):
        if i == 0 or i == a-1:
            print("*"*a)
        else :
            x = a- b
            print ("*"+" "*(a-2)+"*")
kotak(4,5)

#No3a
def jmlVokal(string):
    vkl = 0
    a = "Kartasura"
    for car in string.lower():
        if car in a:
            vkl += 1
    vokal = len(string)
    return(vokal,vkl)

#No3b
def jmlVokal2(string):
    vok = 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car not in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)

#No4
def rerata(b):
    sum = 0
    for i in b :
        sum += i
    return(sum/len(b))

#no5
from math import sqrt as sq
def apakahPrima(x):
    x = int(x)
    assert x >= 0
    primaKecil = [2,3,5,7,11]
    bukanPriKecil = [0,1,4,6,8,9,10]
    if x in primaKecil:
        return True
    elif x in bukanPriKecil:
        return False
    else:
        hasil=[]
        for i in range(2,int(sq(x))+1):
            if i in primaKecil:
                hasil.append(True)
                print (True)
            elif i in bukanPriKecil:
                hasil.append(False)
                print (False)
        #return hasil

apakahPrima(25)

#no6
for i in range(2,1000):
    if i > 1:
        for j in range (2, i):
            if(i % j) == 0:
                break
        else:
            print(i)

#no7
def faktorPrima(x) :
    a = []
    b = []
    hasil = 0
    bil = x
    prima =True
    for i in range(2,x):
        prima = True
        for u in range(2, i) :
            if i % u == 0 :
               prima = False
        if prima :
            a.append(i)
    idx = 0
    while bil > 1 :      
        try:
            if (bil%a[idx]) == 0 : 
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])
            else :
                idx = idx + 1
        except IndexError :
            break
    print (b)

#no8

a = input("h = ")
b = input("k = ")
def apa(a,b):
        if a in b:
            return True
        else :
            return False

#no9

for i in range(1,100):
    if(i % 3) == 0 and (i % 5) == 0 :
        i = "Python UMS"
    elif(i % 3) == 0:
        i = "Python"
    elif(i % 5) == 0:
        i = "UMS"
    print(i)

#no10
from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if (D < 0):
        print("Determinan negatif. Persamaan tidak mempunyai akar real.")
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)
        hasil = (x1,x2)
        return hasil

#no11
def apakahKabisat(t):
    b = int(t)
    if(t % 4) == 0:
        if(t % 100) == 0:
            if(t % 400) == 0:
                print("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")

#no12

r = random.randint(1,100)
a = """Permainan tebak angka.
Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba Tebak."""

print(a)

b = "Masukkan tebakan ke-"
f = ":> "
c = 1
d = str(c)

for i in range(1,100):
    e = (b+d+f)
    a = int(input(e))
    c+=1
    d = str(c)
    if(a < r):
        print("Itu terlalu kecil. Coba lagi.")
    elif(a > r):
        print("Itu terlalu besar. Coba lagi.")
    elif(a == r):
        print("Ya. Anda benar")
        break

#no13
def katakan(bil):
    angka = ["","Satu ","Dua ","Tiga ","Empat ","Lima ","Enam ",
             "Tujuh ","Delapan ","Sembilan ","Sepuluh ","Sebelas "]
    hasil = ""
    n = int(bil)
    if n >= 0 and n <= 11:

 
        hasil = angka[n]
    elif n < 20:
        hasil = katakan(n-10) + " Belas "
    elif n < 100:
        hasil = katakan(n/10) + " Puluh " + katakan(n%10)
    elif n < 200:
        hasil = " Seratus " + katakan(n-100)
    elif n < 1000:
        hasil = katakan(n/100) + " Ratus " + katakan(n%100)
    elif n < 2000:
        hasil = " Seribu " + katakan(n-1000)
    elif n < 1000000:
        hasil = katakan(n/1000) + " Ribu " + katakan(n%1000) 
    elif n < 1000000000:
        hasil = katakan(n/1000000) + " Juta " + katakan(n%1000000)
    elif n > 1000000000:
        hasil = 'Maaf, program tidak membaca angka lebih dari Satu Milyar'
    return hasil


a = 1
while a != 0:
    a = input(' Masukkan angka dari 1 sd 1.000.000.000: ')
    huruf = katakan(a)
    print(huruf +' Rupiah'

#no14
def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return "Rp " + x

