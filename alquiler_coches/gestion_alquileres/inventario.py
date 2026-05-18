from vehiculos.vehiculo import Vehiculo

class Inventario:
    """
        Clase Inventario
            Gestiona los vehiculos del sistema

        Atributos
        -----------------
        vehiculos:
            Lista de vehiculos disponibles para alquilar

        Metodos:
        -------------
        __init__(self)
            Constructor del objeto.
        agregar_vehiculo(self, vehiculo):
            Agregar vehiculo al inventario
        eliminar_vehiculo(self, matricula):
            Eiminar un vehiculo de la lista de vehiculos disponibles
        lista_disponible(self):
            Lista de vehiculos disponibles para alquilar
        buscar_por_matriculs(self, matricula):
            Encontrar vehiculo por matricula

    """

    def __init__(self) -> None:
        self._vehiculos: list = []

        """
        Metodo constructor

        Parámetros:
        -----------------+
        vehiculos:
            Lista de vehiculos. Cada vehiculo es un objeto de la clase Vehiculo
        """

    @property
    def vehiculos(self) -> list:
        return self._vehiculos

    def agregar_vehiculo(self, vehiculo) -> None:
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError('Inventario necesita un objeto Vehiculo')
        self._vehiculos.append(vehiculo)

    def eliminar_vehiculo(self, matricula) -> bool:
        for vehiculo in self._vehiculos:
            if vehiculo.matricula == matricula:
                self._vehiculos.remove(vehiculo)
                return True
        return False

    def lista_disponible(self) -> list[Vehiculo]:
        vehiculos_disponibles = []
        for vehiculo in self._vehiculos:
            if vehiculo.disponible:
                vehiculos_disponibles.append(vehiculo)
        return vehiculos_disponibles

    def buscar_por_matricula(self, matricula) -> Vehiculo | None:
        vehiculo_encontrado = None
        for vehiculo in self._vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo_encontrado =  vehiculo
                break

        if vehiculo_encontrado is not None:
            return vehiculo_encontrado

        return None












