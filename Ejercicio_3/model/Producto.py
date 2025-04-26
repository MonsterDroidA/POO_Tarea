import re

class Producto:
    def __init__(self, codigo: str, precio: float):
        if not re.match(r"^[a-zA-Z0-9]+$", codigo):
            raise ValueError("El código debe ser alfanumérico")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        
        self.codigo = codigo
        self.precio = precio

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = nuevo_precio

    def __str__(self):
        return f'Código: {self.codigo}, Precio: ${self.precio:.2f}'