#Atributos: puertas, combustible, estado, color, plazas (hereda de Vehiculo)
#Métodos: usa los de Vehiculo, mostrar_info()

from vehiculo import Vehiculo

class Turismo(Vehiculo):
    """
        Clase Turismo
            Representa un vehículo tipo turismo destinado al transporte de personas.
            Hereda las características generales de Vehiculo y añade propiedades específicas.

        Atributos
        -----------------
        puertas: int
            Número de puertas del vehículo
        combustible: str
            Tipo de combustible (gasolina, diésel, eléctrico...)
        estado: str
            Estado general del vehículo
        plazas: int
            Número de plazas disponibles

        Métodos
        -------------
        __init__(...)
            Constructor del objeto

        __str__(self) -> str
            Devuelve la información completa del turismo
    """

    def __init__(self, matricula, marca, modelo, precio_dia, color, puertas, combustible, estado, plazas):
        """
        Metodo constructor
        """
        super().__init__(matricula, marca, modelo, precio_dia, color)

        self.puertas = puertas
        self.combustible = combustible
        self.estado = estado
        self.plazas = plazas

    @property
    def puertas(self):
        return self._puertas

    @puertas.setter
    def puertas(self, nuevo):
        if not isinstance(nuevo, int) or nuevo <= 0:
            raise ValueError("El número de puertas debe ser positivo")
        self._puertas = nuevo

    @property
    def combustible(self):
        return self._combustible

    @combustible.setter
    def combustible(self, nuevo):
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El combustible no puede estar vacío")
        self._combustible = nuevo.strip().lower()

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo):
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El estado no puede estar vacío")
        self._estado = nuevo.strip()

    @property
    def plazas(self):
        return self._plazas

    @plazas.setter
    def plazas(self, nuevo):
        if not isinstance(nuevo, int) or nuevo <= 0:
            raise ValueError("El número de plazas debe ser positivo")
        self._plazas = nuevo

    def __str__(self):
        """
        Devuelve una representación legible del turismo
        """
        info_padre = super().__str__()
        return (f"{info_padre}"
                f"Puertas: {self.puertas}"
                f"Combustible: {self.combustible}"
                f"Estado: {self.estado}"
                f"Plazas: {self.plazas}")