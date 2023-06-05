print("=== PRAKTIKUM MODUL 3 ===")
#OUTPUT
print(1,2,3,4,5,6,7)
#Outputnya : 1 2 3 4 5 6 7
print (1,2,3,4,5, sep='*')
#outpunya: 1*2*3*4*5
print(1,2,3, sep='#', end='&')
#
print("===================================")

#OUTPUT 
print("=Output=")
a= input("Masukan Nilai a :")
b=input ("Masukan Nilai b :")

#contoh kode input integer tanpa Fungsi int()
c=a+b 
print (c)

#contoh kode input integer dengan Fungsi int cara pertama()
a= int(input("Masukan Nilai a :"))
b=int(input ("Masukan Nilai b :"))
c=a+b 
print (c)

#contoh kode input integer dengan Fungsi int cara kedua()
a= input("Masukan Nilai a :")
b=input ("Masukan Nilai b :")
c=int(a)+int(b) 
print (c)

#contoh kode input integer tanpa Fungsi float()untuk bilangan pecahan
a= input("Masukan Nilai a :")
b=input ("Masukan Nilai b :")
c=float(a)/float (b) 
print (c)

#Dengan menggunakan fungsi abs() kita bisa hilangkan tipe data yang ada minusnya
#Fungsi abs statis
a= -5
c= abs (a)
print (c)

#Fungsi abs Dinamis
a= int(input("masukan nilai a:"))
c=abs (a)
print(c)

#pow(). Adalah fungsi untuk menghitung pangkat.
#fungsi pow statis
c= pow (2,3)
print (c)
#fungsi pow dinamis
a=int(input("masukan nilai :"))
b=int(input("masukan nilai pangkat"))
c=pow(a,b)
print(c)
#sqrt(). Fungsi untuk mencari akar kuadrat dari suatu pangkat.
#Fungsi sqrt statis
import math
c=math.sqrt(36)
print(c)
#Fungsi sqrt Dinamis
import math
a=input ("masukan nilai:")
c=math.sqrt (int(a))
print(c)











