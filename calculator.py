from tkinter import *
import tkinter.font as font
import math

# Inisialisasi aplikasi
root = Tk()
root.title("Calculator")
root.geometry("310x450")
root["bg"] = "#2e2e2e"  # Warna background dark
myfont = font.Font(size=15)

# Entry untuk input
e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# List untuk menyimpan sejarah operasi dan stack untuk Undo
history = []
undo_stack = []

# Fungsi untuk memasukkan angka
def angka(nilai):
    sebelum = e.get()
    e.delete(0, END)
    e.insert(0, str(sebelum) + str(nilai))
    undo_stack.append(('angka', nilai))

# Fungsi operasi dasar
def tambah():
    global n_awal, math
    n_awal = float(e.get())
    math = "penjumlahan"
    e.delete(0, END)
    undo_stack.append(('operasi', 'penjumlahan', n_awal))

def kurang():
    global n_awal, math
    n_awal = float(e.get())
    math = "pengurangan"
    e.delete(0, END)
    undo_stack.append(('operasi', 'pengurangan', n_awal))

def kali():
    global n_awal, math
    n_awal = float(e.get())
    math = "perkalian"
    e.delete(0, END)
    undo_stack.append(('operasi', 'perkalian', n_awal))

def bagi():
    global n_awal, math
    n_awal = float(e.get())
    math = "pembagian"
    e.delete(0, END)
    undo_stack.append(('operasi', 'pembagian', n_awal))

def akar():
    n_awal = float(e.get())
    e.delete(0, END)
    e.insert(0, math.sqrt(n_awal))
    history.append(f"√{n_awal} = {math.sqrt(n_awal)}")
    undo_stack.append(('akar', n_awal))

def sisabagi():
    global n_awal, math
    n_awal = float(e.get())
    math = "sisabagi"
    e.delete(0, END)
    undo_stack.append(('operasi', 'sisabagi', n_awal))

def pangkat():
    n_awal = float(e.get())
    e.delete(0, END)
    e.insert(0, n_awal ** 2)
    history.append(f"{n_awal}^2 = {n_awal ** 2}")
    undo_stack.append(('pangkat', n_awal))

def hapus():
    e.delete(0, END)

def samadengan():
    nomor_akhir = e.get()
    e.delete(0, END)
    try:
        if math == "penjumlahan":
            result = n_awal + float(nomor_akhir)
        elif math == "pengurangan":
            result = n_awal - float(nomor_akhir)
        elif math == "perkalian":
            result = n_awal * float(nomor_akhir)
        elif math == "pembagian":
            result = n_awal / float(nomor_akhir)
        elif math == "sisabagi":
            result = n_awal % float(nomor_akhir)

        e.insert(0, result)
        history.append(f"{n_awal} {math} {nomor_akhir} = {result}")
        undo_stack.append(('hasil', result))
    except ZeroDivisionError:
        e.insert(0, 'infinity')

# Fitur sejarah
def tampilkan_sejarah():
    history_window = Toplevel(root)
    history_window.title("Sejarah")
    history_window.geometry("300x300")
    
    history_display = Listbox(history_window, selectmode=SINGLE)
    history_display.pack(expand=True, fill='both')
    
    for entry in history:
        history_display.insert(END, entry)

    def edit_entry():
        selected_index = history_display.curselection()
        if selected_index:
            selected_entry = history_display.get(selected_index)
            history_display.delete(selected_index)
            e.delete(0, END)
            e.insert(0, selected_entry.split('=')[0].strip())

    edit_button = Button(history_window, text="Edit", command=edit_entry)
    edit_button.pack(pady=5)

# Fungsi Pembulatan
def pembulatan():
    try:
        value = float(e.get())
        e.delete(0, END)
        e.insert(0, round(value))
        undo_stack.append(('pembulatan', value))
    except ValueError:
        e.insert(0, "Error")

