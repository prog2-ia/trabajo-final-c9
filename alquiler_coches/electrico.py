from vehiculo import Vehiculo
from recargable import Recargable 

class Electrico(Vehiculo, Recargable):
    """
        Clase Electrico
            Representa un vehículo eléctrico. No utiliza combustible,
            sino batería recargable.

        Atributos
        -----------------
        puertas: int
            Número de puertas del vehículo
        estado: str
            Estado general del vehículo
        plazas: int
            Número de plazas disponibles
        bateria: float
            Capacidad de la batería en kWh
        autonomia: int
            Autonomía máxima en kilómetros
        tiempo_carga: float
            Tiempo estimado de carga completa en horas

        Métodos
        -------------
        __init__(...)
            Constructor del objeto

        __str__(self) -> str
            Devuelve la información completa del vehículo eléctrico
    """

    def __init__(self, matricula, marca, modelo, tarifa, color, puertas, estado, plazas, bateria, autonomia, tiempo_carga):

        Vehiculo.__init__(self, matricula, marca, modelo, tarifa, color)
        Recargable.__init__(self, bateria, autonomia, tiempo_carga)
        self.puertas = puertas
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
        info_padre = super().__str__()
        return (f"{info_padre}"
                f"Puertas: {self.puertas}\n"
                f"Estado: {self.estado}\n"
                f"Plazas: {self.plazas}\n"
                f"Batería: {self.bateria}kWh\n"
                f"Autonomía: {self.autonomia}km\n"
                f"Tiempo_carga: {self.tiempo_carga}h\n")