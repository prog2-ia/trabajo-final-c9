from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import pickle

from .inventario import Inventario
from .reserva import Reserva
from .alquiler import Alquiler
from .factura import Factura
from personas.empleado import Empleado


if TYPE_CHECKING:
    from personas.cliente import Cliente
    from vehiculos.vehiculo import Vehiculo
    from gestion_alquileres.seguro import Seguro

class SistemaAlquiler:
    """
        Clase SistemaAlquiler
            Controla todo el sistema

        Atributos
        -----------------
        clientes:
            Lista de clientes registrados
        empleados: 
            Lista de empleados registrados
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

        buscar_vehiculos(self, tipo, plazas, combustible): 
            Busca un vehículo según lo que busque el cliente 

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
        
        registrar_empleado(self, empleado): 
            Añade un empleado al sistema
        
        eliminar_empleado(self, dni): 
            Elimina un empleado del sistema por su DNI 
        
        listar_empleados (self): 
            Devuelve la lista de empleados 
        """

    def __init__(self) -> None:
        self._clientes: list = []
        self._empleados:list[Empleado] =[]
        self._reservas: list[Reserva] = []
        self._alquileres: list[Alquiler] = []
        self._inventario: Inventario = Inventario()

    def registrar_cliente(self, cliente: Cliente) -> None:
        for c in self._clientes:
            if c.dni == cliente.dni:
                raise ValueError("Ya existe un cliente con ese DNI")
        self._clientes.append(cliente)

    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        for v in self._inventario.vehiculos:
            if v.matricula == vehiculo.matricula:
                raise ValueError("Ya existe un vehículo con esa matrícula")
        self._inventario.agregar_vehiculo(vehiculo)

    def eliminar_vehiculo(self, matricula: str) -> bool:
        vehiculo = self._inventario.buscar_por_matricula(matricula)
        if vehiculo is None:
            return False
        if not vehiculo.disponible:
            raise ValueError("No se puede eliminar un vehículo que está alquilado")
        return self._inventario.eliminar_vehiculo(matricula)
    
    def buscar_vehiculos(self, tipo=None, plazas=None, combustible=None) -> list:
        resultado = []
        for v in self._inventario.lista_disponible():
            if tipo and type(v).__name__.lower() != tipo:
                continue
            if plazas and v.plazas < plazas:
                continue
            if combustible and hasattr(v, 'combustible') and v.combustible != combustible:
                continue
            resultado.append(v)
        return resultado
    
    def crear_reserva(self, cliente: Cliente, vehiculo: Vehiculo, dias: int) -> Reserva:
        if not vehiculo.disponible:
            raise ValueError("El vehículo no está disponible")
        reserva = Reserva(cliente, vehiculo, dias)
        self._reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, reserva: Reserva) -> bool:
        if reserva in self._reservas:
            return reserva.cancelar_reserva()
        return False

    def iniciar_alquiler(self, reserva: Reserva, seguro: Seguro) -> Alquiler:
        if not reserva.activa:
            raise ValueError("La reserva no está activa")
 
        vehiculo = reserva.vehiculo
 
        if not vehiculo.disponible:
            raise ValueError("El vehículo ya está alquilado")
 
        vehiculo.alquilar()
 
        alquiler = Alquiler(reserva, seguro)
        self._alquileres.append(alquiler)
 
        cliente = reserva.cliente
        cliente.anyadir_vehiculo(alquiler)
 
        return alquiler

    def finalizar_alquiler(self, alquiler: Alquiler) -> Optional[Factura]:
        if alquiler not in self._alquileres:
            return None
        alquiler.finalizar()
        factura = Factura(alquiler)
        factura.generar_total()
        return factura

    def vehiculos_disponibles(self) -> list:
        return self._inventario.lista_disponible()

    def listar_clientes(self) -> list:
        return self._clientes

    def listar_reservas(self) -> list:
        return self._reservas

    def listar_alquileres(self) -> list:
        return self._alquileres
    
    def reservas_activas(self) -> list:
        return [r for r in self._reservas if r.activa]
    
    def registrar_empleado(self, empleado: Empleado) -> None:
        for e in self._empleados:
            if e.dni == empleado.dni:
                raise ValueError("Ya existe un empleado con ese DNI")
        self._empleados.append(empleado)
 
    def eliminar_empleado(self, dni: str) -> bool:
        for e in self._empleados:
            if e.dni == dni:
                self._empleados.remove(e)
                return True
        return False
 
    def listar_empleados(self) -> list:
        return self._empleados
    
    def guardar_sistema(self, archivo="sistema.dat") -> None:
        with open(archivo, "wb") as f:
            pickle.dump(self, f)
    
    @staticmethod
    def cargar_sistema(archivo="sistema.dat"):
        with open(archivo, "rb") as f:
            return pickle.load(f)