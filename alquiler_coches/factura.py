from alquiler import Alquiler

class Factura:
    """
        Clase Factura
            Representa la factura generada a partir de un alquiler.

        Atributos
        -----------------
        alquiler: Alquiler
            Alquiler asociado a la factura
        total: float
            Coste total de la factura

        Métodos
        -------------
        generar_total(self) -> float
            Calcula el total de la factura

        mostrar_factura(self) -> str
            Devuelve la información de la factura
    """

    def __init__(self, alquiler: Alquiler):
        """
        Metodo constructor
        """
        self.alquiler = alquiler
        self._total = 0.0

    @property
    def alquiler(self):
        return self._alquiler

    @alquiler.setter
    def alquiler(self, nuevo_alquiler):
        if not isinstance(nuevo_alquiler, Alquiler):
            raise ValueError("Debe ser un objeto de tipo Alquiler")
        self._alquiler = nuevo_alquiler

    @property
    def total(self):
        return self._total

    def generar_total(self):
        """
        Calcula el total de la factura
        """
        self._total = self.alquiler.calcular_total()
        return self._total

    def __str__(self):
        return (f"========== FACTURA ==========\n"
                f"{self.alquiler.reserva}\n"
                f"{self.alquiler.seguro}\n"
                f"Estado alquiler: {'Activo' if self.alquiler.activo else 'Finalizado'}\n"
                f"TOTAL: {self.total:.2f} €\n"
                f"============================\n")
        