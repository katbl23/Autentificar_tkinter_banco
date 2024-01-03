import tkinter as tk
from tkinter import messagebox

# Credenciales de usuario
usuario_correcto = "humano2390"
contraseña_correcta = "6578"
dinero_inicial = 2000 


def autenticar():
    # Obtener valores de las entradas de usuario y contraseña
    usuario_introducido = entry_usuario.get()
    contraseña_introducida = entry_contraseña.get()

    # Verificar las credenciales
    if usuario_introducido == usuario_correcto and contraseña_introducida == contraseña_correcta:
        mostrar_menu()
    else:
        messagebox.showerror("Error de Autenticación", "Credenciales incorrectas. Inténtalo de nuevo.")

def Transferir():
    # Crear etiqueta y entrada para la cantidad a transferir
    print("Estoy aqui")
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Depositar")
    cantidad_transferir_label = tk.Label(ventana_menu, text="Ingresa la cantidad a transferir")
    cantidad_transferir_label.pack(pady=10)
    
    cantidad_transferir_entry = tk.Entry(ventana_menu)
    cantidad_transferir_entry.pack(pady=10)

    def realizar_transferencia():
        # Obtener la cantidad a transferir desde la entrada del usuario
        cantidad_transferir_str = cantidad_transferir_entry.get()

        # Verificar si la entrada está vacía
        if not cantidad_transferir_str:
            messagebox.showerror("Error", "Por favor, ingrese una cantidad antes de transferir.")
            return

        try:
            # Convertir la cantidad a transferir a un número entero
            cantidad_transferir_int = int(cantidad_transferir_str)

            # Verificar si hay suficiente dinero para la transferencia
            global dinero_inicial
            if dinero_inicial >= cantidad_transferir_int:
                print("Operación aprobada")
                dinero_inicial -= cantidad_transferir_int
                print("Nuevo saldo:", dinero_inicial)
                messagebox.showinfo("Operación Aprobada", f"Su saldo es: ${dinero_inicial}")
            else:
                messagebox.showerror("Error", "No tiene fondos suficientes para esta operación")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")

    # Crear botón para realizar la transferencia
    boton_transferir = tk.Button(ventana_menu, text="Transferir", command=realizar_transferencia)
    boton_transferir.pack(pady=10)

def Versaldo():
    global dinero_inicial 
    messagebox.showinfo("Saldo Actual", f"Su saldo actual es: ${dinero_inicial}")

    
def Depositar():
    print("Estoy aqui")
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Depositar")
    cantidad_depositar_label = tk.Label(ventana_menu, text="Ingresa la cantidad a depositar")
    cantidad_depositar_label.pack(pady=10)
    cantidad_depositar_entry = tk.Entry(ventana_menu)
    cantidad_depositar_entry.pack(pady=10)

    def realizar_deposito():
        # Obtener la cantidad a depositar desde la entrada del usuario
        cantidad_depositar_str = cantidad_depositar_entry.get()

        # Verificar si la entrada está vacía
        if not cantidad_depositar_str:
            messagebox.showerror("Error", "Por favor, ingrese una cantidad antes de depositar.")
            return

        try:
            # Convertir la cantidad a depositar a un número entero
            cantidad_depositar_int = int(cantidad_depositar_str)

            # Verificar si hay suficiente dinero para la operación
            global dinero_inicial
            print("Operación aprobada")
            dinero_inicial += cantidad_depositar_int
            
            messagebox.showinfo("Operacion aprobada", f"Su saldo actual es: $ {dinero_inicial}")
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")

    # Crear botón para realizar el depósito
    boton_depositar = tk.Button(ventana_menu, text="Depositar", command=realizar_deposito)
    boton_depositar.pack(pady=10)

def mostrar_menu():
    # Cerrar la ventana principal
    #ventana.destroy()

    # Crear una nueva ventana para el menú
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Principal")

    # Agregar elementos del menú (puedes personalizar esto según tus necesidades)
    etiqueta_menu = tk.Label(ventana_menu, text="Seleccione una opción:")
    etiqueta_menu.pack(pady=10)

    opcion1 = tk.Button(ventana_menu, text="Transferir", command=Transferir)
    opcion1.pack(pady=5)

    opcion2 = tk.Button(ventana_menu, text="Ver saldo", command=Versaldo)
    opcion2.pack(pady=5)

    opcion3 = tk.Button(ventana_menu, text="Depositar", command=Depositar)
    opcion3.pack(pady=5)

def mostrar_mensaje_menu(opcion):
    mensaje = f"Has seleccionado: {opcion}"
    messagebox.showinfo("Selección de Menú", mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenido a Schoolarbank")

ventana.geometry("400x200")

# Crear etiquetas y entradas para usuario y contraseña
etiqueta_usuario = tk.Label(ventana, text="Ingrese su Usuario:")
etiqueta_usuario.pack(pady=10)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=10)

etiqueta_contraseña = tk.Label(ventana, text="Ingrese su contraseña:")
etiqueta_contraseña.pack(pady=10)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack(pady=10)

# Crear botón de autenticación
boton = tk.Button(ventana, text="Ingresar", command=autenticar)
boton.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
