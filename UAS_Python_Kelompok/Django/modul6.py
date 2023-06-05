print("=======MODUL/Tema 6===========")
print("======SEDRI SELLA JUMENI======")
#Object Oriented Programming
#1. Perkenalan Kelas & Objec
#kelas:adalah cetak biru atau prototipe dari object dimana kita mendefinisikan atribut dari suatu object
class python :#penamaan kelas, diikuti dengan titik dua (:)
    pass #pass pada baris ke-3 artinya adalah pernyataan pass tidak melakukan apapun.
#object:adalah instansiasi atau perwujudan dari sebuah kelas. Bila kelas adalah prototipenya, dan objek adalah barang jadinya.
python1=python()#pembuatan object.
python2=python()#pembuatan object.
python3=python()#pembuatan object.

python1.name ="kelas D"
python1.mahasiswa="30"
python2.name ="kelas C"
python2.mahasiswa="31"
python3.name ="kelas B"
python3.mahasiswa="32"

#pemanggilan
print(python1)
print(python1.__doc__)
print(python1.name)#pemanggilan atribut. 
#2.Kelas dan object sederhana
class marvel:
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):# __init__() adalah metode konstruktor
        #untuk menginisialisasi pembuatan objek dari kelas tersebut.
        self.name=inputname #self digunakan untuk mengakses atribut. 
        self.health=inputhealth
        self.power=inputpower
        self.armor=inputarmor

marvel1=marvel("iron man",100,10,90)
marvel2=marvel("thor",90,15,100)
marvel3=marvel("captain america",80,5,70)
print(marvel1.name)
print(marvel2.health)
print(marvel3.__dict__)#pemanggilan atribut. 
#3.Variabel kelas dan object
class marvel: #class variabel
    jumlah=0
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):#instance variabel:
        self.name=inputname#variabel object
        self.health=inputhealth
        self.power=inputpower
        self.armor=inputarmor
        marvel.jumlah+=1
        print("hero marvel dengan nama :"+inputname)
marvel1=marvel('iron man',1000,900,800)
print(marvel.jumlah)
marvel2=marvel("thor",900,1000,900)
print(marvel.jumlah)
marvel3=marvel("captain america",800,700,600)
print(marvel.jumlah)
#4.Method
class marvel:
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):# __init__() adalah metode konstruktor
        #untuk menginisialisasi pembuatan objek dari kelas tersebut.
        self.name=inputname #self digunakan untuk mengakses atribut. 
        self.health=inputhealth
        self.power=inputpower
        self.armor=inputarmor
#void function method tanpa return
    def siapa(self):
        print("namaku adalah :"+self.name)
    #method dengan argumen
    def healthtambah(seft,tambah):
        self.health += tambah

    #method denga return
    def gethealth(self):
        return self.health

marvel1=marvel('iron man',1000,900,800)
marvel2=marvel("thor",900,1000,900)
marvel3=marvel("iron man",800,700,600)

#pemanggilan method
marvel1.siapa()
#pemakaian method dengan argumen
marvel1.healthtambah(10)
print(marvel1.health)
#mengembalikan nilai dengan method
print(marvel.gethealth())
#5.Game dengan OOP
class marvel:
    def __init__(self,name,health,attackpower,armornumber):
        self.name=name
        self.health=health
        self.attackpower=attackpower
        self.armornumber=armornumber
    def serang(self,lawan):
        print(self.name+"menyerang"+lawan.name )
        lawan.diserang(self,self.attackpower)
    def diserang (self,lawan,attackpower_lawan):
        print (self.name +"diserang"+lawan.name)
        attact_diterima=attackpower_lawan
        print("serangan terasa:"+str(attact_diterima))
        self.health-=attact_diterima
        print("Darah"+self.name+"tersisa"+str(self.health))
ironman=marvel("iron man",100,10,5)
thor=marvel("thor",95,15,10)
#ironman.serang()
ironman.serang(thor)




















