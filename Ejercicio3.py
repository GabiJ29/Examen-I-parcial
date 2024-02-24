#Aplicación que permita calcular el descuento
def aplicar_descuento(productos):
    descuento_productos = []
    for productos in productos:
        if productos["precio"] > 500:
            descuento_precio = productos["precio"] * 0.9
            descuento_productos = {
                "nombre": productos["nombre"],
                "precio": descuento_precio,
            }
            descuento_productos.append(descuento_productos)
        else:
            descuento_productos.append(productos)
    return descuento_productos

products = [
    {"nmbre": "Producto 1", "precio": 400},
    {"nombre": "Producto 2", "precio": 600},
    {"nombre": "Producto 3", "precio": 700},
]

descuento_productos = aplicar_descuento(productos)
for productos in descuento_productos:
    print(f"nombre: {productos['nombre']}, Precio: {productos['precio']}")