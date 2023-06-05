print("=======MODUL/Tema 7===========")
print("======SEDRI SELLA JUMENI======")
#Tkinter
#tampilan gui sederhana
import tkinter as tk
window=tk.Tk ()

window.mainloop()

import tkinter as tk
#aplikasi aritmatika

class AdditionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplikasi Aritmatika Pertambahan")

        self.num1_label = tk.Label(self.root, text="Masukkan angka pertama:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(self.root, text="Masukkan angka kedua:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.add_button = tk.Button(self.root, text="Tambahkan", command=self.addition)
        self.add_button.pack()

        self.quit_button = tk.Button(self.root, text="Keluar", command=self.root.quit)
        self.quit_button.pack()

    def addition(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = num1 + num2
            self.result_label.config(text="Hasil: " + str(result))
        except ValueError:
            self.result_label.config(text="Input salah. Masukkan angka.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AdditionApp()
    app.run()

#aplikasi aritmatika disetakan menu menunya

import tkinter as tk

class AdditionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplikasi Aritmatika Pertambahan")

        # menu bar
        self.menu_bar = tk.Menu(self.root)

        # file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Keluar", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Tentang", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        # widgets
        self.num1_label = tk.Label(self.root, text="Masukkan angka pertama:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(self.root, text="Masukkan angka kedua:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.add_button = tk.Button(self.root, text="Tambahkan", command=self.addition)
        self.add_button.pack()

        self.quit_button = tk.Button(self.root, text="Keluar", command=self.root.quit)
        self.quit_button.pack()

    def addition(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = num1 + num2
            self.result_label.config(text="Hasil: " + str(result))
        except ValueError:
            self.result_label.config(text="Input salah. Masukkan angka.")

    def show_about(self):
        about_text = "Aplikasi Aritmatika Pertambahan\n\nDibuat oleh John Doe"
        tk.messagebox.showinfo("Tentang", about_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AdditionApp()
    app.run()

#Latihan
import tkinter as tk

class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kalkulator")

        # menu bar
        self.menu_bar = tk.Menu(self.root)

        # file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Keluar", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Tentang", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        # widgets
        self.num1_label = tk.Label(self.root, text="Masukkan angka pertama:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(self.root, text="Masukkan angka kedua:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        self.operation_var = tk.StringVar(self.root, value="+")
        self.operation_label = tk.Label(self.root, text="Operasi:")
        self.operation_label.pack()
        self.add_radio_button = tk.Radiobutton(self.root, text="Tambah", variable=self.operation_var, value="+")
        self.add_radio_button.pack()
        self.subtract_radio_button = tk.Radiobutton(self.root, text="Kurang", variable=self.operation_var, value="-")
        self.subtract_radio_button.pack()
        self.multiply_radio_button = tk.Radiobutton(self.root, text="Kali", variable=self.operation_var, value="*")
        self.multiply_radio_button.pack()
        self.divide_radio_button = tk.Radiobutton(self.root, text="Bagi", variable=self.operation_var, value="/")
        self.divide_radio_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.calculate_button = tk.Button(self.root, text="Hitung", command=self.calculate)
        self.calculate_button.pack()

        self.quit_button = tk.Button(self.root, text="Keluar", command=self.root.quit)
        self.quit_button.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            self.result_label.config(text="Hasil: " + str(result))
        except ValueError:
            self.result_label.config(text="Input salah. Masukkan angka.")
        except ZeroDivisionError:
            self.result_label.config(text="Tidak dapat dibagi dengan nol.")

    def show_about(self):
        about_text = "Kalkulator"
        tk.messagebox.showinfo("Tentang", about_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
