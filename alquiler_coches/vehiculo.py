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
        tarifa: float
            Objeto de la clase Tarifa
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
        tarifa: Tarifa
            Tarifa del coche a alquilar
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
        """
        Establece que la tarifa obtenida ser un objeto de la clase Tarifa
        """
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
