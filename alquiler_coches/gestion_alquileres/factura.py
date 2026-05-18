from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gestion_alquileres import Alquiler
    
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

    def __init__(self, alquiler: Alquiler) -> None:
        """
        Metodo constructor
        """
        self.alquiler = alquiler
        self._total = 0.0

    @property
    def alquiler(self) -> Alquiler:
        return self._alquiler

    @alquiler.setter
    def alquiler(self, nuevo_alquiler) -> None:
        if not isinstance(nuevo_alquiler, Alquiler):
            raise ValueError("Debe ser un objeto de tipo Alquiler")
        self._alquiler = nuevo_alquiler

    @property
    def total(self) -> float:
        return self._total

    def generar_total(self) -> float:
        """
        Calcula el total de la factura
        """
        self._total = self.alquiler.calcular_total()
        return self._total

    def __str__(self) -> str:
        return (f"========== FACTURA ==========\n"
                f"{self.alquiler.reserva}\n"
                f"{self.alquiler.seguro}\n"
                f"Estado alquiler: {'Activo' if self.alquiler.activo else 'Finalizado'}\n"
                f"TOTAL: {self.total:.2f} €\n"
                f"============================\n")

    def guardar_factura_txt(self) -> str:
        """
        Guarda la factura en un fichero de texto.

        Returns
        -------
        str
            Nombre del archivo generado.
        """
        nombre_archivo = f"factura_{self.alquiler.reserva.id}.txt"

        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(str(self))

        return nombre_archivo
        