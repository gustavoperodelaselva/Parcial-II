import tkinter as tk
from tkinter import messagebox, ttk
from superadmin import verificar_datos_usuario

def abrirVentanaAdmin():
    def inscribirEstudiante():
        ventanaInscripcion = tk.Toplevel()
        ventanaInscripcion.title("Inscribir Estudiante a Módulo")
        ventanaInscripcion.geometry("500x300")
        ventanaInscripcion.resizable(False, False)

    
        ventanaInscripcion.grid_rowconfigure(0, weight=1)
        ventanaInscripcion.grid_rowconfigure(4, weight=1)
        ventanaInscripcion.grid_columnconfigure(0, weight=1)
        ventanaInscripcion.grid_columnconfigure(1, weight=1)

        tk.Label(ventanaInscripcion, text="Inscripción de Estudiante", font=("Arial", 14)).grid(row=1, column=0, columnspan=2, pady=(30, 20), padx=50)

        tk.Label(ventanaInscripcion, text="Documento Estudiante:").grid(row=2, column=0, padx=20, pady=10, sticky='e')
        entryDoc = tk.Entry(ventanaInscripcion)
        entryDoc.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        tk.Label(ventanaInscripcion, text="Código del Módulo:").grid(row=3, column=0, padx=20, pady=10, sticky='e')
        entryModulo = tk.Entry(ventanaInscripcion)
        entryModulo.grid(row=3, column=1, padx=20, pady=10, sticky='w')

        def guardar_inscripcion():
            doc = entryDoc.get().strip()
            modulo = entryModulo.get().strip()

            if not doc or not modulo:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            estudiante_existe = False
            with open('datos/usuarios.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 3 and partes[0] == doc and partes[2] == "estudiante":
                        estudiante_existe = True
                        break
            if not estudiante_existe:
                messagebox.showerror("Error", f"No existe el estudiante con documento {doc}.")
                return

            modulo_existe = False
            with open('datos/modulos.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 1 and partes[0] == modulo:
                        modulo_existe = True
                        break
            if not modulo_existe:
                messagebox.showerror("Error", f"No existe el módulo con código {modulo}.")
                return

            with open('datos/inscripciones.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    if linea.strip() == f"{doc},{modulo}":
                        messagebox.showerror("Error", "El estudiante ya está inscrito en ese módulo.")
                        return


            with open('datos/inscripciones.txt', 'a', encoding='utf-8') as f:
                f.write(f"{doc},{modulo}\n")

            messagebox.showinfo("Éxito", f"Estudiante inscrito en módulo {modulo}.")
            ventanaInscripcion.destroy()

        tk.Button(ventanaInscripcion, text="Inscribir", command=guardar_inscripcion).grid(row=4, column=0, columnspan=2, pady=30)


    def registrarModulos():
        ventanaModulos=tk.Toplevel()
        ventanaModulos.title("Registrar Modulos")

        titulo = tk.Label(ventanaModulos, text="Registrar Modulos", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        labelNprof=tk.Label(ventanaModulos,text="Nombre del profesor")
        labelNprof.grid(row=1, column=0, padx=30, pady=5)
        cajaNprof=tk.Entry(ventanaModulos)
        cajaNprof.grid(row=1, column=1, padx=30, pady=5)

        labelCod=tk.Label(ventanaModulos,text="Codigo modulo")
        labelCod.grid(row=2, column=0,padx=30,pady=5)
        cajaCod=tk.Entry(ventanaModulos)
        cajaCod.grid(row=2,column=1,padx=30,pady=5)

        labelMateria=tk.Label(ventanaModulos,text="Nombre modulo")
        labelMateria.grid(row=3,column=0,padx=30,pady=5)
        cajaMateria=tk.Entry(ventanaModulos)
        cajaMateria.grid(row=3,column=1,padx=30,pady=5)

        def guardarModulo():
            Nprof = cajaNprof.get().strip()
            cod = cajaCod.get().strip()
            materia = cajaMateria.get().strip()

            if not all([Nprof, cod, materia]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            
            with open('datos/modulos.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 1 and partes[0] == cod:
                        messagebox.showerror("Error", f"Ya existe un módulo con el código {cod}.")
                        return


            profesor_encontrado = False
            
            with open('datos/usuarios.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 4:
                        doc, contraseña, rol, nombre = partes
                        if rol == 'profesor' and nombre.strip().lower() == Nprof.lower():
                            profesor_encontrado = True
                            break

            if not profesor_encontrado:
                messagebox.showerror("Error", f"No existe un profesor registrado con el nombre: {Nprof}")
                return

            try:
                with open('datos/modulos.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{cod},{materia},{Nprof}\n")
                messagebox.showinfo("Éxito", "Módulo registrado correctamente.")
                ventanaModulos.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el módulo: {e}")
    
        botonGuardar=tk.Button(ventanaModulos,text="Guardar",command=guardarModulo)
        botonGuardar.grid(row=4,column=0,columnspan=2,pady=15)



        


    def ingresar_calificaciones():
        ventanaCalificaciones = tk.Toplevel()
        ventanaCalificaciones.title("Ingresar Calificaciones")
        ventanaCalificaciones.geometry("700x400")
        ventanaCalificaciones.resizable(False, False)

        titulo = tk.Label(ventanaCalificaciones, text="Ingresar Calificaciones", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=4, pady=10)

        tk.Label(ventanaCalificaciones, text="Documento:").grid(row=1, column=0, padx=5, pady=5)
        cajaDocumento = tk.Entry(ventanaCalificaciones)
        cajaDocumento.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventanaCalificaciones, text="Cod. Módulo:").grid(row=1, column=2, padx=5, pady=5)
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
            
            estudiante_encontrado = False
            
            with open('datos/usuarios.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 4:
                        doc, _, rol, _ = partes
                        if doc == documento and rol == 'estudiante':
                            estudiante_encontrado = True
                            break
            
            if not estudiante_encontrado:
                messagebox.showerror("Error", f"No existe un estudiante con documento: {documento}")
                return

            modulo_encontrado = False
            with open('datos/modulos.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 1 and partes[0] == modulo:
                        modulo_encontrado = True
                        break

            if not modulo_encontrado:
                messagebox.showerror("Error", f"No existe el módulo con código: {modulo}")
                return

            inscrito = False
            with open('datos/inscripciones.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    doc_mod = linea.strip().split(',')
                    if len(doc_mod) == 2 and doc_mod[0] == documento and doc_mod[1] == modulo:
                        inscrito = True
                        break

                if not inscrito:
                    messagebox.showerror("Error", f"El estudiante no está inscrito en el módulo {modulo}")
                    return
            
            with open('datos/calificaciones.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) >= 2 and partes[0] == documento and partes[1] == modulo:
                        messagebox.showerror("Error", "Este estudiante ya tiene calificación registrada en este módulo.")
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
        ventanaConsulta.geometry("1200x700")
        ventanaConsulta.resizable(False, False)

        # Configurar grid weights para centrar
        ventanaConsulta.grid_rowconfigure(0, weight=1)
        ventanaConsulta.grid_rowconfigure(4, weight=1)
        ventanaConsulta.grid_columnconfigure(0, weight=1)
        ventanaConsulta.grid_columnconfigure(1, weight=1)
        ventanaConsulta.grid_columnconfigure(2, weight=1)

        titulo = tk.Label(ventanaConsulta, text="Consultar Calificaciones", font=("Arial", 16))
        titulo.grid(row=1, column=0, columnspan=3, pady=(30, 20), padx=50)

        tk.Label(ventanaConsulta, text="Módulo:").grid(row=2, column=0, padx=20, pady=10, sticky='e')
        cajaModulo = tk.Entry(ventanaConsulta, width=40)
        cajaModulo.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        def cargar_datos():
            try:

                for item in tree.get_children():
                    tree.delete(item)

                modulo_filtrado = cajaModulo.get().strip()
                aprobados = 0
                reprobados = 0

                estudiantes = {}
                with open('datos/usuarios.txt', 'r', encoding='utf-8') as f:
                    for linea in f:
                        partes = linea.strip().split(',')
                        if len(partes) >= 4:
                            doc, _, rol, nombre = partes
                            if rol == 'estudiante':
                                estudiantes[doc] = nombre

                modulos = {}
                with open('datos/modulos.txt', 'r', encoding='utf-8') as f:
                    for linea in f:
                        partes = linea.strip().split(',')
                        if len(partes) >= 2:
                            cod, materia = partes[0], partes[1]
                            modulos[cod] = materia


                with open('datos/calificaciones.txt', 'r', encoding='utf-8') as f:
                    for linea in f:
                        datos = linea.strip().split(',')
                        if len(datos) >= 7:
                            documento, cod_modulo, p1, p2, proy, prom, estado = datos
                            if modulo_filtrado and cod_modulo != modulo_filtrado:
                                continue
                            
                            nombre = estudiantes.get(documento, "...")
                            materia = modulos.get(cod_modulo, "...")

                            tree.insert('', 'end', values=(documento, nombre, cod_modulo, materia, p1, p2, proy, prom, estado))

                            if estado == "Aprobado":
                                aprobados += 1
                            else:
                                reprobados += 1

                labelEstadisticas.config(text=f"Aprobados: {aprobados} | Reprobados: {reprobados}")
                
            except FileNotFoundError:
                messagebox.showinfo("Info", "No hay calificaciones registradas")

        botonConsultar = tk.Button(ventanaConsulta, text="Consultar", command=cargar_datos)
        botonConsultar.grid(row=2, column=2, padx=20, pady=10)

        columns = ('Documento', 'Nombre', 'Código Módulo', 'Materia', 'Parcial 1', 'Parcial 2', 'Proyecto', 'Promedio', 'Estado')
        tree = ttk.Treeview(ventanaConsulta, columns=columns, show='headings', height=20)

        column_widths = [120, 200, 120, 150, 100, 100, 100, 100, 100]
        for i, col in enumerate(columns):
            tree.heading(col, text=col)
            tree.column(col, width=column_widths[i], anchor='center')

        tree.grid(row=3, column=0, columnspan=3, padx=20, pady=20, sticky='nsew')

        labelEstadisticas = tk.Label(ventanaConsulta, text="", font=("Arial", 14))
        labelEstadisticas.grid(row=4, column=0, columnspan=3, pady=20)

    ventanaAdmin = tk.Toplevel()
    ventanaAdmin.title("Ventana Administrador")
    ventanaAdmin.geometry("500x450")
    ventanaAdmin.resizable(False, False)

    ventanaAdmin.grid_rowconfigure(0, weight=1)
    ventanaAdmin.grid_rowconfigure(7, weight=1)
    ventanaAdmin.grid_columnconfigure(0, weight=1)
    ventanaAdmin.grid_columnconfigure(1, weight=1)

    labelTitulo = tk.Label(ventanaAdmin, text="Bienvenido Administrador", font=("Arial", 16))
    labelTitulo.grid(row=1, column=0, columnspan=2, pady=(30, 10), padx=50)

    labelTexto = tk.Label(ventanaAdmin, text="Gestión de Calificaciones", font=("Arial", 12))
    labelTexto.grid(row=2, column=0, columnspan=2, pady=(0, 30), padx=50)

    botonRegistrar = tk.Button(ventanaAdmin, text="Inscribir a modulo", width=20, command=inscribirEstudiante)
    botonRegistrar.grid(row=3, column=0, columnspan=2, pady=15, padx=50)

    botonRModulo=tk.Button(ventanaAdmin,text="Registrar modulo",width=20,command=registrarModulos)
    botonRModulo.grid(row=4,column=0,columnspan=2,pady=15,padx=50)

    botonCalificaciones = tk.Button(ventanaAdmin, text="Ingresar Calificaciones", width=20, command=ingresar_calificaciones)
    botonCalificaciones.grid(row=5, column=0, columnspan=2, pady=15, padx=50)

    botonConsultar = tk.Button(ventanaAdmin, text="Consultar Calificaciones", width=20, command=consultar_calificaciones)
    botonConsultar.grid(row=6, column=0, columnspan=2, pady=15, padx=50)

    def cerrar_sesion():
        ventanaAdmin.destroy()
        from login import abrirVentanaLogin
        abrirVentanaLogin()

    botonCerrarSesion = tk.Button(ventanaAdmin, text="Cerrar Sesión", width=20, command=cerrar_sesion)
    botonCerrarSesion.grid(row=7, column=0, columnspan=2, pady=15, padx=50)
