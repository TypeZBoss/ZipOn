import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Ensure output folder exists
os.makedirs("zipped", exist_ok=True)

root = tk.Tk()
root.geometry("600x500")
root.title("Zip")

status_label = tk.Label(root, text="")
status_label.grid(pady=10)

def zip_item():
    choice = messagebox.askquestion(
        "Zip What?",
        "Do you want to zip a FOLDER?\n\nYes = Folder\nNo = File"
    )

    if choice == "yes":
        path = filedialog.askdirectory()
    else:
        path = filedialog.askopenfilename()

    if not path:
        return

    try:
        base_name = os.path.basename(path.rstrip("/\\"))
        zip_path = os.path.join("zipped", base_name + ".zip")

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:

            if os.path.isfile(path):
                zipf.write(path, arcname=os.path.basename(path))

            else:
                for foldername, subfolders, filenames in os.walk(path):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, path)
                        zipf.write(file_path, arcname)

        status_label.config(text=f"Success! Created {base_name}.zip")

    except Exception as e:
        status_label.config(text=f"Error: {e}")

zip_btn = tk.Button(root, text="Zip File or Folder", command=zip_item)
zip_btn.grid(pady=10)

root.mainloop()