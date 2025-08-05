import tkinter as tk
import os
import sys

from tkinter import messagebox

#& Función para centrar la ventana en la pantalla 
def centrar_ventana_en_pantalla(ventana, ancho, alto):
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    
#& Función para obtener la ruta absoluta del recurso 
def resource_path(relative_path):
    """Obtener la ruta absoluta del recurrso"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
        
#& Función para convertir la ruta 
def convertir_ruta():
    ruta = entrada.get()
    if ruta:
        ruta_convertida = ruta.replace("\\", "/")
        salida.delete(0, tk.END)
        salida.insert(0, ruta_convertida)
    else:
        messagebox.showinfo("Información", "Por favor, introduce una ruta para convertir")
        
#& Función para borrar el campo de ruta convertida cuando se borra la entrada
def borrar_ruta_convetida(event):
    if not entrada.get():
        salida.delete(0, tk.END)

#& Función para copiar la ruta convertida al portapapeles  
def copiar_ruta():
    ruta_convertida = salida.get()
    if ruta_convertida:
        ventana.clipboard_clear()
        ventana.clipboard_append(ruta_convertida)
                
    else:
        messagebox.showinfo("Información", "No hay ruta convertida para copiar")

#! Ventana principal
ventana = tk.Tk()
ventana.title("Conversor de rutas")
ventana.config(bg="#000000")
ventana.iconbitmap(resource_path("assets/icon.ico"))

centrar_ventana_en_pantalla(ventana, 500, 205)

# Etiqueta y campo de entrada
tk.Label(ventana, text="Pega la ruta: ", bg="#000000", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
entrada = tk.Entry(ventana, width=60)
entrada.pack(pady=5)
entrada.bind("<KeyRelease>", borrar_ruta_convetida)

# Botón para convertir
tk.Button(ventana, text="Convertir", command=convertir_ruta, font=("Arial", 10)).pack(pady=5)

# Campo de salida
tk.Label(ventana, text="Ruta convertida: ", bg="#000000", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
salida = tk.Entry(ventana, width=60)
salida.pack(pady=5)

# Botón para copiar
tk.Button(ventana, text="Copiar", command=copiar_ruta, font=("Arial", 11)).pack(pady=5)


ventana.mainloop()