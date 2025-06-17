# Sistema de Gestión de Pagos

usuarios = {}  # Diccionario para almacenar cuentas de usuario
pagos = []  # Lista para almacenar los pagos registrados

# Registro de cuenta con verificación de usuario existente
def registrar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, inicie sesión.\n")
        return
    
    contraseña = input("Ingrese su contraseña: ")
    usuarios[usuario] = contraseña
    print("Cuenta creada exitosamente.\n")

# Inicio de sesión con validación
def iniciar_sesion():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuarios.get(usuario) == contraseña:
        print("Acceso concedido.\n")
        return usuario
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.\n")
        return None

# Registro de pagos asociados al usuario
def registrar_pago(usuario):
    proveedor = input("Ingrese el nombre del proveedor: ")
    tipo_gasto = input("Ingrese el tipo de gasto: ")
    monto = float(input("Ingrese el monto: "))
    fecha_vencimiento = input("Ingrese la fecha de vencimiento: ")
    frecuencia_pago = input("Seleccione la frecuencia de pago (mensual/trimestral/anual): ")
    categoria = input("Seleccione la categoría (Servicios/Préstamos/Nómina/Otros): ")
    forma_pago = input("Ingrese la forma de pago: ")

    # Agregar pago a la lista
    pagos.append({
        "usuario": usuario,
        "proveedor": proveedor,
        "tipo_gasto": tipo_gasto,
        "monto": monto,
        "fecha_vencimiento": fecha_vencimiento,
        "frecuencia_pago": frecuencia_pago,
        "categoria": categoria,
        "forma_pago": forma_pago
    })

    print("Pago registrado exitosamente.\n")

# Mostrar pagos del usuario actual
def mostrar_pagos(usuario):
    print("\nPagos pendientes:")
    encontrados = False
    for pago in pagos:
        if pago["usuario"] == usuario:
            print(f"Proveedor: {pago['proveedor']}, Monto: {pago['monto']}, Vence: {pago['fecha_vencimiento']}")
            encontrados = True
    
    if not encontrados:
        print("No hay pagos registrados.\n")

# Configuración de alertas de vencimiento
def configurar_alertas():
    print("Configurando recordatorios...\nAlertas activadas para todos los pagos próximos.\n")

# Menú principal tras inicio de sesión
def menu_principal(usuario):
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar nuevo pago")
        print("2. Mostrar pagos pendientes")
        print("3. Configurar alertas")
        print("4. Cerrar sesión")
        
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            registrar_pago(usuario)
        elif opcion == "2":
            mostrar_pagos(usuario)
        elif opcion == "3":
            configurar_alertas()
        elif opcion == "4":
            print("Sesión finalizada.\n")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Menú de inicio del sistema
while True:
    print("=== Sistema de Gestión de Pagos ===")
    print("1. Registrar nueva cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")
    
    opcion_inicio = input("Seleccione una opción: ")

    if opcion_inicio == "1":
        registrar_usuario()
    elif opcion_inicio == "2":
        usuario_actual = iniciar_sesion()
        if usuario_actual:
            menu_principal(usuario_actual)
    elif opcion_inicio == "3":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")