#Cliente+vehículo antes del alquiler
#Atributos: cliente, vehículo, días, activa(True/False)
#Métodos: confirmar(), cancelar()

from cliente import Cliente
from vehiculo import Vehiculo
from datetime import date


class Reserva:
    """
        Clase Reserva
            Define la reserva que hizo el cliente especificando las fechas y el vehiculo elegido.

        Atributos
        -----------------
        cliente:
            Cliente que hizo la reserva
        vehiculo:
            Vehiculo que alquilará el cliente
        fecha_inicio:
            Fecha de inicio del alquiler
        fecha_fin:
            Fecha de finalización del alquiler
        activa:
            Indica si la reserva está activa

        Metodos:
        -------------
        __init__(self, cliente: Cliente, vehiculo: Vehiculo, fecha_inicio: date, fecha_fin: date)
            Constructor del objeto.

        cancelae_reserva(self):
            Cancelamos la reserva y indicamos el atributo ativa como falso

        duracion(self):
            Indica la duración total de la reserva en días
    """

    contador = 0
    def __init__(self, cliente: Cliente, vehiculo: Vehiculo, fecha_inicio: date, fecha_fin: date):
        """
        Metodo constructor

        Parámetros
        -----------------
        cliente:
            Objeto de la clase cliente
        vehiculo:
            Objeto de la clase Vehiculo
        fecha_inicio:
            Fecha de inicio en formato date (yyyy/mm/dd)
        fecha_fin:
            Fecha de fin en formato date (yyyy/mm/dd)
        activa:
            Atributo booleano que indica si la reserva está activa o no
        """

        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self._activa = True
        self._id = Reserva.contador
        Reserva.contador += 1


    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, nuevo_cliente):
        if not isinstance(nuevo_cliente, Cliente):
            raise ValueError("Cliente debe ser un objeto de Cliente")
        self._cliente = nuevo_cliente

    @property
    def vehiculo(self):
        return self._vehiculo

    @vehiculo.setter
    def vehiculo(self, nuevo_vehiculo):
        if not isinstance(nuevo_vehiculo, Vehiculo):
            raise ValueError("Vehiculo debe ser un objeto de Vehiculo")
        self._vehiculo = nuevo_vehiculo

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        if not isinstance(fecha_inicio, date):
            raise ValueError("La fecha de inicio será un objeto date")
        self._fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        if not isinstance(fecha_fin, date):
            raise ValueError("La fecha de fin será un objeto date")
        if fecha_fin <= self.fecha_inicio:
            raise ValueError("La fecha de fin debe ser posterior a la de inicio")
        self._fecha_fin = fecha_fin

    @property
    def activa(self):
        return self._activa

    @property
    def id(self):
        return self._id

    def cancelae_reserva(self):
        """
        Si la reserva es False, devolvemos False porque la reserva ya estaba cancelada
        Del otro modo, si la reserva es True, la ponemos como False y devolvemos True. La reserva ha sido cancelada
        """
        if not self._activa:
            return False
        self._activa = False
        return True

    def duracion(self):
        return (self.fecha_fin - self.fecha_inicio).days

    def __str__(self):
        estado = "Activa" if self._activa else "Cancelada"
        return (f"--- RESERVA ---\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Vehículo: {self.vehiculo.matricula}\n"
                f"Inicio: {self.fecha_inicio.strftime('%d/%m/%Y')}\n"
                f"Fin: {self.fecha_fin.strftime('%d/%m/%Y')}\n"
                f"Estado: {estado}\n"
                f"Id: {self.id}")




