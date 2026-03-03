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




# CLASE VEHICULO


#Atributos: matricula, marca, modelo, precio_dia, disponible (booleano), color
#Métodos: alquilar(), devolver(), mostrar_info()
#Debería de ser abstracta(COMENTAR CON MARIA)
from abc import ABC
from tarifa import Tarifa

class Vehiculo(ABC):
    """
        Clase Vehiculo
            Representa un vehículo que puede ser alquilado dentro del sistema.
            Controla su identificación, características y estado de disponibilidad.

        Atributos
        -----------------
        matricula: str
            Identificador único del vehículo
        marca: str
            Marca del vehículo
        modelo: str
            Modelo del vehículo
        precio_dia: float
            Coste diario de alquiler del vehículo
        color: str
            Color del vehículo
        disponible: bool
            Indica si el vehículo puede alquilarse

        Métodos
        -------------
        __init__(self, matricula: str, marca: str, modelo: str, precio_dia: float, color: str) -> None
            Constructor del objeto

        alquilar(self) -> bool
            Cambia el estado a no disponible si el vehículo puede alquilarse

        devolver(self) -> bool
            Cambia el estado a disponible si el vehículo estaba alquilado

        __str__(self) -> str
            Devuelve la información del vehículo en formato legible
    """

    def __init__(self, matricula: str, marca: str, modelo: str, tarifa: Tarifa, color: str):
        """
        Metodo constructor

        Parámetros
        -----------------
        matricula: str
            Identificador único del vehículo
        marca: str
            Marca del vehículo
        modelo: str
            Modelo del vehículo
        precio_dia: float
            Precio diario del alquiler (mayor que 0)
        color: str
            Color del vehículo
        """
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.tarifa = tarifa
        self.color = color
        self._disponible = True

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, nuevo):
        """
        Establece la matrícula validando que no esté vacía
        """
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("La matrícula no puede estar vacía")
        self._matricula = nuevo.strip().upper()

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nuevo):
        """
        Establece la marca validando que no esté vacía
        """
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("La marca no puede estar vacía")
        self._marca = nuevo.strip()

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo):
        """
        Establece el modelo validando que no esté vacío
        """
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El modelo no puede estar vacío")
        self._modelo = nuevo.strip()

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, nueva_tarifa: Tarifa):
        if not isinstance(nueva_tarifa, Tarifa):
            raise ValueError("Debe ser una instancia de Tarifa")
        self._tarifa = nueva_tarifa

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo):
        """
        Establece el color validando que no esté vacío
        """
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El color no puede estar vacío")
        self._color = nuevo.strip()

    @property
    def disponible(self):
        return self._disponible

    def alquilar(self):
        """
        Intenta alquilar el vehículo

        Retorno
        -----------------
        bool
            True si el vehículo pasa a estar alquilado
            False si ya estaba alquilado
        """
        if not self._disponible:
            return False
        self._disponible = False
        return True

    def devolver(self):
        """
        Devuelve el vehículo al sistema

        Retorno
        -----------------
        bool
            True si el vehículo pasa a estar disponible
            False si ya lo estaba
        """
        if self._disponible:
            return False
        self._disponible = True
        return True

    def __str__(self):
        """
        Devuelve una representación legible del vehículo
        """
        estado = "Disponible" if self.disponible else "Alquilado"
        return (f"Matrícula: {self.matricula}"
                f"Marca: {self.marca}"
                f"Modelo: {self.modelo}"
                f"Estado: {estado}"
                f"Color: {self.color}"
                f"{self.tarifa}")