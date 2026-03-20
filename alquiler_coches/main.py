from cliente import Cliente
from turismo import Turismo
from electrico import Electrico
from furgoneta import Furgoneta
from tarifa import Tarifa
from reserva import Reserva
from seguro import Seguro
from alquiler import Alquiler
from factura import Factura
from sistema_alquiler import SistemaAlquiler
from datetime import date


# continue --> se mantiene en el bucle while
# break --> termina el programa


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
            nombre  = input("Nombre: ")
            dni = input("DNI: ")
            gmail = input("Gmail: ")
            fecha_nacimiento = date(input("Fecha nacieminto (yyyy/mm/dd): "))
            codigo_postal = int(input("Código Postal: "))
            telefono = int(input("Telefono: "))

            try:
                cliente = Cliente(nombre, dni, gmail, fecha_nacimiento, codigo_postal, telefono)
                sistema.registrar_cliente(cliente)
            except Exception as e:
                print("Error al registrar cliente:", e)

        elif opcion == "2":
            matricula = input("Matrícula: ")
            if not matricula.strip():
                print("Matrícula no válida")
                continue
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")

            try:
                precio_base = float(input("Precio base por día: "))
                precio_km = float(input("Precio por km: "))
                penalizacion = float(input("Penalización por retraso: "))
            except ValueError:
                print("Error: los precios deben ser números")
                continue

            try:
                tarifa = Tarifa(precio_base, precio_km, penalizacion)
                tipo = input("Tipo (turismo/furgoneta/electrico): ").lower()

                if tipo == "turismo":
                    vehiculo = Turismo(matricula, marca, modelo, tarifa, color)
                elif tipo == "furgoneta":
                    vehiculo = Furgoneta(matricula, marca, modelo, tarifa, color)
                elif tipo == "electrico":
                    vehiculo = Electrico(matricula, marca, modelo, tarifa, color)
                else:
                    print("Tipo no válido")
                    continue

                sistema.agregar_vehiculo(vehiculo)

                print("Vehículo añadido correctamente")

            except Exception as e:
                print("Error al añadir vehículo:", e)

        elif opcion == "3":
            matricula = input("Matrícula: ").strip()

            if not matricula:
                break
            print("Matrícula no válida")
            eliminado = sistema.eliminar_vehiculo(matricula)

            if eliminado:
                print("Vehículo eliminado correctamente")
            else:
                print("No se encontró un vehículo con esa matrícula")

        elif opcion == "4":
            clientes = sistema.listar_clientes()

            if not clientes:
                print("No hay clientes registrados")
                continue

            print("\nClientes:")
            for i, c in enumerate(clientes):
                print(f"{i}. {c.nombre} --> {c.dni}")

            try:
                indice_cliente_elegido = int(input("Selecciona cliente: "))
                cliente_elegido = clientes[indice_cliente_elegido]
            except Exception as e:
                print("Selección inválida")
                continue

            vehiculos = sistema.vehiculos_disponibles()

            if not vehiculos:
                print("No hay vehículos disponibles")
                continue
            print("\nVehiculos:")
            for i, v in enumerate(vehiculos):
                print(f"{i}. {v.matricula} - {v.marca} {v.modelo}")

            try:
                indice_vehiculo_elegido = int(input("Selecciona vehículo: "))
                vehiculo_elegido = vehiculos[indice_vehiculo_elegido]
            except:
                print("Selección inválida")
                continue

            try:
                fecha_inicio = date(input("Fecha inicio (yyyy/mm/dd): "))
                fecha_fin = date(input("Fecha fin (yyyy/mm/dd): "))
            except:
                print("Formato de fecha incorrecto")
                continue

            try:
                reserva = sistema.crear_reserva(cliente_elegido, vehiculo_elegido, fecha_inicio, fecha_fin)
                print("\nReserva creada correctamente")
                print(reserva)
            except Exception as e:
                print("Error al crear reserva:", e)
                
        elif opcion == "5":
            reservas = sistema.listar_reservas()

            if not reservas:
                print("No hay reservas registradas")
                continue

            print("\nReservas:")
            for r in reservas:
                print(f"ID: {r.id} | Cliente: {r.cliente.nombre} | Vehículo: {r.vehiculo.matricula}")

            try:
                id_reserva = int(input("Introduce el ID de la reserva a cancelar: "))
            except ValueError:
                print("ID inválido")
                continue

            for r in reservas:
                if r.id == id_reserva:
                    if sistema.cancelar_reserva(r):
                        print("Reserva cancelada correctamente")
                    else:
                        print("La reserva ya estaba cancelada")
                    break
            else:
                print("No se encontró la reserva")

        elif opcion == "6":
            reservas = sistema.reservas_activas()

            if not reservas:
                print("No hay reservas activas")
                continue

            print("\nReservas activas:")
            for r in reservas:
                print(f"ID: {r.id} | Cliente: {r.cliente.nombre} | Vehículo: {r.vehiculo.matricula}")

            try:
                id_reserva = int(input("Introduce el ID de la reserva: "))
            except ValueError:
                print("ID inválido")
                continue

            for r in reservas:
                if r.id == id_reserva:
                    try:
                        alquiler = sistema.iniciar_alquiler(r)
                        print("\nAlquiler iniciado correctamente")
                        print(alquiler)
                    except Exception as e:
                        print("Error:", e)
                    break
            else:
                print("No se encontró la reserva")





if __name__ == "__main__":
    main()






"""
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
"""

