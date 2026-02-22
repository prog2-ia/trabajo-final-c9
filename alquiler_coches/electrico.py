#Atributos: puertas, estado, color, plazas, bateria, autonomia, tiempo_carga (hereda de Vehiculo)
#Métodos: usa los de Vehiculo, mostrar_info()

from vehiculo import Vehiculo


class Electrico(Vehiculo):
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

    def __init__(self, matricula, marca, modelo, precio_dia, color,
                 puertas, estado, plazas, bateria, autonomia, tiempo_carga):

        super().__init__(matricula, marca, modelo, precio_dia, color)

        self.puertas = puertas
        self.estado = estado
        self.plazas = plazas
        self.bateria = bateria
        self.autonomia = autonomia
        self.tiempo_carga = tiempo_carga

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

    @property
    def bateria(self):
        return self._bateria

    @bateria.setter
    def bateria(self, nuevo):
        if not isinstance(nuevo, (int, float)) or nuevo <= 0:
            raise ValueError("La batería debe ser positiva (kWh)")
        self._bateria = float(nuevo)

    @property
    def autonomia(self):
        return self._autonomia

    @autonomia.setter
    def autonomia(self, nuevo):
        if not isinstance(nuevo, int) or nuevo <= 0:
            raise ValueError("La autonomía debe ser positiva")
        self._autonomia = nuevo

    @property
    def tiempo_carga(self):
        return self._tiempo_carga

    @tiempo_carga.setter
    def tiempo_carga(self, nuevo):
        if not isinstance(nuevo, (int, float)) or nuevo <= 0:
            raise ValueError("El tiempo de carga debe ser positivo")
        self._tiempo_carga = float(nuevo)

    def __str__(self):
        info_padre = super().__str__()
        return (f"{info_padre}, "
                f"puertas: {self.puertas}, "
                f"estado: {self.estado}, "
                f"plazas: {self.plazas}, "
                f"batería: {self.bateria}kWh, "
                f"autonomía: {self.autonomia}km, "
                f"tiempo_carga: {self.tiempo_carga}h")