import tkinter as tk
from tkinter import messagebox, ttk
from superadmin import verificar_datos_usuario

def abrirVentanaAdmin():
    def registrar_estudiante():
        ventanaRegistro = tk.Toplevel()
        ventanaRegistro.title("Registrar Estudiante")
        ventanaRegistro.geometry("400x300")
        ventanaRegistro.resizable(False, False)

        titulo = tk.Label(ventanaRegistro, text="Registrar Estudiante", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        labelDocumento = tk.Label(ventanaRegistro, text="Documento de Identidad:")
        labelDocumento.grid(row=1, column=0, padx=30, pady=5)
        cajaDocumento = tk.Entry(ventanaRegistro)
        cajaDocumento.grid(row=1, column=1, padx=30, pady=5)

        labelNombre = tk.Label(ventanaRegistro, text="Nombre Completo:")
        labelNombre.grid(row=2, column=0, padx=30, pady=5)
        cajaNombre = tk.Entry(ventanaRegistro)
        cajaNombre.grid(row=2, column=1, padx=30, pady=5)

        labelContraseña = tk.Label(ventanaRegistro, text="Contraseña:")
        labelContraseña.grid(row=3, column=0, padx=30, pady=5)
        cajaContraseña = tk.Entry(ventanaRegistro, show="*")
        cajaContraseña.grid(row=3, column=1, padx=30, pady=5)

        def guardar_estudiante():
            documento = cajaDocumento.get().strip()
            contraseña = cajaContraseña.get().strip()
            nombre_completo = cajaNombre.get().strip()
            
            valido, mensaje = verificar_datos_usuario(documento, contraseña, nombre_completo, rol='estudiante')
            if not valido:
                messagebox.showerror("Error de validación", mensaje)
                return
            
            # Guardar en archivo de estudiantes
            with open('datos/estudiantes.txt', 'a', encoding='utf-8') as f:
                f.write(f"{documento},{nombre_completo},{contraseña}\n")
            
            # Guardar en usuarios.txt para login
            with open('datos/usuarios.txt', 'a', encoding='utf-8') as f:
                f.write(f"{documento},{contraseña},estudiante,{nombre_completo}\n")
            
            messagebox.showinfo("Éxito", "Estudiante registrado correctamente.")
            ventanaRegistro.destroy()

        botonGuardar = tk.Button(ventanaRegistro, text="Guardar", command=guardar_estudiante)
        botonGuardar.grid(row=4, column=0, columnspan=2, pady=15)

    def ingresar_calificaciones():
        ventanaCalificaciones = tk.Toplevel()
        ventanaCalificaciones.title("Ingresar Calificaciones")
        ventanaCalificaciones.geometry("500x400")
        ventanaCalificaciones.resizable(False, False)

        titulo = tk.Label(ventanaCalificaciones, text="Ingresar Calificaciones", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=4, pady=10)

        # Campos de entrada
        tk.Label(ventanaCalificaciones, text="Documento:").grid(row=1, column=0, padx=5, pady=5)
        cajaDocumento = tk.Entry(ventanaCalificaciones)
        cajaDocumento.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventanaCalificaciones, text="Módulo:").grid(row=1, column=2, padx=5, pady=5)
        cajaModulo = tk.Entry(ventanaCalificaciones)
        cajaModulo.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(ventanaCalificaciones, text="Parcial 1 (30%):").grid(row=2, column=0, padx=5, pady=5)
        cajaParcial1 = tk.Entry(ventanaCalificaciones)
        cajaParcial1.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(ventanaCalificaciones, text="Parcial 2 (30%):").grid(row=2, column=2, padx=5, pady=5)
        cajaParcial2 = tk.Entry(ventanaCalificaciones)
        cajaParcial2.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(ventanaCalificaciones, text="Proyecto Final (40%):").grid(row=3, column=0, padx=5, pady=5)
        cajaProyecto = tk.Entry(ventanaCalificaciones)
        cajaProyecto.grid(row=3, column=1, padx=5, pady=5)

        def guardar_calificacion():
            documento = cajaDocumento.get().strip()
            modulo = cajaModulo.get().strip()
            parcial1 = cajaParcial1.get().strip()
            parcial2 = cajaParcial2.get().strip()
            proyecto = cajaProyecto.get().strip()
            
            if not all([documento, modulo, parcial1, parcial2, proyecto]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            try:
                p1 = float(parcial1)
                p2 = float(parcial2)
                proy = float(proyecto)
                
                if not (0 <= p1 <= 5 and 0 <= p2 <= 5 and 0 <= proy <= 5):
                    messagebox.showerror("Error", "Las calificaciones deben estar entre 0 y 5")
                    return
                
                promedio = (p1 * 0.3) + (p2 * 0.3) + (proy * 0.4)
                estado = "Aprobado" if promedio >= 3.0 else "Reprobado"
                
                with open('datos/calificaciones.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{documento},{modulo},{p1},{p2},{proy},{promedio:.2f},{estado}\n")
                
                messagebox.showinfo("Éxito", f"Calificación guardada. Promedio: {promedio:.2f} - {estado}")
                ventanaCalificaciones.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Las calificaciones deben ser números")

        botonGuardar = tk.Button(ventanaCalificaciones, text="Guardar Calificación", command=guardar_calificacion)
        botonGuardar.grid(row=4, column=0, columnspan=4, pady=20)

    def consultar_calificaciones():
        ventanaConsulta = tk.Toplevel()
        ventanaConsulta.title("Consultar Calificaciones")
        ventanaConsulta.geometry("800x600")
        ventanaConsulta.resizable(False, False)

        titulo = tk.Label(ventanaConsulta, text="Consultar Calificaciones", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(ventanaConsulta, text="Módulo:").grid(row=1, column=0, padx=5, pady=5)
        cajaModulo = tk.Entry(ventanaConsulta)
        cajaModulo.grid(row=1, column=1, padx=5, pady=5)

        def cargar_datos():
            try:
                # Limpiar tabla
                for item in tree.get_children():
                    tree.delete(item)
                
                modulo = cajaModulo.get().strip()
                aprobados = 0
                reprobados = 0
                
                with open('datos/calificaciones.txt', 'r', encoding='utf-8') as f:
                    for linea in f:
                        datos = linea.strip().split(',')
                        if len(datos) >= 7 and (not modulo or datos[1] == modulo):
                            documento, mod, p1, p2, proy, prom, estado = datos
                            tree.insert('', 'end', values=(documento, mod, p1, p2, proy, prom, estado))
                            
                            if estado == "Aprobado":
                                aprobados += 1
                            else:
                                reprobados += 1
                
                labelEstadisticas.config(text=f"Aprobados: {aprobados} | Reprobados: {reprobados}")
                
            except FileNotFoundError:
                messagebox.showinfo("Info", "No hay calificaciones registradas")

        botonConsultar = tk.Button(ventanaConsulta, text="Consultar", command=cargar_datos)
        botonConsultar.grid(row=1, column=2, padx=5, pady=5)

        # Crear tabla
        columns = ('Documento', 'Módulo', 'Parcial 1', 'Parcial 2', 'Proyecto', 'Promedio', 'Estado')
        tree = ttk.Treeview(ventanaConsulta, columns=columns, show='headings')
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        labelEstadisticas = tk.Label(ventanaConsulta, text="", font=("Arial", 12))
        labelEstadisticas.grid(row=3, column=0, columnspan=3, pady=10)

    # Ventana principal del administrador
    ventanaAdmin = tk.Toplevel()
    ventanaAdmin.title("Ventana Administrador")
    ventanaAdmin.geometry("400x350")
    ventanaAdmin.resizable(False, False)

    labelTitulo = tk.Label(ventanaAdmin, text="Bienvenido Administrador", font=("Arial", 16))
    labelTitulo.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=30)

    labelTexto = tk.Label(ventanaAdmin, text="Gestión de Calificaciones", font=("Arial", 12))
    labelTexto.grid(row=1, column=0, columnspan=2, pady=(0, 20), padx=30)

    botonRegistrar = tk.Button(ventanaAdmin, text="Registrar Estudiante", width=20, command=registrar_estudiante)
    botonRegistrar.grid(row=2, column=0, columnspan=2, pady=10, padx=30)

    botonCalificaciones = tk.Button(ventanaAdmin, text="Ingresar Calificaciones", width=20, command=ingresar_calificaciones)
    botonCalificaciones.grid(row=3, column=0, columnspan=2, pady=10, padx=30)

    botonConsultar = tk.Button(ventanaAdmin, text="Consultar Calificaciones", width=20, command=consultar_calificaciones)
    botonConsultar.grid(row=4, column=0, columnspan=2, pady=10, padx=30)

    def cerrar_sesion():
        ventanaAdmin.destroy()
        from login import abrirVentanaLogin
        abrirVentanaLogin()

    botonCerrarSesion = tk.Button(ventanaAdmin, text="Cerrar Sesión", width=20, command=cerrar_sesion)
    botonCerrarSesion.grid(row=5, column=0, columnspan=2, pady=10, padx=30)
