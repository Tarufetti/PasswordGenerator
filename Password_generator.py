import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import string
import random
import pyperclip

root = tk.Tk()
root.title('Password Generator')
cwd = os.getcwd() # usar cwd evita errores al usar el script en otra pc con otra ruta
root.iconbitmap(f'{cwd}\\resources\\icono.ico') #icono de la aplicacion
root.geometry('450x600')

def put_placeholder(event=None):
    if not numero_caracteres.get().strip():
        numero_caracteres.delete(0, "end")
        numero_caracteres.insert(0, 'N° Caracteres')
        submit.focus_set()

def remove_placeholder(event):
    if numero_caracteres.get() == 'N° Caracteres':
        numero_caracteres.delete(0, "end")

def pass_generator():
    global boton_copiar
    global label_copiar
    global contrasena
    if numero_caracteres == '' or numero_caracteres.get().isdigit() == False or int(numero_caracteres.get()) < 6 or int(numero_caracteres.get()) > 32:
        messagebox.showerror(title='Error', message='Ingrese un numero entre 6 y 32')
    else:
        minus = string.ascii_lowercase
        mayus = string.ascii_uppercase
        num = string.digits
        simbolos = '!?.,#$='
        todo = minus + mayus
        if checkbox_simbolos.get():
            todo += simbolos
        while True:
            if checkbox_numeros.get() and checkbox_simbolos.get():
                todo += num + simbolos
                contrasena = ''.join(random.choices(todo, k=int(numero_caracteres.get())))
                if any(s in simbolos for s in contrasena) and any(n.isdigit() for n in contrasena):
                    break
            elif checkbox_numeros.get():
                todo += num
                contrasena = ''.join(random.choices(todo, k=int(numero_caracteres.get())))
                if any(n.isdigit() for n in contrasena):
                    break
            elif checkbox_simbolos.get():
                todo += simbolos
                contrasena = ''.join(random.choices(todo, k=int(numero_caracteres.get())))
                if any(s in simbolos for s in contrasena):
                    break
            else:
                contrasena = ''.join(random.choices(todo, k=int(numero_caracteres.get())))
                break

        label_titulo.config(text='Tu contraseña segura es:')
        label_imagen.config(image='',text=f'{contrasena}', font=('Helvetica', 14, 'bold'), pady=90)
        if boton_copiar:
            boton_copiar.destroy()
        if label_copiar:
            label_copiar.destroy()
        boton_copiar = tk.Button(root, width=20, text='Copiar contraseña',font=('Helvetica', 12), bg='grey',fg='white', command=copiar)
        boton_copiar.pack(after=label_imagen, padx=100, pady=20, expand=True, fill='both')
def copiar():
    global label_copiar
    if label_copiar:
        label_copiar.destroy()
    pyperclip.copy(contrasena)
    label_copiar = tk.Label(root, width=40, text='Contraseña copiada al portapapeles', font=('Helvetica', 8))
    label_copiar.pack(before=boton_copiar, padx=80)


label_titulo = tk.Label(master=root, text='Genera tu contraseña segura', font=('Helvetica', 18, 'bold'))
label_titulo.pack(padx=12, pady=5, expand=True, fill='both', anchor='n')
img = ImageTk.PhotoImage(Image.open(f'{cwd}\\resources\\seguro1.jpeg').resize((300,300)))
label_imagen = tk.Label(root, image=img)
label_imagen.pack(padx=12, pady=5, expand=True, fill='both')
label_copiar = None
boton_copiar = None
contrasena = None

numero_caracteres = tk.Entry(root, width=20)
numero_caracteres.bind("<FocusIn>", remove_placeholder)
numero_caracteres.bind("<FocusOut>", put_placeholder)
numero_caracteres.bind("<Leave>", put_placeholder)
root.bind("<Button-1>", lambda event: put_placeholder() if not numero_caracteres.winfo_containing(event.x_root, event.y_root) else None)

numero_caracteres.pack(padx=160, pady=5, expand=True, fill='both')

checkbox_numeros = tk.BooleanVar(value=True)
checkbox_simbolos = tk.BooleanVar(value=True)
numeros = tk.Checkbutton(root, text='Incluir Números', variable=checkbox_numeros)
numeros.pack(padx=140, pady=20, expand=True, fill='both')
simbolos = tk.Checkbutton(root, text='Incluir Símbolos', variable=checkbox_simbolos)
simbolos.pack(padx=140, pady=20, expand=True, fill='both')

submit = tk.Button(root, width=20, text='Generar Contraseña', font=('Helvetica', 12), command=pass_generator)
submit.pack(padx=100, pady=5, expand=True, fill='both')
put_placeholder()

root.mainloop()