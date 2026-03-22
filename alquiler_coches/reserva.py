from cliente import Cliente
from vehiculo import Vehiculo

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
        dias: 
            Número de días del alquiler 
        activa:
            Indica si la reserva está activa

        Metodos:
        -------------
        __init__(self, cliente: Cliente, vehiculo: Vehiculo, dias)
            Constructor del objeto.

        cancelar_reserva(self):
            Cancelamos la reserva y indicamos el atributo ativa como falso

        duracion(self):
            Indica la duración total de la reserva en días
    """
    contador = 0

    def __init__(self, cliente: Cliente, vehiculo: Vehiculo, dias): 
        """
        Metodo constructor

        Parámetros
        -----------------

        cliente:
            Objeto de la clase cliente
        vehiculo:
            Objeto de la clase Vehiculo
        dias: 
            Cantidad de dias del alquiler
        activa:
            Atributo booleano que indica si la reserva está activa o no
        """
        self.cliente = cliente
        self.vehiculo = vehiculo
        self._dias = dias 
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
    def activa(self):
        return self._activa

    @property
    def id(self):
        return self._id
    
    def duracion(self): 
        return self._dias 
    
    def cancelar_reserva(self):
        """
        Si la reserva es False, devolvemos False porque la reserva ya estaba cancelada
        Del otro modo, si la reserva es True, la ponemos como False y devolvemos True. La reserva ha sido cancelada
        """
        if not self._activa:
            return False
        self._activa = False
        return True

    def __str__(self):
        estado = "Activa" if self._activa else "Cancelada"
        return (f"--- RESERVA ---\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Vehículo: {self.vehiculo.matricula}\n"
                f"Días: {self._dias}\n"
                f"Estado: {estado}\n"
                f"Id: {self.id}")




