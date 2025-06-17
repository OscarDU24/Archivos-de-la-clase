# Sistema de Gestión de Pagos

usuarios = {}
pagos = []

#Registro de cuenta
def registrarusuario():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    usuarios[usuario] = contraseña
    print("Cuenta creada exitosamente.\n")

#Incio de sesion
def iniciarsesion():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuarios.get(usuario) == contraseña:
        print("Acceso concedido.\n")
        return usuario
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.\n")
        return None

#Registo de pagos
def registrarpago(usuario):
    proveedor = input("Ingrese el nombre del proveedor: ")
    tipogasto = input("Ingrese el tipo de gasto: ")
    monto = float(input("Ingrese el monto: "))
    fechavencimiento = input("Ingrese la fecha de vencimiento: ")
    frecuenciapago = input("Seleccione la frecuencia de pago (mensual/trimestral/anual): ")
    categoria = input("Seleccione la categoría (Servicios/Préstamos/Nómina/Otros): ")
    formapago = input("Ingrese la forma de pago: ")

#Agregarlo    
    pagos.append({
        "usuario": usuario,
        "proveedor": proveedor,
        "tipogasto": tipogasto,
        "monto": monto,
        "fechavencimiento": fechavencimiento,
        "frecuenciapago": frecuenciapago,
        "categoria": categoria,
        "formapago": formapago
    })
    
    print("Pago registrado exitosamente.\n")

def mostrarpagos(usuario):
    print("\nPagos pendientes:")
    for pago in pagos:
        if pago["usuario"] == usuario:
            print(f"Proveedor: {pago['proveedor']}, Monto: {pago['monto']}, Vence: {pago['fechavencimiento']}")

def configuraralertas():
    print("Configurando recordatorios...\nAlertas activadas para todos los pagos próximos.\n")

#Menu del sistema
def menuprincipal(usuario):
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar nuevo pago")
        print("2. Mostrar pagos pendientes")
        print("3. Configurar alertas")
        print("4. Salir")
        
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            registrarpago(usuario)
        elif opcion == "2":
            mostrarpagos(usuario)
        elif opcion == "3":
            configuraralertas()
        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Flujo del sistema
registrarusuario()
usuarioactual = iniciarsesion()

if usuarioactual:
    menuprincipal(usuarioactual)