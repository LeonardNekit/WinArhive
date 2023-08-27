import tkinter as tk
from tkinter import filedialog
import zipfile
import py7zr

def unpack_zip():
    file = filedialog.askopenfilename(filetypes=[('ZIP ФАЙЛ', '*.zip')])
    if not file:
        return
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall()
def pack_zip():
    files = filedialog.askopenfilenames()
    if not files:
        return
    zip_file = filedialog.asksaveasfilename(defaultextension='.zip', filetypes=[('ZIP ФАЙЛ', '*.zip')])
    if not zip_file:
        return
    with zipfile.ZipFile(zip_file, 'w') as zip_ref:
        for file in files:
            zip_ref.write(file)
def unpack_7z():
    file = filedialog.askopenfilename(filetypes=[('7Z ФАЙЛ', '*.7z')])
    if not file:
        return
    with py7zr.SevenZipFile(file, mode='r') as archive:
        archive.extractall()
def pack_7z():
    files = filedialog.askopenfilenames()
    if not files:
        return
    zip_file = filedialog.asksaveasfilename(defaultextension='.7z', filetypes=[('7Z ФАЙЛ', '*.7z')])
    if not zip_file:
        return
    with py7zr.SevenZipFile(zip_file, mode='w') as archive:
        for file in files:
            archive.write(file) 
def pack_rar():
    files = filedialog.askopenfilenames()
    if not files:
        return
    zip_file = filedialog.asksaveasfilename(defaultextension='.7z', filetypes=[('RAR ФАЙЛ', '*.rar')])
    if not zip_file:
        return
    with py7zr.SevenZipFile(zip_file, mode='w') as archive:
        for file in files:
            archive.write(file)
def unpack_rar():
    file = filedialog.askopenfilename(filetypes=[('RAR ФАЙЛ', '*.rar')])
    if not file:
        return
    with py7zr.SevenZipFile(file, mode='r') as archive:
        archive.extractall()
root = tk.Tk()
root.title("WinArhife")
root.resizable(width=False, height=False)
root["bg"] = "gray22"
btn_unpack_zip = tk.Button(root, text="Распаковывать ZIP", command=unpack_zip)
btn_unpack_zip.pack()
btn_pack_zip = tk.Button(root, text="Упаковка ZIP", command=pack_zip)
btn_pack_zip.pack()
btn_unpack_7z = tk.Button(root, text="Распаковывать 7Z", command=unpack_7z)
btn_unpack_7z.pack()
btn_pack_7z = tk.Button(root, text="Упаковка 7Z", command=pack_7z)
btn_pack_7z.pack()
btn_pack_rar = tk.Button(root, text="Распаковывать RAR", command=unpack_rar)
btn_pack_rar.pack()
btn_pack_rar = tk.Button(root, text="Упаковка RAR", command=pack_rar)
btn_pack_rar.pack()
if __name__ == '__main__':
    root.mainloop()