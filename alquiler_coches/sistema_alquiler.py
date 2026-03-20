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
    def __init__(self):
        self._clientes = []
        self._reservas = []
        self._alquileres = []
        self._inventario = Inventario()


    def registrar_cliente(self, cliente):
        self._clientes.append(cliente)

    def agregar_vehiculo(self, vehiculo):
        self._inventario.agregar_vehiculo(vehiculo)

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

        alquiler.finalizar()  # dentro debería llamar a vehiculo.devolver()

        return True

    def vehiculos_disponibles(self):
        return self._inventario.lista_disponible()

    def listar_clientes(self):
        return self._clientes

    def listar_reservas(self):
        return self._reservas

    def listar_alquileres(self):
        return self._alquileres

