import tkinter as tk
from tkinter import messagebox

def abrirVentanaSuperadmin():


    def abrirVentanaProfesor():
        ventanaProfesor = tk.Toplevel()
        ventanaProfesor.title("Registrar Profesor")
        ventanaProfesor.geometry("500x300")
        ventanaProfesor.resizable(False, False)

        titulo = tk.Label(ventanaProfesor, text="Registrar Profesor", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        labelUsuario = tk.Label(ventanaProfesor, text="Documento de Identidad:")
        labelUsuario.grid(row=1, column=0, padx=30, pady=5)
        cajaUsuario = tk.Entry(ventanaProfesor)
        cajaUsuario.grid(row=1, column=1, padx=30, pady=5)

        labelNombre = tk.Label(ventanaProfesor, text="Nombre Completo:")
        labelNombre.grid(row=2, column=0, padx=30, pady=5)
        cajaNombre = tk.Entry(ventanaProfesor)
        cajaNombre.grid(row=2, column=1, padx=30, pady=5)

        labelContraseña = tk.Label(ventanaProfesor, text="Contraseña:")
        labelContraseña.grid(row=3, column=0, padx=30, pady=5)
        cajaContraseña = tk.Entry(ventanaProfesor, show="*")
        cajaContraseña.grid(row=3, column=1, padx=30, pady=5)

        botonRegistrar = tk.Button(ventanaProfesor, text="Registrar", command=lambda: registrar_profesor())
        botonRegistrar.grid(row=4, column=0, columnspan=2, pady=15)

        def registrar_profesor():
            usuario = cajaUsuario.get().strip()
            contraseña = cajaContraseña.get().strip()
            nombre_completo = cajaNombre.get().strip()
            valido, mensaje = verificar_datos_usuario(usuario, contraseña, nombre_completo, rol='profesor')
            if not valido:
                messagebox.showerror("Error de validación", mensaje)
                return
            registrar_usuario(usuario, contraseña, nombre_completo, 'profesor')
            messagebox.showinfo("Éxito", "Profesor registrado correctamente.")
            ventanaProfesor.destroy()

    def abrirVentanaEstudiante():
        ventanaEstudiante = tk.Toplevel()
        ventanaEstudiante.title("Registrar Estudiante")
        ventanaEstudiante.geometry("500x300")
        ventanaEstudiante.resizable(False, False)

        titulo = tk.Label(ventanaEstudiante, text="Registrar Estudiante", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        labelUsuario = tk.Label(ventanaEstudiante, text="Documento de Identidad:")
        labelUsuario.grid(row=1, column=0, padx=30, pady=5)
        cajaUsuario = tk.Entry(ventanaEstudiante)
        cajaUsuario.grid(row=1, column=1, padx=30, pady=5)

        labelNombre = tk.Label(ventanaEstudiante, text="Nombre Completo:")
        labelNombre.grid(row=2, column=0, padx=30, pady=5)
        cajaNombre = tk.Entry(ventanaEstudiante)
        cajaNombre.grid(row=2, column=1, padx=30, pady=5)

        labelContraseña = tk.Label(ventanaEstudiante, text="Contraseña:")
        labelContraseña.grid(row=3, column=0, padx=30, pady=5)
        cajaContraseña = tk.Entry(ventanaEstudiante, show="*")
        cajaContraseña.grid(row=3, column=1, padx=30, pady=5)

        botonRegistrar = tk.Button(ventanaEstudiante, text="Registrar", command=lambda: registrar_estudiante())
        botonRegistrar.grid(row=4, column=0, columnspan=2, pady=15)

        def registrar_estudiante():
            usuario = cajaUsuario.get().strip()
            contraseña = cajaContraseña.get().strip()
            nombre_completo = cajaNombre.get().strip()
            valido, mensaje = verificar_datos_usuario(usuario, contraseña, nombre_completo, rol='estudiante')
            if not valido:
                messagebox.showerror("Error de validación", mensaje)
                return
            registrar_usuario(usuario, contraseña, nombre_completo, 'estudiante')
            messagebox.showinfo("Éxito", "Estudiante registrado correctamente.")
            ventanaEstudiante.destroy()

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

    def cerrar_sesion():
        ventanaSuperadmin.destroy()
        from login import abrirVentanaLogin
        abrirVentanaLogin()

    botonCerrarSesion = tk.Button(ventanaSuperadmin, text="Cerrar Sesión", width=20, command=cerrar_sesion)
    botonCerrarSesion.grid(row=4, column=0, columnspan=2, pady=10, padx=30)

def verificar_datos_usuario(usuario, contraseña, nombre_completo, identificacion=None, rol=None):

    if not usuario or not contraseña or not nombre_completo:
        return False, "No se permiten campos vacíos."
   
    if not usuario.isdigit():
        return False, "El usuario debe ser el número de documento de identidad (solo números)."
    
    if not all(c.isalpha() or c.isspace() for c in nombre_completo):
        return False, "El nombre completo solo debe contener letras y espacios."

    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    tiene_mayus = False
    tiene_minus = False
    tiene_num = False
    for c in contraseña:
        if c.isupper():
            tiene_mayus = True
        elif c.islower():
            tiene_minus = True
        elif c.isdigit():
            tiene_num = True
    if not tiene_mayus:
        return False, "La contraseña debe tener al menos una mayuscula."
    if not tiene_minus:
        return False, "La contraseña debe tener al menos una minúscula."
    if not tiene_num:
        return False, "La contraseña debe tener al menos un número."
    
    
    try:
        with open('datos/usuarios.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                partes = linea.strip().split(',')
                if len(partes) >= 1 and partes[0] == usuario:
                    return False, f"Ya existe un usuario registrado con el documento {usuario}."
    except FileNotFoundError:
        pass
    
    return True, "Datos validos."

def registrar_usuario(usuario, contraseña, nombre_completo, rol, identificacion=None):
    ruta = 'datos/usuarios.txt'
    with open(ruta, 'a', encoding='utf-8') as f:
        f.write(f"{usuario},{contraseña},{rol},{nombre_completo}\n")
