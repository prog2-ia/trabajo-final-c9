from alquiler_coches.sistema_alquiler import SistemaAlquiler
from cliente import Cliente
from turismo import Turismo
from tarifa import Tarifa
from reserva import Reserva
from seguro import Seguro
from alquiler import Alquiler
from factura import Factura
from sistema_alquiler import SistemaAlquiler
from datetime import date



def main():
    sistema = SistemaAlquiler()

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar cliente")
        print("2. Añadir vehículo")
        print("3. Eliminar vehiculo")
        print("4. Crear reserva")
        print("5. Cancelar reserva")
        print("6. Iniciar alquiler")
        print("7. Finalizar alquiler")
        print("8. Ver vehiculos disponibles")
        print("9. Ver inventario")
        print("10. Ver reservas")
        print("11. Ver clientes")
        print("12. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":


def main():
    print("=== SISTEMA DE ALQUILER ===\n")
    cliente = Cliente("Victoria", "12345678A", "correo@gmail.com", "01/01/2006", 46000, 123456789)
    tarifa = Tarifa(precio_base=30, precio_km=0.5, penalizacion_retraso=50)
    coche = Turismo("1234ABC", "Toyota", "Corolla", tarifa, "Rojo", 5, "gasolina", "nuevo", 5)
    seguro = Seguro("Premium", 10, {"daños": True, "robo": True})
    reserva = Reserva(cliente, coche, date(2026, 3, 20), date(2026, 3, 25))
    print(reserva)
    alquiler = Alquiler(reserva, seguro, True)
    coche.alquilar()
    total = alquiler.calcular_total()
    print(f"\nTotal alquiler: {total:.2f} €")
    factura = Factura(alquiler)
    factura.generar_total()
    print(factura)
    cliente.anyadir_vehiculo(alquiler)
    print("\n--- CLIENTE ---")
    print(cliente)

if __name__ == "__main__":
    main()

