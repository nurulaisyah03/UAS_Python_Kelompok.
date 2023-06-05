print("=======MODUL/Tema/modul 8===========")
print("========SEDRI SELLA JUMENI========")
#Komponen - Komponen 
#1.ComboBox
import tkinter as tk
from tkinter import ttk

# membuat instance tkinter
root = tk.Tk()

# judul jendela
root.title("Operator Matematika")

# ukuran jendela
root.geometry("300x150")

# membuat label
label = ttk.Label(root, text="Pilih operator:")
label.pack(pady=10)

# membuat ComboBox dengan beberapa opsi operator
options = ["+", "-", "*", "/"]
combo_box = ttk.Combobox(root, values=options)
combo_box.pack()

# menentukan nilai default ComboBox
combo_box.current(0)

# fungsi untuk menampilkan hasil operasi
def calculate():
    operator = combo_box.get()
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = 0
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    
    result_label.config(text="Hasil: " + str(result))

# tombol untuk melakukan operasi
calculate_button = ttk.Button(root, text="Tampil", command=calculate)
calculate_button.pack(pady=10)

# label untuk menampilkan hasil operasi
result_label = ttk.Label(root, text="")
result_label.pack()

# menjalankan jendela
root.mainloop()

#2.Radio Buton
print("=======MODUL/Tema/modul 8===========")
print("========SEDRI SELLA JUMENI========")
import tkinter as tk
from tkinter import ttk

# membuat instance tkinter
root = tk.Tk()

# judul jendela
root.title("Pilihan Jurusan")

# ukuran jendela
root.geometry("300x150")

# membuat label
label = ttk.Label(root, text="Pilih jurusan:")
label.pack(pady=10)

# variabel untuk menyimpan pilihan jurusan
selected = tk.StringVar()

# membuat RadioButton dengan tiga opsi jurusan
radio_button1 = ttk.Radiobutton(root, text="Sistem Informasi", variable=selected, value="1")
radio_button1.pack()

radio_button2 = ttk.Radiobutton(root, text="Informatika", variable=selected, value="2")
radio_button2.pack()

radio_button3 = ttk.Radiobutton(root, text="Komputer Akuntansi", variable=selected, value="3")
radio_button3.pack()

# fungsi untuk menampilkan pilihan jurusan yang dipilih
def show_selected():
    label.config(text=" " + selected.get())

# tombol untuk menampilkan pilihan jurusan yang dipilih
show_button = ttk.Button(root, text="Tampil", command=show_selected)
show_button.pack(pady=10)

# label untuk menampilkan pilihan jurusan yang dipilih
label = ttk.Label(root, text="")
label.pack()

# menjalankan jendela
root.mainloop()

