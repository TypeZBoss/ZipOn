import zipfile
import tkinter
from tkinter import filedialog

def unzip_file():
    try:
        file = filedialog.askopenfilename(
            filetypes=[("ZIP files", "*.zip")]
        )
        
       
        if file:
            with zipfile.ZipFile(file, 'r') as zip_file:
                zip_file.extractall('extracted')
                success_label = tkinter.Label(root, text="Successful, check the 'extracted' folder")
                success_label.grid()
    except Exception as e:
        print(f"An error occurred: {e}")

root = tkinter.Tk()
root.geometry("600x500")
root.title("Unzip")

enter_btn = tkinter.Button(root, text="Browse and Unzip", command=unzip_file)
enter_btn.grid(padx=20, pady=20)

root.mainloop()
