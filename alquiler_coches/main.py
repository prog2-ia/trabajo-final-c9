from cliente import Cliente
from turismo import Turismo
from tarifa import Tarifa
from reserva import Reserva
from seguro import Seguro
from alquiler import Alquiler
from factura import Factura
from datetime import date


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

