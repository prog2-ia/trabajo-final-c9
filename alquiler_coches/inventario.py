#Atributos: vehículos(lista)
#Métodos: agregar_vehiculo(), eliminar_vehiculo(), buscar_disponible(), listar()


# QUIERO UN METODO DONDE TENGA UNA LISTA DE VEHICULOS A ALQUILAR,
# Y SE SEPARE COMO EN DOS SECCIONES: DISPONIBLES Y NO DISPONIBLES
# Y QUE NO ELIMIE LOS COCHES, SOLO QUE LOS PONGA COMO NO DISPONIBLES
# Y QUE SE VUELVAN A PONER COMO DISPONIBLES CUANDO TOQUE

from alquiler_coches.vehiculo import Vehiculo


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

    def __init__(self):
        self._vehiculos = []

        """
        Metodo constructor

        Parámetros:
        -----------------+
        vehiculos:
            Lista de vehiculos. Cada vehiculo es un objeto de la clase Vehiculo
        """

    @property
    def vehiculos(self):
        return self._vehiculos

    def agregar_vehiculo(self, vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError('Inventario necesita un objeto Vehiculo')
        self._vehiculos.append(vehiculo)

    def eliminar_vehiculo(self, matricula):
        for vehiculo in self._vehiculos:
            if vehiculo.matricula == matricula:
                self._vehiculos.remove(vehiculo)
                return True
        return False

    def lista_disponible(self):
        vehiculos_disponibles = []
        for vehiculo in self._vehiculos:
            if vehiculo.disponible:
                vehiculos_disponibles.append(vehiculo)
        return vehiculos_disponibles

    def buscar_por_matriculs(self, matricula):
        vehiculo_encontrado = None
        for vehiculo in self._vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo_encontrado =  vehiculo
                break

        if vehiculo_encontrado is not None:
            return vehiculo_encontrado

        return False









