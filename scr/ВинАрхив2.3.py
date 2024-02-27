import tkinter as tk
from tkinter import filedialog, Button
from tkinter.messagebox import showinfo
import zipfile, py7zr, tarfile
import threading

def unpack_zip():
    def _unpack_zip():
        file = filedialog.askopenfilename(filetypes=[('ZIP ФАЙЛ', '*.zip')])
        direct = filedialog.askdirectory(title="Выберите директорию для извлечения")
        if not file:
            return
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(direct)
        showinfo(title="Информация", message=f"Файл {file} был распакован успешно!")

    threading.Thread(target=_unpack_zip).start()

def pack_zip():
    def _pack_zip():
        files = filedialog.askopenfilenames()
        if not files:
            return
        zip_file = filedialog.asksaveasfilename(defaultextension='.zip', filetypes=[('ZIP ФАЙЛ', '*.zip')])
        if not zip_file:
            return
        with zipfile.ZipFile(zip_file, 'w') as zip_ref:
            for file in files:
                zip_ref.write(file)

    threading.Thread(target=_pack_zip).start()

def antivirus_zip():
    def _antivirus_zip():
        try:
            zip_file = filedialog.asksaveasfilename(defaultextension='.zip', filetypes=[('ZIP ФАЙЛ', '*.zip')])
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall()  
                zip_ref.testzip() 
            showinfo(title="Информация", message="Архив не содержит ошибок/повреждений")
        except zipfile.BadZipfile:
            showinfo(title="Информация", message="Архив поврежден или имеет неверный формат")

    threading.Thread(target=_antivirus_zip).start()

def unpack_7z():
    def _unpack_7z():
        file = filedialog.askopenfilename(filetypes=[('7Z ФАЙЛ', '*.7z')])
        direct = filedialog.askdirectory(title="Выберите директорию для извлечения")
        if not file:
            return
        with py7zr.SevenZipFile(file, mode='r') as archive:
            archive.extractall(direct)
        showinfo(title="Информация", message=f"Файл {file} был распакован успешно!")

    threading.Thread(target=_unpack_7z).start()

def pack_7z():
    def _pack_7z():
        files = filedialog.askopenfilenames()
        if not files:
            return
        zip_file = filedialog.asksaveasfilename(defaultextension='.7z', filetypes=[('7Z ФАЙЛ', '*.7z')])
        if not zip_file:
            return
        with py7zr.SevenZipFile(zip_file, mode='w') as archive:
            for file in files:
                archive.write(file)

    threading.Thread(target=_pack_7z).start()

def pack_rar():
    def _pack_rar():
        files = filedialog.askopenfilenames()
        if not files:
            return
        zip_file = filedialog.asksaveasfilename(defaultextension='.rar', filetypes=[('RAR ФАЙЛ', '*.rar')])
        if not zip_file:
            return
        with py7zr.SevenZipFile(zip_file, mode='w') as archive:
            for file in files:
                archive.write(file)

    threading.Thread(target=_pack_rar).start()

def unpack_rar():
    def _unpack_rar():
        file = filedialog.askopenfilename(filetypes=[('RAR ФАЙЛ', '*.rar')])
        direct = filedialog.askdirectory(title="Выберите директорию для извлечения")
        if not file:
            return
        with py7zr.SevenZipFile(file, mode='r') as archive:
            archive.extractall(direct)
        showinfo(title="Информация", message=f"Файл {file} был распакован успешно!")

    threading.Thread(target=_unpack_rar).start()

def about():
    def _about():
        zip_path = filedialog.askopenfilename(filetypes=[('ZIP ФАЙЛ', '*.zip')])
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            for file_name in file_list:
                showinfo(title="Информация", message=f"{file_name}")

    threading.Thread(target=_about).start()

def about_7z():
    def _about_7z():
        ar_path = filedialog.askopenfilename(filetypes=[('7Z ФАЙЛ', '*.7z')])
        with py7zr.SevenZipFile(ar_path, 'r') as archive_ref:
            file_list = archive_ref.getnames()
            for file_name in file_list:
                showinfo(title="Информация", message=f"{file_name}")

    threading.Thread(target=_about_7z).start()

def unpack_tar():
    def _unpack_tar():
        file = filedialog.askopenfilename(filetypes=[('TAR ФАЙЛ', '*.tar')])
        direct = filedialog.askdirectory(title="Выберите директорию для извлечения")
        if not file:
            return
        with tarfile.open(file, 'r') as tar:
            tar.extractall(direct)
        showinfo(title="Информация", message=f"Файл {file} был распакован успешно!")
    threading.Thread(target=_unpack_tar).start()
root = tk.Tk()
root.title("ВинАрхив")
root.iconbitmap('logo.ico')
root.resizable(width=False, height=False)
root["bg"] = "#0000ff"
lbl = tk.Label(root, text="Работа с ZIP архивом", bg="gray22", fg="white")
lbl.pack()
btn_unpack_zip = tk.Button(root, text="Распаковывать ZIP", command=unpack_zip)
btn_unpack_zip.pack()
btn_pack_zip = tk.Button(root, text="Упаковка ZIP", command=pack_zip)
btn_pack_zip.pack()
btn_about = tk.Button(root, text="Содержимое ZIP", command=about)
btn_about.pack()
btn_antivirus_zip = tk.Button(root, text="Проверить ZIP", command=antivirus_zip)
btn_antivirus_zip.pack()
lbl1 = tk.Label(root, text="Работа с 7Z архивом", bg="gray22", fg="white")
lbl1.pack()
btn_unpack_7z = tk.Button(root, text="Распаковывать 7Z", command=unpack_7z)
btn_unpack_7z.pack()
btn_pack_7z = tk.Button(root, text="Упаковка 7Z", command=pack_7z)
btn_pack_7z.pack()
btn_about_7z = tk.Button(root, text="Содержимое 7Z", command=about_7z)
btn_about_7z.pack()
lbl2 = tk.Label(root, text="Работа с 7Z архивом", bg="gray22", fg="white")
lbl2.pack()
btn_unpack_rar = tk.Button(root, text="Распаковывать RAR", command=unpack_rar)
btn_unpack_rar.pack()
btn_pack_rar = tk.Button(root, text="Упаковка RAR", command=pack_rar)
btn_pack_rar.pack()
lbl3 = tk.Label(root, text="Работа с TAR архивом", bg="gray22", fg="white")
lbl3.pack()
btn_unpack_tar = tk.Button(root, text="Распаковывать TAR", command=unpack_tar)
btn_unpack_tar.pack()


if __name__ == '__main__':
    root.mainloop()
