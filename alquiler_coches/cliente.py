#Atributos: nombre, dni, telefono, codigo_postal, email (heredados de persona), historial de alquileres
#Métodos: mostrar_info()


from persona import Persona
from alquiler import Alquiler

class Cliente(Persona):
    """
        Clase Cliente
            Representa al cliente de nuestro servicio de alguiler de vehiculos.
            Hereda las características generales de la clase Persona y añade algunas propias.

        Atributos
        -----------------
        historial:
            Lista del historial de las veces que el clinete alquiló un coche

        Metodos:
        -------------
        __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: str, codigo_postal: int, telefono: int)
            Constructor del objeto.

        anyadir_vehiculo(self, alquiler)
            Añadimos a la lista del historial del cliente un objeto Alquiler del alquiler del coche que escogio
    """


    def __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: str, codigo_postal: int, telefono: int):
        super().__init__(nombre, dni, gmail, fecha_nacimiento, codigo_postal, telefono)
        self._historial = []

        """
        Metodo constructor

        Parámetros:
        -----------------+
        historial: list
            Lista que contiene los alquileres que hizo cada persona 
        """

    @property
    def historial(self):
        return self._historial

    def anyadir_vehiculo(self, alquiler: Alquiler) -> None:  # alquiler es un objeto de Alquiler
        self._historial.append(alquiler)

    def __str__(self):
        info_padre = super().__str__()
        return  (f"{info_padre}"
            f"Historial: {len(self.historial)} alquileres")




