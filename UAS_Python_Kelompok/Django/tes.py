##Perbandingan##
a=10
b=5

c= a < b
print(c)

c=a > b
print(c)

c= a==b
print(c)

c= a!=b
print(c)
print("===Operator Penugasan=====")
#Penugasan
print("=ontoh 1 ")
a= 12
b=2

a+=b
print(a)

a=12
b=2
a-=b
print(a)
print (" contoh 2")
x=5
x-=3 #x=x-3
print(x)

#Operator Logika
#1. Operatoe and
print("====Operator logika=====")
x=10
print(x>5 and x< 5)

#2. Operator or
a=True
b=False
print(a or b)

#Operator Not
c=True
d=not c 
print("not",c,"=",d)

#Operator bitwise
print ("===Operator bitwise==")
a=2
b=3

c=a|b 
print(c)

c=a & b 
print (c)

c=a^b 
print (c)

c=a<<b 
print(c)

c=a>>b 
print (c)

#Operator Identitas
print ("==Operator identitas==")
x="Pyhton"
y=20
z="Pyhton"

print (x is y )
print (x is z )

print (x is not y)
print (x is not z)

print(type(x) is str)
print (type(z) is int )

#Operator Keanggotaan 
print ("==Operator keanggotaan 1===")
kata=" hari ini belajar pyhton"
#1. Operator in
print ("hari" in kata )
print ("siang" in kata)
#2. Operator not in
print("belajar" not in kata)
print ("pyhton" not in kata)
print ("")
print ("==Operator keanggotaan 2===")
kata=5,6, "operasi"
#1. Operator in
print (5 in kata )
print (6 in kata)   
#2. Operator not in
print(6 not in kata)
print ("operasi" not in kata)



 