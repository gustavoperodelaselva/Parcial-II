import tkinter as tk
from tkinter import ttk

def abrirVentanaEstudiante(documentoEstudiante):
    
    nombreEstudiante = "Estudiante"
    with open("datos/usuarios.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) >= 4:
                doc, _, rol, nombre = partes
                if doc == documentoEstudiante and rol == "estudiante":
                    nombreEstudiante = nombre
                    break
    
    
    ventana = tk.Toplevel()
    ventana.title("Menú Estudiante")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_rowconfigure(3, weight=1)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    labelTitulo = tk.Label(ventana, text=f"Bienvenido Estudiante {nombreEstudiante}", font=("Arial", 16))
    labelTitulo.grid(row=1, column=0, columnspan=2, pady=(30, 20), padx=50)

    def consultarNotas():
        ventanaNotas = tk.Toplevel()
        ventanaNotas.title("Mis Calificaciones")
        ventanaNotas.geometry("1000x700")
        ventanaNotas.resizable(False, False)

        # Configurar grid weights para centrar
        ventanaNotas.grid_rowconfigure(0, weight=1)
        ventanaNotas.grid_rowconfigure(3, weight=1)
        ventanaNotas.grid_columnconfigure(0, weight=1)
        ventanaNotas.grid_columnconfigure(1, weight=1)

        tk.Label(ventanaNotas, text="Mis Calificaciones", font=("Arial", 16)).grid(row=1, column=0, columnspan=2, pady=(30, 20), padx=50)

        columns = ("Módulo", "Materia", "Parcial 1", "Parcial 2", "Proyecto", "Promedio", "Estado")
        tree = ttk.Treeview(ventanaNotas, columns=columns, show="headings", height=20)

        column_widths = [150, 200, 120, 120, 120, 120, 120]
        for i, col in enumerate(columns):
            tree.heading(col, text=col)
            tree.column(col, width=column_widths[i], anchor='center')

        tree.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

        def cargarCalificaciones():
            for item in tree.get_children():
                tree.delete(item)

            modulosDict = {}
            
            with open("datos/modulos.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split(",")
                    if len(partes) >= 2:
                        cod, materia = partes[0], partes[1]
                        modulosDict[cod] = materia
            
            modulosInscritos = []
            with open("datos/inscripciones.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    doc, cod = linea.strip().split(",")
                    if doc == documentoEstudiante:
                        modulosInscritos.append(cod)

            with open("datos/calificaciones.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 7:
                        doc, cod_modulo, p1, p2, proy, prom, estado = datos
                        if doc == documentoEstudiante and cod_modulo in modulosInscritos:
                            materia = modulosDict.get(cod_modulo, "Desconocida")
                            tree.insert('', 'end', values=(cod_modulo, materia, p1, p2, proy, prom, estado))
            
        cargarCalificaciones()

    botonNotas = tk.Button(ventana, text="Ver Mis Notas", width=20, command=consultarNotas)
    botonNotas.grid(row=2, column=0, columnspan=2, pady=20, padx=50)

    def cerrarSesion():
        ventana.destroy()
        from login import abrirVentanaLogin
        abrirVentanaLogin()

    botonCerrar = tk.Button(ventana, text="Cerrar Sesión", width=20, command=cerrarSesion)
    botonCerrar.grid(row=3, column=0, columnspan=2, pady=20, padx=50)
