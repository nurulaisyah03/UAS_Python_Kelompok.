print("========Modul 4=========")
print("===SEDRI SELLA JUMENI====")
print("==========================")
#Membuat Tuple
#membuat tuple kosong
tuple1=()
print(tuple1)
#tuple dengan satu elemen
tuple1=(1)
print(tuple1)
#tuple berisi integer
tuple1=(1,2,3)
print(tuple1)
#tuple bersarang
tuple1=("hello",[1,2,3],(4,5,6))
print(tuple1)
#Tuple biasa tidak menggunakan tanda()
tuple1=1,2,3
print(tuple1)
#memasukan anggota tuple ke variabel yang sesuaian
a,b,c=tuple1
print(a,b,c) 
print("===SEDRI SELLA JUMENI====")
print("==========================")
#Mengakses anggota tuple
tuple1=('p','y','t','h','o','n')
print(tuple1[0])
print(tuple1[1])
print(tuple1[-1])
print(tuple1[2])
print(tuple1[5])
#mengakses satu range anggota tuple dengan menggunakan operator titik dua ( : ).
tuple1=('p','r','o','g','r','a','m','m','i','n','g')
print(tuple1[:3])
print(tuple1[2:7])
print(tuple1[3:])
print("===SEDRI SELLA JUMENI====")
print("==========================")
#mengubah anggota tuple
tuple1=(2,3,4,[5,6])
#kita memang tidak bisa mengubah anggota tuple karena bila kita hilangkan komentar # akan muncul error
#tapi list di dalam tuple bisa dirubah
tuple1[3][0]=7
print(tuple1)
#tuple diganti secara keseluruhan dengan cara penugasan kembali
tuple1=('p','y','t','h','o','n')
print(tuple1)
#anggota tuple tidak dapat dihapus menggunakan perintah del,karena akan menghasilkan eror 
del tuple1
print("===SEDRI SELLA JUMENI====")
print("==========================")
#Menguji Keanggotaan Tuple
tuple1=(1,2,3,4,'a','b','c','d')
#menggunakan in
print(3 in tuple1)
print('2'in tuple1)
print('e' in tuple1)
print('k' not in tuple1)
print("===SEDRI SELLA JUMENI====")
print("==========================")
#iterasi pada tuple
nama=('Teknik','informatika')
for a in nama :
    print('Hai',a)

print("===SEDRI SELLA JUMENI====")
print("==========================")
#metode dan fungsi bawaan tuple
tuple1=('p','y','t','h','o','n','s','a','y','a')
print(tuple1.count('a'))
print(tuple1.index('n'))

print("===SEDRI SELLA JUMENI====")
print("==========================")
#Set
#Membuat set
#set integer
set_saya={1,2,3,4}
print(set_saya)
#set dengan menggunakan fungsi set()
set_saya=set([1,2,3,4])
print(set_saya)
#set data campuran
set_saya={1,2.0,"python",(3,4,5)}
print(set_saya)
#menghilangkan duplikasi
set_saya={1,2,2,3,3,3,4,4,4,4}
print(set_saya)
#membuat variable a dengan{}
a={}
print(type(a))

a=set()
print(type(a))

print("===SEDRI SELLA JUMENI====")
print("==========================")
#mengubah anggota set
#membuat set baru
set_saya={1,2,3,4}
print(set_saya)

#menambah satu anggota atau data baru
set_saya.add(5)
print(set_saya)
#menambahkan beberapa anggota
set_saya.update([4,5,6,7,8])
print(set_saya)
print("===SEDRI SELLA JUMENI====")
print("==========================")
#menghapus anggota set
#membuat set baru
set_saya={1,2,3,4,5,6}
print(set_saya)
#menghapus angka 2 dengan discard
set_saya.discard (2)
print(set_saya)
#menghapus angka 5 dengan remove
set_saya.remove (5)
print(set_saya)

#membuat set baru
set_saya=set("Hello dunia")
print(set_saya)
#pop anggota(menghapus)
print(set_saya.pop())
print(set_saya)
#mengosongkan set
set_saya.clear()
print(set_saya)

print("===SEDRI SELLA JUMENI====")
print("==========================")
#operasi gabungan(Union)
a={1,2,3,4,5}
b={6,7,8,9,10}
#gabungkan menggunakan operator |
print(a|b)
#menggunakan fungsi union()
a.union(b)
b.union(a)

print("===SEDRI SELLA JUMENI====")
print("==========================")
#Operasi Irisan 
#membuat set A dan B
a={1,2,3,4,5}
b={6,7,8,9,10}
#iris menggunakan opertor &
print(a&b)
#menggunakan intersection
a.intersection(b)
b.intersection(a)
#operator selisih
a={1,2,3,4,5}
b={6,7,8,9,10}
#menggunakan operator - pada a
print(a-b)
a.difference(b)
print(b-a)
b.difference(a)
print("===SEDRI SELLA JUMENI====")
print("==========================")
#Operasi Komplemen (Symmetric Difference)
a={1,2,3,4,5}
b={6,7,8,9,10}
#menggunakan operator ^ pada a
print(a^b)
a.symmetric_difference(b)
print(b^a)
b.symmetric_difference(a)
print("===SEDRI SELLA JUMENI====")
print("==========================")
#Dictionary
#membuat dictionary kosong
dict1={}
print(dict1)
#dictionary dengan kunci integer
dict1={1:'sepatu',2:'sandal'}
print(dict1)
#dictionary dengan kunci campuran
dict1={'warna':'merah',1:[2,3,4]}
print(dict1)
#membuat dictionari menggunakan fungsi dict()
dict1=dict([('1','sepatu'),('2','kaos')])
print(dict1)

dict1=dict(m=7,n=2,o=2)
print (dict1)
print("===SEDRI SELLA JUMENI====")
print("==========================")
#mengakses anggota Dictionary
dict_saya={'nama':'Jungkook','usia':25}
print(dict_saya['nama'])
print(dict_saya.get('usia'))
print(dict_saya.get('alamat'))
print("===SEDRI SELLA JUMENI====")
print("==========================")
#menguah angota dictionary
dict_saya={'nama':'Taehyung','usia':26}
#update nilai
dict_saya['usia']=20
print(dict_saya)
#menambah anggota
dict_saya['alamat']='Korea Selatan'
print(dict_saya)
#menghapus anggota dictionary
#membuat dictionary baru
dict_saya={1:1,2:4,3:9,4:16,5:25}
#menghapus anggota tertentu
print(dict_saya.pop(3))
#menghapus anggota secara acak
print(dict_saya.popitem())
print (dict_saya)
del dict_saya[2]
print(dict_saya)
#menghapus semua anggota
dict_saya.clear()
del dict_saya
