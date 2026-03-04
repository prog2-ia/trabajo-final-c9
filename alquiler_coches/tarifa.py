#precio base, precio km, penalizacion_retraso 
#mostrar_info() eso se hace en vehiculo


class Tarifa:
    """
        Clase Tarifa
            Representa la politica de precios asociada al coche que quiere alquilar el cliente

        Atributos
        -----------------
        precio_base:
            Precio base del vehiculo, lo mínimo que pagas por usarlo
        precio_km:
            Precio por km. Cuantos más km hagas, más aumentará el precio
        penalizacion_retraso:
            Penalizacion por entregar el coche con retraso. Si lo entregas tarde el precio final aumenta

        Metodos:
        -------------
        __init__(self, precio_base: float, precio_km: float, penalizacion_retraso: float)
            Constructor del objeto.

        calcular_precio(self, dias: int, kilometros: int, retraso=False) -> float
            Calcula el precio total del alquiler del vehiculo
        """

    def __init__(self, precio_base: float, precio_km: float, penalizacion_retraso: float):
        self.precio_base = precio_base
        self.precio_km = precio_km
        self.penalizacion_retraso = penalizacion_retraso

        """
        Metodo constructor

        Parámetros:
        -----------------+
        precio_base:
            Precio inicial del vehiculo 
        precio_km:
            Precio por cada km
        penalizacion_retraso:
            Precio por la pensalización por retraso
        """

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio base debe ser positivo")
        self._precio_base = float(nuevo_precio)

    @property
    def precio_km(self):
        return self._precio_km

    @precio_km.setter
    def precio_km(self, nuevo):
        if not isinstance(nuevo, (int, float)) or nuevo < 0:
            raise ValueError("El precio por km no puede ser negativo.")
        self._precio_km = float(nuevo)

    @property
    def penalizacion_retraso(self):
        return self._penalizacion_retraso

    @penalizacion_retraso.setter
    def penalizacion_retraso(self, nuevo):
        if not isinstance(nuevo, (int, float)) or nuevo < 0:
            raise ValueError("La penalización no puede ser negativa.")
        self._penalizacion_retraso = float(nuevo)

    def calcular_precio(self, dias: int, kilometros: int, retraso=False) -> float:
        total = (self.precio_base * dias) + (self.precio_km * kilometros)
        if retraso:
            total += self.penalizacion_retraso
        return total

    def __str__(self):
        return (f"Tarifa -> Precio base: {self.precio_base}€/día, "
                f"Precio por km: {self.precio_km}€, "
                f"Penalización: {self.penalizacion_retraso}€")

