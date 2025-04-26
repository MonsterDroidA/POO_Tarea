from model.Factura import Factura
from model.Producto import Producto
from model.Persistencia import Persistencia

# Crear factura
factura = Factura(numero=1001)

# Agregar productos
factura.agregar_producto(Producto('C1', 24))
factura.agregar_producto(Producto('H23', 234))
factura.agregar_producto(Producto('M30', 109))

# Guardar la factura en JSON
Persistencia.guardar_factura(factura)

# Mostrar factura inicial
print("\nFactura inicial:")
print(factura)

# Cambiar el segundo producto
factura.actualizar_producto(1, Producto('K123', 247))

# Guardar la factura actualizada
Persistencia.guardar_factura(factura)

# Mostrar factura después de la actualización
print("\nFactura actualizada:")
print(factura)

# Recuperar todas las facturas guardadas
print("\nHistorial de facturas guardadas:")
facturas_guardadas = Persistencia.cargar_facturas()
for f in facturas_guardadas:
    print(f"\nFactura N°{f['numero']} ({f['fecha']}):")
    for p in f["productos"]:
        print(f"   Código: {p['codigo']}, Precio: ${p['precio']:.2f}")