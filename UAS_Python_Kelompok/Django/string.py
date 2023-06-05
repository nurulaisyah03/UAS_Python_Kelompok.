#Operasi String
#len(). Berfungsi untuk mengembalikan panjang (jumlah anggota) dari suatu objek
string1="Hello pyhton"
print(len(string1))
#index(). Mencari posisi suatu nilai.
kata="Hallo pyhton"
print(kata.index("o"))
#count(). Menghitung kemunculan nilai tertentu.
#upper(). Mengubah string menjadi huruf kapital.
#lower(). Mengubah string menjadi huruf kecil.
#split(). Memisah string menjadi item
print("=========================")
kata="Hello pyhton"
print(kata.count("o"))
print (kata.upper())
print (kata.lower())
kata_baru=kata.split(" ")
print(kata_baru)
print("==Range slince==")
#Range Slice. 
#range Slice menampilkan range karakter dari a mendekati b (limit b), yang diformulasikan dengan.
kata="Halo semua"
print(kata[3:6])
print(kata[7])

print ("================LIST=====================")
#list kosong
list_ku=[]
#list berisi integer
list_ku=[1,2,3,4,5,6,7]
print(list_ku)
# list berisi tipe campuran
list_ku= [1, 3.5, "Hello"]
print(list_ku)
# list bersarang
list_ku = ["hello", [2,4,6], ['a','b']]
print(list_ku)

print("-----------------------------------------")
print("==SEDRI SELLA JUMENI==")
print("-----------------------------------------")

#List Dengan Indeks Negatif
my_list=['s','e','l','a','m','a','t']
print(my_list[-1])
print(my_list[-3])
print("-----------------------------------------")
print("==SEDRI SELLA JUMENI==")
print("-----------------------------------------")
#Memotong (Slicing) List
my_list=['s','e','l','a','m','a','t','d','a','t','a','n','g']
print(my_list[3:6])#artinya anggota list dari 3s/d 6
print (my_list[4:])
print(my_list[:5])

print("-----------------------------------------")
print("==SEDRI SELLA JUMENI==")
print("-----------------------------------------")
#Mengubah Anggota List
ganjil=[1,3,5,7,9]
print ("item awal :",ganjil)
#mengubah item ke 3 index ke 2
ganjil[2]=7
print (ganjil)
print("-----------------------------------------")
print("==SEDRI SELLA JUMENI==")
print("-----------------------------------------")
#Menambahkan Anggota List
ganjil=[1,3,5,7]
ganjil.append(9)
print(ganjil)

ganjil.extend([11,13,15])
print(ganjil)
#Menggabung list dengan operator
genap=[2,4,6]
print(genap+[8,10,12])

print("============================")
print("======SEDRI SELLA===========")
print("============================")
print(['p','y']*2)
# Menyisipkan Anggota List
ganjil=[5,7,11,13,15]
#menyisipkan angka 9 setelah angka 7
ganjil.insert(2,9)
print (ganjil)

print("============================")
print("======SEDRI SELLA===========")
print("============================")

#Menghapus anggota list
my_list=['p','y','t','h','o','n','k','u']
my_list.remove('p')
print(my_list)
#Remove hanya menghapus element pertama yang dijumpai
my_list=['p','y','t','h','o','n','k','u']
my_list.remove('k')

#output 'y'
print(my_list.pop(1))
del my_list[2]
print(my_list)

my_list.clear()
print(my_list)

print("============================")
print("======SEDRI SELLA===========")
print("============================")
#mengurutkan anggota list
alfabet=['a','b','c','d','e','f','g','h','i','j','k','l']
alfabet.sort()
print(alfabet)
#Membalik urutan list
alfabet.sort(reverse=True)
print(alfabet)






 
