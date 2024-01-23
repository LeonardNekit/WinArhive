import tkinter as tk
from tkinter import filedialog, Button
from tkinter.messagebox import showinfo
import zipfile, py7zr
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
def antivirus_zip():
    try:
        zip_file = filedialog.asksaveasfilename(defaultextension='.zip', filetypes=[('ZIP ФАЙЛ', '*.zip')])
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall()  
            zip_ref.testzip() 
        showinfo(title="Информация", message="Архив не содержит ошибок/повреждений")
    except zipfile.BadZipfile:
        showinfo(title="Информация", message="Архив поврежден или имеет неверный формат")
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
    zip_file = filedialog.asksaveasfilename(defaultextension='.rar', filetypes=[('RAR ФАЙЛ', '*.rar')])
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
def about():
    zip_path = filedialog.askopenfilename(filetypes=[('ZIP ФАЙЛ', '*.zip')])
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        for file_name in file_list:
            showinfo(title="Информация", message=f"{file_name}")
def about_7z():
    ar_path = filedialog.askopenfilename(filetypes=[('7Z ФАЙЛ', '*.7z')])
    with py7zr.SevenZipFile(ar_path, 'r') as archive_ref:
        file_list = archive_ref.getnames()
        for file_name in file_list:
            showinfo(title="Информация", message=f"{file_name}")
root = tk.Tk()
root.title("ВинАрхив")
root.iconbitmap('logo.ico')
root.resizable(width=False, height=False)
root["bg"] = "gray22"
root.geometry("250x235")
btn_unpack_zip = tk.Button(root, text="Распаковывать ZIP", command=unpack_zip)
btn_unpack_zip.pack()
btn_pack_zip = tk.Button(root, text="Упаковка ZIP", command=pack_zip)
btn_pack_zip.pack()
btn_about = tk.Button(root, text="Содержимое ZIP", command=about)
btn_about.pack()
btn_antivirus_zip = tk.Button(root, text="Проверить ZIP", command=antivirus_zip)
btn_antivirus_zip.pack()
btn_unpack_7z = tk.Button(root, text="Распаковывать 7Z", command=unpack_7z)
btn_unpack_7z.pack()
btn_pack_7z = tk.Button(root, text="Упаковка 7Z", command=pack_7z)
btn_pack_7z.pack()
btn_about_7z = tk.Button(root, text="Содержимое 7Z", command=about_7z)
btn_about_7z.pack()
btn_unpack_rar = tk.Button(root, text="Распаковывать RAR", command=unpack_rar)
btn_unpack_rar.pack()
btn_pack_rar = tk.Button(root, text="Упаковка RAR", command=pack_rar)
btn_pack_rar.pack()
if __name__ == '__main__':
    root.mainloop()