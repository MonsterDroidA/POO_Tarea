import json
from model.Factura import Factura
from model.Producto import Producto

class Persistencia:
    @staticmethod
    def guardar_factura(factura: Factura, archivo="facturas.json"):
        datos = {
            "numero": factura.numero,
            "fecha": factura.fecha_emision,
            "productos": [{"codigo": p.codigo, "precio": p.precio} for p in factura.productos]
        }

        try:
            with open(archivo, "r") as f:
                facturas = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            facturas = []

        facturas.append(datos)

        with open(archivo, "w") as f:
            json.dump(facturas, f, indent=4)

    @staticmethod
    def cargar_facturas(archivo="facturas.json"):
        try:
            with open(archivo, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []