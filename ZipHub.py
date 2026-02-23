# main.py
import subprocess
import sys
import tkinter as tk
import os

os.makedirs("zipped", exist_ok=True)
os.makedirs("extracted", exist_ok=True)

root = tk.Tk()
root.title("ZipHub by redo_fly")
root.geometry('400x400')

def Zip():
    subprocess.run([sys.executable, 'zip.py'], capture_output=True, text=True) 
def UnZip():
    subprocess.run([sys.executable, 'unzip.py'], capture_output=True, text=True) 


zip_btn = tk.Button(root, text="Zip", command=Zip)
zip_btn.grid()

unzip = tk.Button(text="UnZip", command=UnZip)
unzip.grid()



root.mainloop()


