#Controla todo el sistema
#Atributos: clientes(lista), empleados(lista), reservas(lista), alquileres(lista), inventario(objeto inventario)
#Métodos: registrar_cliente(),
# crear_reserva(),
# iniciar_alquiler(),
# finalizar_alquiler(),

from inventario import Inventario
from reserva import Reserva
from alquiler import Alquiler

class SistemaAlquiler:
    """
        Clase SistemaAlquiler
            Controla todo el sistema

        Atributos
        -----------------
        clientes:
            Lista de clientes registrados
        reservas:
            Lista de las reservas que se han realizado
        alquileres:
            Lista de alquileres que se han realizado
        inventario:
            Inventario del sistema. Son los coches de los que disponemos

        Metodos:
        -------------
        __init__(self)
            Constructor del objeto.

        registrar_cliente(self, cliente):
            Añadimos a la lista de clientes a todos los clientes que se registren

        agregar_vehiculo(self, vehiculo):
            Agrega vehiculos al inventario

        eliminar_vehiculo(self, matricula):
            Elimina un vehiculo del inventario

        crear_reserva(self, cliente, vehiculo, fecha_inicio, fecha_fin):
            Crea una reserva

        cancelar_reserva(self, reserva):
            Cancela una reserva

        iniciar_alquiler(self, reserva):
            Inicia un alquiler

        finalizar_alquiler(self, alquiler):
            Finaliza un alquiler

        vehiculos_disponibles(self):
            Devuelve los vehiculos disponibes

        listar_clientes(self):
            Devuelve la lista de clientes

        listar_reservas(self):
            Devuelve la lista de reservas

        listar_alquileres(self):
            Devuelve la lista de alquileres
        """

    def __init__(self):
        self._clientes = []
        self._reservas = []
        self._alquileres = []
        self._inventario = Inventario()

        """
        Metodo constructor

        Parámetros:
        -----------------+
        clientes:
            Lista de clientes. Cada cliente es un objeto de la clase Cliente
        reservas:
            Lista de las reservas realizadas. Cada reserva es un objeto de la clase Reserva
        alquileres:
            Lista de los alquileres realizados. Cada alquiler es un objeto de la clase Alquileres
        inventario:
            Inventario del sistema. Objeto de la clase inventario que obtiene a lista de los vehiculos 
 
        """


    def registrar_cliente(self, cliente):
        for c in self._clientes:
            if c.dni == cliente.dni:
                raise ValueError("Ya existe un cliente con ese DNI")
        self._clientes.append(cliente)

    def agregar_vehiculo(self, vehiculo):
        for v in self._inventario.vehiculos:
            if v.matricula == vehiculo.matricula:
                raise ValueError("Ya existe un vehículo con esa matrícula")
        self._inventario.agregar_vehiculo(vehiculo)

    def eliminar_vehiculo(self, matricula):
        vehiculo = self._inventario.eliminar_vehiculo(matricula)

        if vehiculo and not vehiculo.disponible:
            raise ValueError("No se puede eliminar un vehiculo alquilado")

    def crear_reserva(self, cliente, vehiculo, fecha_inicio, fecha_fin):
        if not vehiculo.disponible:
            raise ValueError("El vehículo no está disponible")

        reserva = Reserva(cliente, vehiculo, fecha_inicio, fecha_fin)
        self._reservas.append(reserva)

        return reserva

    def cancelar_reserva(self, reserva):
        if reserva in self._reservas:
            return reserva.cancelar_reserva()

        return False

    def iniciar_alquiler(self, reserva):
        if not reserva.activa:
            raise ValueError("La reserva no está activa")

        vehiculo = reserva.vehiculo

        if not vehiculo.disponible:
            raise ValueError("El vehículo ya está alquilado")

        vehiculo.alquilar()

        alquiler = Alquiler(reserva)
        self._alquileres.append(alquiler)

        cliente = reserva.cliente
        cliente.anyadir_alquiler(alquiler)

        return alquiler

    def finalizar_alquiler(self, alquiler):
        if alquiler not in self._alquileres:
            return False
        alquiler.finalizar()

        return True

    def vehiculos_disponibles(self):
        return self._inventario.lista_disponible()

    def listar_clientes(self):
        return self._clientes

    def listar_reservas(self):
        return self._reservas

    def listar_alquileres(self):
        return self._alquileres

