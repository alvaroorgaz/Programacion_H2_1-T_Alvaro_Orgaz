import uuid  #generar un número único de pedido

#almacenar los datos de los clientes, productos y pedidos
clientes = []
productos = [
    {"id": 1, "nombre": "Iphone 15", "precio": 1000},
    {"id": 2, "nombre": "Lavadora Plus", "precio": 500},
    {"id": 3, "nombre": "Smartwatch", "precio": 300}
]
pedidos = []

#registrar un cliente
def registrar_cliente():
    nombre = input("Introduce tu nombre completo: ")
    correo = input("Introduce tu correo electrónico: ")
    
    # Verificar si el correo ya está registrado
    for cliente in clientes:
        if cliente['correo'] == correo:
            print("Este correo ya está registrado. Intenta con otro.")
            return
    
    telefono = input("Introduce tu número de teléfono: ")
    direccion = input("Introduce tu dirección: ")
    
    # Crear el cliente y agregarlo 
    nuevo_cliente = {'nombre': nombre, 'correo': correo, 'telefono': telefono, 'direccion': direccion}
    clientes.append(nuevo_cliente)
    print(f"¡Bienvenido, {nombre}! Te has registrado exitosamente.")

# Función para mostrar todos los clientes registrados
def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados aún.")
        return
    print("Clientes registrados:")
    for cliente in clientes:
        print(f"{cliente['nombre']} - {cliente['correo']}")

# Función para buscar un cliente por correo
def buscar_cliente():
    correo_buscar = input("Introduce el correo del cliente que deseas buscar: ")
    for cliente in clientes:
        if cliente['correo'] == correo_buscar:
            print(f"Cliente encontrado: {cliente['nombre']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Dirección: {cliente['direccion']}")
            return
    print("No se encontró a ningún cliente con ese correo.")

# Función para realizar una compra
def realizar_compra():
    correo_cliente = input("Introduce tu correo electrónico: ")
    
    # Buscar al cliente
    cliente = None
    for c in clientes:
        if c['correo'] == correo_cliente:
            cliente = c
            break
    
    if cliente is None:
        print("No estás registrado. Por favor, regístrate primero.")
        return
    
    print("Productos disponibles para la compra:")
    for producto in productos:
        print(f"{producto['id']}: {producto['nombre']} - ${producto['precio']}")
    
    productos_comprados = []
    total = 0
    
    while True:
        id_producto = int(input("Introduce el ID del producto que quieres comprar (0 para finalizar): "))
        if id_producto == 0:
            break
        
        producto_encontrado = False
        for producto in productos:
            if producto['id'] == id_producto:
                productos_comprados.append(producto)
                total += producto['precio']
                producto_encontrado = True
                print(f"Producto agregado: {producto['nombre']}")
                break
        
        if not producto_encontrado:
            print("Producto no válido. Intenta nuevamente.")
    
    if not productos_comprados:
        print("No has seleccionado productos para comprar.")
        return
    
    # Generar número de pedido único
    numero_pedido = str(uuid.uuid4())
    nuevo_pedido = {'cliente': cliente, 'productos': productos_comprados, 'total': total, 'numero_pedido': numero_pedido}
    pedidos.append(nuevo_pedido)
    
    print(f"Compra realizada con éxito. Tu número de pedido es {numero_pedido}. El total de tu compra es ${total}.")

#hacer seguimiento de un pedido
def seguimiento_pedido():
    numero_pedido = input("Introduce tu número de pedido para ver el seguimiento: ")
    
    for pedido in pedidos:
        if pedido['numero_pedido'] == numero_pedido:
            print(f"Detalles del pedido #{numero_pedido}:")
            print(f"Cliente: {pedido['cliente']['nombre']}")
            print("Productos comprados:")
            for producto in pedido['productos']:
                print(f"- {producto['nombre']} (${producto['precio']})")
            print(f"Total: ${pedido['total']}")
            return
    
    print("No se encontró ningún pedido con ese número.")

# Menú principal
def mostrar_menu():
    while True:
        print("\n*** Menú de Gestión de Pedidos ***")
        print("1. Registrar un nuevo cliente")
        print("2. Ver todos los clientes")
        print("3. Buscar un cliente")
        print("4. Realizar una compra")
        print("5. Seguimiento de un pedido")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            mostrar_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            realizar_compra()
        elif opcion == '5':
            seguimiento_pedido()
        elif opcion == '6':
            print("Gracias por usar el sistema de gestión de pedidos. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

# Ejecutar el menú
mostrar_menu()
