import tkinter as tk
from tkinter import messagebox
from superadmin import abrirVentanaSuperadmin

def validarUsuario(usuario, contraseña):
    with open('datos/usuarios.txt', 'r') as archivo:
        usuarios = archivo.readlines()

    for linea in usuarios:
        usr, con, rol = linea.strip().split(',')
        if usr == usuario and con == contraseña:
            return rol
    return None

def abrirVentanaLogin():
    def iniciarSesion():
        
            usuario = cajaUsuario.get()
            contraseña = cajaContraseña.get()
            rol = validarUsuario(usuario, contraseña)
            if rol == 'superadministrador':
                print("Bienvenido Super Administrador")
                ventanaLogin.withdraw()
                abrirVentanaSuperadmin()
            elif rol == 'administrador':
                print("Bienvenido Administrador")
            elif rol == 'Estudiante':
                print("Bienvenido Estudiante")
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    ventanaLogin = tk.Tk()
    ventanaLogin.title("Login")
    ventanaLogin.geometry("300x280")


    labelTitulo = tk.Label(ventanaLogin, text="Iniciar sesion", font=("Arial", 14))
    labelTitulo.grid(row=2, column=0,columnspan=2, pady=10, padx=30)

    labeUsuario = tk.Label(ventanaLogin, text="Usuario:")
    labeUsuario.grid(row=3, column=0, padx=30, pady=5)
    cajaUsuario = tk.Entry(ventanaLogin)
    cajaUsuario.grid(row=3, column=1, padx=30, pady=5)

    labeContraseña = tk.Label(ventanaLogin, text="Contraseña:")
    labeContraseña.grid(row=4, column=0, padx=30, pady=5)
    cajaContraseña = tk.Entry(ventanaLogin, show="*")
    cajaContraseña.grid(row=4, column=1, padx=30, pady=5)

    botonIniciarSesion = tk.Button(ventanaLogin, text="Iniciar sesion", width=12, height=2, command=iniciarSesion)
    botonIniciarSesion.grid(row=5, column=0, columnspan=2, pady=10)

    ventanaLogin.mainloop()
