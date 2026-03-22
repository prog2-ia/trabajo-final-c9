from cliente import Cliente
from turismo import Turismo
from electrico import Electrico
from furgoneta import Furgoneta
from tarifa import Tarifa
from seguro import Seguro
from sistema_alquiler import SistemaAlquiler
from empleado import Empleado

def main():
    sistema = SistemaAlquiler()

    # Catálogo por defecto
    t1 = Tarifa(50.0, 0.20, 30.0)
    t2 = Tarifa(80.0, 0.30, 50.0)
    t3 = Tarifa(60.0, 0.10, 25.0)
    t4 = Tarifa(45.0, 0.15, 20.0)
    t5 = Tarifa(70.0, 0.25, 40.0)
    sistema.agregar_vehiculo(Turismo("1234ABC", "Seat", "Ibiza", t1, "Rojo", 5, "gasolina", "Bueno", 5))
    sistema.agregar_vehiculo(Turismo("5678DEF", "Toyota", "Corolla", t1, "Blanco", 4, "gasolina", "Excelente", 5))
    sistema.agregar_vehiculo(Furgoneta("9012GHI", "Mercedes", "Sprinter", t2, "Blanco", 3, "diesel", "Bueno", 9))
    sistema.agregar_vehiculo(Electrico("3456JKL", "Tesla", "Model 3", t3, "Negro", 4, "Nuevo", 5, 75.0, 500, 8.0))
    sistema.agregar_vehiculo(Turismo("7890MNO", "Volkswagen", "Golf", t4, "Gris", 4, "diesel", "Excelente", 5))
    sistema.agregar_vehiculo(Furgoneta("2345PQR", "Ford", "Transit", t5, "Blanco", 3, "diesel", "Bueno", 8))
    sistema.agregar_vehiculo(Electrico("6789STU", "Peugeot", "e-208", t3, "Azul", 4, "Nuevo", 5, 50.0, 340, 7.5))
    sistema.agregar_vehiculo(Turismo("1122VWX", "BMW", "Serie 1", t5, "Negro", 4, "gasolina", "Excelente", 5))
    sistema.registrar_cliente(Cliente("María García", "12345678A", "maria@gmail.com", "15/05/1990", "46000", "600111222"))
    sistema.registrar_cliente(Cliente("Carlos López", "87654321B", "carlos@gmail.com", "22/03/1985", "28001", "611333444"))
    sistema.registrar_cliente(Cliente("Laura Martínez", "11223344C", "laura@gmail.com", "07/09/1995", "08001", "622555666"))
    
    while True:
        print("\n--- MENÚ PRINCIPAL---")
        print("1. Registrar cliente")
        print("2. Añadir vehículo")
        print("3. Eliminar vehículo")
        print("4. Crear reserva")
        print("5. Cancelar reserva")
        print("6. Iniciar alquiler")
        print("7. Finalizar alquiler")
        print("8. Ver vehiculos disponibles")
        print("9. Ver inventario completo")
        print("10. Ver reservas")
        print("11. Ver clientes")
        print("12. Gestionar empleados")
        print("13. Ver ingresos totales")
        print("14. Salir")

        opcion = input("Elige una opción: ").strip()
        print()

        # 1. REGISTRAR CLIENTE 
        if opcion == "1":
            nombre  = input("Nombre: ").strip()
            dni = input("DNI: ").strip()
            gmail = input("Gmail: ").strip()
            fecha_nacimiento = input("Fecha de nacimiento: ")
            codigo_postal = input("Código Postal: ")
            telefono = input("Telefono: ")
            try:
                cliente = Cliente(nombre, dni, gmail, fecha_nacimiento, codigo_postal, telefono)
                sistema.registrar_cliente(cliente)
                print(f"Cliente {nombre} registrado completamente")
            except Exception as e:
                print("Error al registrar cliente:", e)

        # 2. AÑADIR VEHÍCULO 
        elif opcion == "2":
            matricula = input("Matrícula: ").strip()
            if not matricula:
                print("Matrícula no válida")
                continue
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            color = input("Color: ").strip()
            try:
                precio_base = float(input("Precio base por día: "))
                precio_km = float(input("Precio por km: "))
                penalizacion = float(input("Penalización por retraso: "))
            except ValueError:
                print("Error: los precios deben ser números")
                continue
            try:
                tarifa = Tarifa(precio_base, precio_km, penalizacion)
                tipo = input("Tipo (turismo/furgoneta/eléctrico): ").strip().lower()
                if tipo == "turismo":
                    puertas = int(input("Puertas: "))
                    combustible = input("Combustible: ").strip()
                    estado = input("Estado: ").strip()
                    plazas = int(input("Plazas: "))
                    vehiculo = Turismo(matricula, marca, modelo, tarifa, color, puertas, combustible, estado, plazas)
                elif tipo == "furgoneta":
                    puertas = int(input("Puertas: "))
                    combustible = input("Combustible: ").strip()
                    estado = input("Estado: ").strip()
                    plazas = int(input("Plazas: "))
                    vehiculo = Furgoneta(matricula, marca, modelo, tarifa, color, puertas, combustible, estado, plazas)
                elif tipo == "electrico":
                    puertas = int(input("Puertas: "))
                    estado = input("Estado: ").strip()
                    plazas = int(input("Plazas: "))
                    bateria = float(input("Batería (kWh): "))
                    autonomia = int(input("Autonomía (km): "))
                    tiempo_carga = float(input("Tiempo de carga (horas): "))
                    vehiculo = Electrico(matricula, marca, modelo, tarifa, color, puertas, estado, plazas, bateria, autonomia, tiempo_carga)
                else:
                    print("Tipo no válido")
                    continue
                sistema.agregar_vehiculo(vehiculo)
                print("Vehículo añadido correctamente")
            except Exception as e:
                print("Error al añadir vehículo:", e)

        # 3. ELIMINAR VEHÍCULO 
        elif opcion == "3":
            matricula = input("Matrícula: ").strip()
            if not matricula:
                print("Matrícula no válida")
                continue
            try:
                eliminado = sistema.eliminar_vehiculo(matricula)
                if eliminado:
                    print("Vehículo eliminado correctamente")
                else:
                    print("No se encontró un vehículo con esa matrícula")
            except ValueError as e: 
                print("Error al eliminar vehículo: ", e)

        # 4. CREAR RESERVA
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
            print("\nFiltrar vehículos (Enter para saltar filtro):")
            tipo = input("Tipo (turismo/furgoneta/electrico): ").strip().lower() or None
            plazas = input("Plazas mínimas: ").strip()
            plazas = int(plazas) if plazas else None
            if tipo in ("turismo", "furgoneta"): 
                combustible = input("Combustible (gasolina/diesel): ").strip().lower() or None
            else: 
                combustible=None 
            vehiculos = sistema.buscar_vehiculos(tipo, plazas, combustible)
            if not vehiculos:
                print("No hay vehículos disponibles")
                continue
            print("\nVehículos disponibles:")
            for i, v in enumerate(vehiculos):
                print(f"{i}. {v.marca} {v.modelo} - {type(v).__name__} - {v.tarifa.precio_base}€/día - {v.color} - {v.plazas} plazas")
            try:
                indice_vehiculo_elegido = int(input("Selecciona vehículo: "))
                vehiculo_elegido = vehiculos[indice_vehiculo_elegido]
            except:
                print("Selección inválida")
                continue
            try:
                dias=int(input("Número de días: "))
                reserva = sistema.crear_reserva(cliente_elegido, vehiculo_elegido, dias)
                print("\nReserva creada correctamente")
                print(reserva)
            except Exception as e:
                print("Error al crear reserva:", e)
        
        # 5. CANCELAR RESERVA 
        elif opcion == "5":
            reservas = [r for r in sistema.listar_reservas() if r.activa]
            if not reservas:
                print("No hay reservas activas")
                continue
            print("\nReservas activas:")
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

        # 6. INICIAR ALQUILER 
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
                    print("\nTipos de seguro:")
                    print("1. Básico (5€/día)")
                    print("2. Estándar (10€/día)")
                    print("3. Todo riesgo (20€/día)")
                    opcion_seguro=input("Elige seguro (1/2/3): ").strip()
                    if opcion_seguro == "1":
                        seguro = Seguro("Básico", 5.0, {"responsabilidad_civil": True})
                    elif opcion_seguro == "2":
                        seguro = Seguro("Estándar", 10.0, {"responsabilidad_civil": True, "robo": True})
                    elif opcion_seguro == "3":
                        seguro = Seguro("Todo Riesgo", 20.0, {"responsabilidad_civil": True, "robo": True, "daños_propios": True})
                    else:
                        print("Opción no válida, se asigna Básico por defecto")
                        seguro = Seguro("Básico", 5.0, {"responsabilidad_civil": True})
                    try:
                        alquiler = sistema.iniciar_alquiler(r, seguro)
                        print("\nAlquiler iniciado correctamente")
                        print(alquiler)
                        if isinstance(r.vehiculo, Electrico): 
                            print("\nVehículo eléctrico detectado: ")
                            r.vehiculo.recargar()
                    except Exception as e:
                        print("Error:", e)
                    break
            else:
                print("No se encontró la reserva")

        # 7. FINALIZAR ALQUILER 
        elif opcion == "7":
            alquileres = [a for a in sistema.listar_alquileres() if a.activo]
            if not alquileres:
                print("No hay alquileres activos")
                continue
            print("\nAlquileres activos:")
            for i, a in enumerate(alquileres):
                print(f"{i}. Cliente: {a.reserva.cliente.nombre} | Vehículo: {a.reserva.vehiculo.matricula}")
            try:
                indice = int(input("Selecciona alquiler: "))
                alquiler_elegido = alquileres[indice]
            except (ValueError, IndexError):
                print("Selección inválida")
                continue
            factura = sistema.finalizar_alquiler(alquiler_elegido)
            print("\nAlquiler finalizado. Factura:")
            print(factura)

        # 8. VER VEHÍCULOS DISPONIBLES 
        elif opcion == "8":
            disponibles = sistema.vehiculos_disponibles()
            if not disponibles:
                print("No hay vehículos disponibles")
            else:
                for i, v in enumerate(disponibles):
                    print(f"VEHÍCULO {i+1}")
                    print(v)

        # 9. VER INVENTARIO COMPLETO
        elif opcion == "9":
            todos = sistema._inventario.vehiculos
            if not todos:
                print("El inventario está vacío")
            else:
                for i, v in enumerate(todos):
                    print(f"VEHÍCULO {i+1}")
                    print(v)

        # 10. VER RESERVAS 
        elif opcion == "10":
            reservas = sistema.listar_reservas()
            if not reservas:
                print("No hay reservas registradas")
            else:
                for r in reservas:
                    print(r)

        # 11. VER CLIENTES 
        elif opcion == "11":
            clientes = sistema.listar_clientes()
            if not clientes:
                print("No hay clientes registrados")
            else:
                for c in clientes:
                    print(c)
        
        # 12. GESTIONAR EMPLEADOS
        elif opcion == "12":
            print("\n--- GESTIÓN DE EMPLEADOS ---")
            print("1. Registrar empleado")
            print("2. Eliminar empleado")
            print("3. Ver empleados")
            opcion_empleado = input("Elige una opción: ").strip()

            if opcion_empleado == "1":
                nombre = input("Nombre: ").strip()
                dni = input("DNI: ").strip()
                gmail = input("Gmail: ").strip()
                fecha_nacimiento = input("Fecha de nacimiento: ")
                codigo_postal = input("Código Postal: ")
                telefono = input("Teléfono: ")
                id_empleado = int(input("ID empleado: "))
                print("Puestos disponibles: gerente, administrativo, mecanico")
                puesto = input("Puesto: ").strip()
                sueldo = float(input("Sueldo: "))
                try:
                    empleado = Empleado(nombre, dni, gmail, fecha_nacimiento, codigo_postal, telefono, id_empleado, puesto, sueldo)
                    sistema.registrar_empleado(empleado)
                    print(f"Empleado '{nombre}' registrado correctamente")
                except Exception as e:
                    print("Error:", e)

            elif opcion_empleado == "2":
                dni = input("DNI del empleado a eliminar: ").strip()
                if sistema.eliminar_empleado(dni):
                    print("Empleado eliminado correctamente")
                else:
                    print("No se encontró un empleado con ese DNI")

            elif opcion_empleado == "3":
                empleados = sistema.listar_empleados()
                if not empleados:
                    print("No hay empleados registrados")
                else:
                    for e in empleados:
                        print(e)

        # 13. VER INGRESOS TOTALES
        elif opcion == "13":
            alquileres = sistema.listar_alquileres()
            finalizados = [a for a in alquileres if not a.activo]
            if not finalizados:
                print("No hay alquileres finalizados")
            else:
                total = 0
                print("\n--- INGRESOS ---")
                for a in finalizados:
                    subtotal = a.calcular_total()
                    total += subtotal
                    print(f"Cliente: {a.reserva.cliente.nombre} | Vehículo: {a.reserva.vehiculo.matricula} | {subtotal:.2f} €")
                print(f"\nTOTAL INGRESOS: {total:.2f} €")
        
        # 14. SALIR 
        elif opcion == "14":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()