from typing import List
from .Producto import Producto
import datetime

class Factura:
    def __init__(self, numero: int):
        if numero <= 0:
            raise ValueError("El número de factura debe ser positivo")
        self.numero = numero
        self.fecha_emision = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def actualizar_producto(self, indice: int, nuevo_producto: Producto):
        if 0 <= indice < len(self.productos):
            self.productos[indice] = nuevo_producto

    def __str__(self):
        detalles_productos = "\n".join(str(prod) for prod in self.productos)
        return f'Factura N°{self.numero} ({self.fecha_emision}):\n{detalles_productos}'