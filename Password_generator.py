import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title('Password Generator')
cwd = os.getcwd() # usar cwd evita errores al usar el script en otra pc con otra ruta
root.iconbitmap(f'{cwd}\\resources\\icono.ico') #icono de la aplicacion
root.geometry('400x600')

def put_placeholder():
    if not numero_caracteres.get().strip():
        numero_caracteres.delete(0, "end")
        numero_caracteres.insert(0, 'N° Caracteres')

def remove_placeholder(event):
    if numero_caracteres.get() == 'N° Caracteres':
        numero_caracteres.delete(0, "end")

def check_focus_out(event=None):
    if event.widget == root:
        put_placeholder()

def pass_generator():
    return

label_titulo = tk.Label(master=root, text='Genera tu contraseña segura', font=('Helvetica', 18, 'bold')).pack(padx=12, pady=5, expand=True, fill='both', anchor='n')
img = ImageTk.PhotoImage(Image.open(f'{cwd}\\resources\\seguro1.jpeg').resize((300,300)))
label_imagen = tk.Label(root, image=img).pack(padx=12, pady=5, expand=True, fill='both')

numero_caracteres = tk.Entry(root, width=20)
put_placeholder()
numero_caracteres.bind("<FocusIn>", remove_placeholder)
numero_caracteres.bind("<FocusOut>", put_placeholder)
#root.bind("<Button-1>", check_focus_out)
#root.bind("<Button-1>", lambda event: put_placeholder())
numero_caracteres.bind("<Leave>", put_placeholder) # Add this line
root.bind("<Button-1>", lambda event: put_placeholder() if not numero_caracteres.winfo_containing(event.x_root, event.y_root) else None)

numero_caracteres.pack(padx=160, pady=5, expand=True, fill='both')

checkbox_numeros = tk.BooleanVar(value=True)
checkbox_simbolos = tk.BooleanVar(value=True)
numeros = tk.Checkbutton(root, text='Incluir Números', variable=checkbox_numeros)
numeros.pack(padx=140, pady=20, expand=True, fill='both')
simbolos = tk.Checkbutton(root, text='Incluir Símbolos', variable=checkbox_simbolos)
simbolos.pack(padx=140, pady=20, expand=True, fill='both')
root.mainloop()