# Fungsi Undo
def undo():
    if undo_stack:
        action = undo_stack.pop()
        if action[0] == 'angka':
            # Jika angka dimasukkan, hapus angka terakhir dari Entry
            current = e.get()
            e.delete(0, END)
            e.insert(0, current[:-1])
        elif action[0] == 'operasi':
            # Jika operasi, kembali ke nilai awal
            e.delete(0, END)
            e.insert(0, n_awal)
        elif action[0] == 'hasil':
            # Kembali ke nilai sebelum hasil
            e.delete(0, END)
            e.insert(0, '')

# Tombol dan grid
btn1 = Button(root, text="1", padx=30, pady=20, command=lambda: angka(1))
btn2 = Button(root, text="2", padx=30, pady=20, command=lambda: angka(2))
btn3 = Button(root, text="3", padx=30, pady=20, command=lambda: angka(3))
btn4 = Button(root, text="4", padx=30, pady=20, command=lambda: angka(4))
btn5 = Button(root, text="5", padx=30, pady=20, command=lambda: angka(5))
btn6 = Button(root, text="6", padx=30, pady=20, command=lambda: angka(6))
btn7 = Button(root, text="7", padx=30, pady=20, command=lambda: angka(7))
btn8 = Button(root, text="8", padx=30, pady=20, command=lambda: angka(8))
btn9 = Button(root, text="9", padx=30, pady=20, command=lambda: angka(9))
btn0 = Button(root, text="0", padx=30, pady=20, command=lambda: angka(0))
tam = Button(root, text="+", padx=30, pady=20, command=tambah)
kur = Button(root, text="-", padx=30, pady=20, command=kurang)
kal = Button(root, text="x", padx=30, pady=20, command=kali)
bag = Button(root, text="/", padx=30, pady=20, command=bagi)
ak2 = Button(root, text="√", padx=30, pady=20, command=akar)
sisa = Button(root, text="%", padx=20, pady=20, command=sisabagi)
pang = Button(root, text="^", padx=30, pady=20, command=pangkat)
hap = Button(root, text="C", padx=30, pady=20, command=hapus)
sama = Button(root, text="=", padx=50, pady=20, command=samadengan)
history_btn = Button(root, text="History", padx=30, pady=20, command=tampilkan_sejarah)
undo_btn = Button(root, text="Undo", padx=30, pady=20, command=undo)
round_btn = Button(root, text="Round", padx=30, pady=20, command=pembulatan)

# Menempatkan tombol di grid
btn1.grid(row=3, column=0, pady=2)
btn2.grid(row=3, column=1, pady=2)
btn3.grid(row=3, column=2, pady=2)
btn4.grid(row=2, column=0, pady=2)
btn5.grid(row=2, column=1, pady=2)
btn6.grid(row=2, column=2, pady=2)
btn7.grid(row=1, column=0, pady=2)
btn8.grid(row=1, column=1, pady=2)
btn9.grid(row=1, column=2, pady=2)
btn0.grid(row=4, column=1, pady=2)

tam.grid(row=1, column=3, pady=2)
kur.grid(row=2, column=3, pady=2)
kal.grid(row=3, column=3, pady=2)
bag.grid(row=4, column=3, pady=2)
hap.grid(row=4, column=0, pady=2)
sama.grid(row=5, column=2, pady=2, columnspan=2)
ak2.grid(row=5, column=0, pady=2)
sisa.grid(row=4, column=2, pady=2)
pang.grid(row=5, column=1, pady=2)
history_btn.grid(row=6, column=0, pady=2)
undo_btn.grid(row=6, column=1, pady=2)
round_btn.grid(row=6, column=2, pady=2)

# Fungsi untuk menangani keyboard shortcuts
def keyboard_shortcuts(event):
    if event.char.isdigit():
        angka(event.char)
    elif event.char == '+':
        tambah()
    elif event.char == '-':
        kurang()
    elif event.char == '*':
        kali()
    elif event.char == '/':
        bagi()
    elif event.char == '=' or event.char == '\r':
        samadengan()
    elif event.char == 'c':
        hapus()
    elif event.char == 'h':
        tampilkan_sejarah()
    elif event.char == 'u':
        undo()
    elif event.char == 'r':
        pembulatan()

root.bind("<Key>", keyboard_shortcuts)

root.mainloop()