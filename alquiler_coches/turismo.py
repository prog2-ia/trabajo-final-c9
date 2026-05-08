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

    def __init__(self, matricula: str, marca: str, modelo: str, precio_dia, color: str, puertas: int, combustible: str, estado: str, plazas: int):
        """
        Metodo constructor
        """
        super().__init__(matricula, marca, modelo, precio_dia, color)

        self.puertas = puertas
        self.combustible = combustible
        self.estado = estado
        self.plazas = plazas

    @property
    def puertas(self) -> int:
        return self._puertas

    @puertas.setter
    def puertas(self, nuevo: int) -> None:
        if not isinstance(nuevo, int) or nuevo <= 0:
            raise ValueError("El número de puertas debe ser positivo")
        self._puertas = nuevo

    @property
    def combustible(self) -> str:
        return self._combustible

    @combustible.setter
    def combustible(self, nuevo: str) -> None:
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El combustible no puede estar vacío")
        self._combustible = nuevo.strip().lower()

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, nuevo) -> None:
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El estado no puede estar vacío")
        self._estado = nuevo.strip()

    @property
    def plazas(self) -> int:
        return self._plazas

    @plazas.setter
    def plazas(self, nuevo: int) -> None:
        if not isinstance(nuevo, int) or nuevo <= 0:
            raise ValueError("El número de plazas debe ser positivo")
        self._plazas = nuevo

    def __str__(self) -> str:
        """
        Devuelve una representación legible del turismo
        """
        info_padre = super().__str__()
        return (f"{info_padre}"
                f"Puertas: {self.puertas}\n"
                f"Combustible: {self.combustible}\n"
                f"Estado: {self.estado}\n"
                f"Plazas: {self.plazas}\n")