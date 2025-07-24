import tkinter as tk
from tkinter import messagebox

def abrirVentanaSuperadmin():


    def abrirVentanaProfesor():
        ventanaProfesor = tk.Toplevel()
        ventanaProfesor.title("Registrar Profesor")
        ventanaProfesor.geometry("400x250")
        ventanaProfesor.resizable(False, False)

        titulo = tk.Label(ventanaProfesor, text="Registrar Profesor", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        labelUsuario = tk.Label(ventanaProfesor, text="Usuario:")
        labelUsuario.grid(row=1, column=0, padx=30, pady=5)
        cajaUsuario = tk.Entry(ventanaProfesor)
        cajaUsuario.grid(row=1, column=1, padx=30, pady=5)

        labelContraseña = tk.Label(ventanaProfesor, text="Contraseña:")
        labelContraseña.grid(row=2, column=0, padx=30, pady=5)
        cajaContraseña = tk.Entry(ventanaProfesor, show="*")
        cajaContraseña.grid(row=2, column=1, padx=30, pady=5)

        botonRegistrar = tk.Button(ventanaProfesor, text="Registrar")
        botonRegistrar.grid(row=3, column=0, columnspan=2, pady=15)

    def abrirVentanaEstudiante():
        ventanaEstudiante = tk.Toplevel()
        ventanaEstudiante.title("Registrar Estudiante")
        ventanaEstudiante.geometry("400x300")
        ventanaEstudiante.resizable(False, False)

        titulo = tk.Label(ventanaEstudiante, text="Registrar Estudiante", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        labelUsuario = tk.Label(ventanaEstudiante, text="Usuario:")
        labelUsuario.grid(row=1, column=0, padx=30, pady=5)
        cajaUsuario = tk.Entry(ventanaEstudiante)
        cajaUsuario.grid(row=1, column=1, padx=30, pady=5)

        labelContraseña = tk.Label(ventanaEstudiante, text="Contraseña:")
        labelContraseña.grid(row=2, column=0, padx=30, pady=5)
        cajaContraseña = tk.Entry(ventanaEstudiante, show="*")
        cajaContraseña.grid(row=2, column=1, padx=30, pady=5)

        labelIdentificacion = tk.Label(ventanaEstudiante, text="Identificación:")
        labelIdentificacion.grid(row=3, column=0, padx=30, pady=5)
        cajaIdentificacion = tk.Entry(ventanaEstudiante)
        cajaIdentificacion.grid(row=3, column=1, padx=30, pady=5)

        botonRegistrar = tk.Button(ventanaEstudiante, text="Registrar")
        botonRegistrar.grid(row=4, column=0, columnspan=2, pady=15)

    # --------- Ventana principal del Super Admin ---------
    ventanaSuperadmin = tk.Toplevel()
    ventanaSuperadmin.title("Ventana Super Administrador")
    ventanaSuperadmin.geometry("400x300")
    ventanaSuperadmin.resizable(False, False)

    labelTitulo = tk.Label(ventanaSuperadmin, text="Bienvenido Super Administrador", font=("Arial", 16))
    labelTitulo.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=30)

    labelTexto = tk.Label(ventanaSuperadmin, text="Registrar un usuario", font=("Arial", 12))
    labelTexto.grid(row=1, column=0, columnspan=2, pady=(0, 20), padx=30)

    botonProfesor = tk.Button(ventanaSuperadmin, text="Registrar Profesor", width=20, command=abrirVentanaProfesor)
    botonProfesor.grid(row=2, column=0, columnspan=2, pady=10, padx=30)

    botonEstudiante = tk.Button(ventanaSuperadmin, text="Registrar Estudiante", width=20, command=abrirVentanaEstudiante)
    botonEstudiante.grid(row=3, column=0, columnspan=2, pady=10, padx=30)
