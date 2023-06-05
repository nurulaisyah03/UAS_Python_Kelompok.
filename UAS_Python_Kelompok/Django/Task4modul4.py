print("=======TASK 4-MODUL/Tema 5===========")
print("========SEDRI SELLA JUMENI=========")
#Percabangan
#1. pernyataan If
angka=10
if angka > 2:
    print(angka,"adalah bilangan posistif")
#2.pernyaan if else
bilangan=-2
if bilangan >=0:
    print("positif atau nol")
else :
    print("bilangan negatif")
#3. pernyataan if else if
bilangan=5.5
if bilangan >0:
    print ("bilangan positif")
elif bilangan ==0:
    print("nol")
else :
    print("bilangan negatif")
#4.if bersarang
print("===Contoh IF Bersarang===")
print("=========================")
gaji=10000000
berkeluarga=True
punyarumah=True
if gaji>3000000:
    print("gaji sudah diatas umr")
    if berkeluarga:
        print("wajib ikut asuransi dan menabung untuk pensiun")
    else:
        print("tidak perlu ikut asuransi")
    if punyarumah:
        print("wajib bayar pajak rumah")
    else:
        print("tidak wajib bayar pajak rumah")
else:
    print("gaji belum umr")

#perulangan 
print("===perulangan===")
nomor =[4,5,5,6,7]
jumlah=0
for tampung in nomor:
    jumlah=jumlah +tampung
print("jumlah semuanya :",jumlah)
#1. Perulangan for dengan range:digunakan untuk menghasilakan deret bilangan
for hitung in range(5):
    print("hitung :",hitung)
#2.perulangan menggunakan while
hitung=0
while (hitung<5):
    print("hitung:",hitung)
    hitung=hitung+2
#3.Program kelipatan bilangan Genap
i=0
n=int (input("masukan batas:"))
for i in range(n):
    if i%2==0:
        print("bilangan:",i)
    i=i+1
#latihan
print("===Latihan====")
n = int(input("Masukkan nilai n: "))

# Mencari banyaknya kelipatan bilangan genap dari 0 hingga n
count = 0
for i in range(n+1):
    if i % 2 == 0:
        count += 1

# Menampilkan kelipatan bilangan genap dan banyaknya jumlah
print("Kelipatan bilangan genap dari 0 hingga", n, "adalah:")
for i in range(0, (count * 2) + 1, 2):
    print(i, end=" ")
print("(", count, "bilangan)")

print("=====FUNGSI======")
print("==SEDRI SELLA JUMENI==")
#1. def function_name(parameters)
def dipanggil(nama):
    print("hallo,"+nama+".Apa kabarmu?")
    return nama #return bersifat opsional. Gunanya adalah untuk mengembalikan suatu nilai expression dari fungsi. 
#pemanggilan fungsi
dipanggil("Anna")
#2. Docstring
def dipanggil(nama):
    "contoh cetak keterangan"
    print("hallo,"+nama+".Gimana Kabarmu?")
    return nama
dipanggil("anna")
print(dipanggil.__doc__)

#program luas persegi panjang dengan Fungsi(statis)
def persegipanjang(panjang,lebar):
    luas=panjang *lebar
    print("Luasnya:",luas )
    return luas
print ("menghitung luas persegi panjang")
persegipanjang(4,6)
#program luas persegi panjang dengan Fungsi(dinamis)
def persegipanjang(panjang,lebar):
    luas=panjang *lebar
    print("Luasnya:",luas )
    return luas
print ("menghitung luas persegi panjang")
a=int(input("masukan nilai panjang:"))
b=int(input("Masukan nilai lebar :"))
persegipanjang(a,b)

print("LATIHAN")
print("menghitung luas persegi panjang & persegi")
def persegipanjang(panjang,lebar):
    luas=panjang *lebar
    print("Luasnya:",luas )
    return luas
print ("persegi panjang")
a=int(input("masukan  panjang:"))
b=int(input("Masukan lebar :"))
persegipanjang(a,b)
def persegi(sisi):
    luas=sisi *sisi
    print("Luasnya:",luas )
    return luas
print ("persegi ")
a=int(input("masukan sisi:"))
persegi(a)

