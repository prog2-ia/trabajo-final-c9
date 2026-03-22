class Alquiler:
    """
        Clase Alquiler
            Representa el alquiler de un vehículo basado en una reserva.

        Atributos
        -----------------
        reserva: Reserva
            Reserva asociada al alquiler
        seguro: Seguro
            Seguro contratado
        activo: bool
            Indica si el alquiler está activo

        Métodos
        -------------
        calcular_total(self) -> float
            Calcula el coste total del alquiler

        finalizar(self) -> None
            Finaliza el alquiler
    """

    def __init__(self, reserva, seguro):
        self.reserva = reserva
        self.seguro = seguro
        self.activo = True

    @property
    def reserva(self):
        return self._reserva

    @reserva.setter
    def reserva(self, nueva_reserva):
        if nueva_reserva is None:
            raise ValueError("La reserva no puede ser None")
        self._reserva = nueva_reserva

    @property
    def seguro(self):
        return self._seguro

    @seguro.setter
    def seguro(self, nuevo_seguro):
        if nuevo_seguro is None:
            raise ValueError("El seguro no puede ser None")
        self._seguro = nuevo_seguro

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, nuevo: bool):
        if not isinstance(nuevo, bool):
            raise ValueError("El estado debe ser booleano")
        self._activo = nuevo

    def calcular_total(self):
        """
        Calcula el coste total del alquiler
        """
        dias = self.reserva.duracion()
        precio_vehiculo = self.reserva.vehiculo.tarifa.precio_base * dias
        precio_seguro = self.seguro.calcular_precio(dias)
        return precio_vehiculo + precio_seguro

    def finalizar(self):
        """
        Finaliza el alquiler
        """
        self._activo = False
        self.reserva._activa = False
        self.reserva.vehiculo.devolver()

    def __str__(self):
        estado = "Activo" if self.activo else "Finalizado"
        return (f"{self.reserva}\n"
                f"{self.seguro}\n"
                f"Estado: {estado}")