"""
TEST COMPLETO DEL SISTEMA DE ALQUILER
Prueba todas las clases y sus métodos
"""

from datetime import date
from tarifa import Tarifa
from turismo import Turismo
from furgoneta import Furgoneta
from electrico import Electrico
from cliente import Cliente
from empleado import Empleado
from reserva import Reserva
from seguro import Seguro
from alquiler import Alquiler
from factura import Factura
from inventario import Inventario
from sistema_alquiler import SistemaAlquiler

OK   = "  ✅ OK"
FAIL = "  ❌ FALLO"

def check(descripcion, condicion):
    estado = OK if condicion else FAIL
    print(f"{estado} — {descripcion}")
    return condicion

def check_excepcion(descripcion, fn):
    try:
        fn()
        print(f"{FAIL} — {descripcion} (no lanzó excepción)")
        return False
    except Exception as e:
        print(f"{OK} — {descripcion} → {type(e).__name__}: {e}")
        return True

errores = 0

# ══════════════════════════════════════════════════════
print("\n══════ TARIFA ══════")
# ══════════════════════════════════════════════════════
t = Tarifa(50.0, 0.20, 30.0)
if not check("Crear Tarifa válida", t.precio_base == 50.0 and t.precio_km == 0.20 and t.penalizacion_retraso == 30.0): errores += 1
if not check("calcular_precio sin retraso (5 días, 100 km)", t.calcular_precio(5, 100) == 270.0): errores += 1
if not check("calcular_precio con retraso",               t.calcular_precio(5, 100, retraso=True) == 300.0): errores += 1
if not check_excepcion("precio_base negativo",   lambda: Tarifa(-1, 0.2, 10)): errores += 1
if not check_excepcion("precio_km negativo",     lambda: Tarifa(50, -1, 10)):  errores += 1
if not check_excepcion("penalizacion negativa",  lambda: Tarifa(50, 0.2, -5)): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ TURISMO ══════")
# ══════════════════════════════════════════════════════
tarifa1 = Tarifa(40.0, 0.15, 20.0)
v1 = Turismo("1234ABC", "Toyota", "Corolla", tarifa1, "Rojo", 4, "gasolina", "Bueno", 5)
if not check("Crear Turismo",               v1.matricula == "1234ABC"): errores += 1
if not check("Matrícula en mayúsculas",     v1.matricula == "1234ABC"): errores += 1
if not check("Disponible al crear",         v1.disponible is True): errores += 1
if not check("alquilar() → True",           v1.alquilar() is True): errores += 1
if not check("No disponible tras alquilar", v1.disponible is False): errores += 1
if not check("alquilar() ya alquilado → False", v1.alquilar() is False): errores += 1
if not check("devolver() → True",           v1.devolver() is True): errores += 1
if not check("Disponible tras devolver",    v1.disponible is True): errores += 1
if not check("devolver() ya disponible → False", v1.devolver() is False): errores += 1
if not check_excepcion("Turismo matrícula vacía",  lambda: Turismo("", "Toyota", "Corolla", tarifa1, "Rojo", 4, "gasolina", "Bueno", 5)): errores += 1
if not check_excepcion("Turismo puertas negativas", lambda: Turismo("9999ZZZ", "X", "Y", tarifa1, "Azul", -2, "gasolina", "Bueno", 5)): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ FURGONETA ══════")
# ══════════════════════════════════════════════════════
tarifa2 = Tarifa(80.0, 0.30, 50.0)
f1 = Furgoneta("5678DEF", "Mercedes", "Sprinter", tarifa2, "Blanco", 3, "diesel", "Excelente", 9)
if not check("Crear Furgoneta",          f1.marca == "Mercedes"): errores += 1
if not check("Combustible en minúsculas", f1.combustible == "diesel"): errores += 1
if not check_excepcion("Furgoneta plazas cero", lambda: Furgoneta("X", "X", "X", tarifa2, "X", 3, "diesel", "OK", 0)): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ ELÉCTRICO ══════")
# ══════════════════════════════════════════════════════
tarifa3 = Tarifa(60.0, 0.10, 25.0)
e1 = Electrico("9012GHI", "Tesla", "Model 3", tarifa3, "Negro", 4, "Nuevo", 5, 75.0, 500, 8.0)
if not check("Crear Eléctrico",           e1.bateria == 75.0): errores += 1
if not check("Autonomía correcta",         e1.autonomia == 500): errores += 1
if not check_excepcion("Batería negativa", lambda: Electrico("X","X","X", tarifa3,"X",4,"OK",5,-10,300,8)): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ CLIENTE ══════")
# ══════════════════════════════════════════════════════
c1 = Cliente("Ana García", "12345678A", "ana@gmail.com", date(1990, 5, 15), 46000, 600123456)
if not check("Crear Cliente",           c1.nombre == "Ana García"): errores += 1
if not check("Historial vacío al crear", len(c1.historial) == 0): errores += 1

c2 = Cliente("Luis Pérez", "87654321B", "luis@gmail.com", date(1985, 3, 22), 28001, 611222333)
if not check("Crear segundo Cliente", c2.dni == "87654321B"): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ EMPLEADO ══════")
# ══════════════════════════════════════════════════════
emp = Empleado("Carlos Ruiz", "11223344C", "carlos@empresa.com", date(1980, 1, 10), 46001, 677888999, 1, "gerente", 2500.0)
if not check("Crear Empleado",            emp.puesto == "gerente"): errores += 1
if not check("Sueldo correcto",           emp.sueldo == 2500.0): errores += 1
if not check("id_empleado solo lectura",  emp.id_empleado == 1): errores += 1
if not check_excepcion("Puesto inválido", lambda: Empleado("X","X","X",date(2000,1,1),46000,600000000,2,"cajero",1000)): errores += 1
if not check_excepcion("Sueldo negativo", lambda: Empleado("X","X","X",date(2000,1,1),46000,600000000,3,"mecanico",-100)): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ SEGURO ══════")
# ══════════════════════════════════════════════════════
s1 = Seguro("Básico", 5.0, {"responsabilidad_civil": True})
if not check("Crear Seguro",               s1.tipo_seguro == "Básico"): errores += 1
if not check("calcular_precio 4 días",     s1.calcular_precio(4) == 20.0): errores += 1
if not check_excepcion("precio_dia cero",  lambda: Seguro("X", 0, {"a": True})): errores += 1
if not check_excepcion("cobertura vacía",  lambda: Seguro("X", 5.0, {})): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ INVENTARIO ══════")
# ══════════════════════════════════════════════════════
inv = Inventario()
tarifa_inv = Tarifa(30.0, 0.1, 10.0)
vi1 = Turismo("AAA111", "Seat", "Ibiza", tarifa_inv, "Azul", 5, "gasolina", "OK", 5)
vi2 = Furgoneta("BBB222", "Ford", "Transit", tarifa_inv, "Blanco", 3, "diesel", "OK", 8)
inv.agregar_vehiculo(vi1)
inv.agregar_vehiculo(vi2)
if not check("agregar 2 vehículos",             len(inv.vehiculos) == 2): errores += 1
if not check("lista_disponible devuelve ambos", len(inv.lista_disponible()) == 2): errores += 1
vi1.alquilar()
if not check("lista_disponible tras alquilar 1", len(inv.lista_disponible()) == 1): errores += 1
if not check("buscar_por_matricula existente",   inv.buscar_por_matricula("BBB222") is vi2): errores += 1
if not check("buscar_por_matricula inexistente", inv.buscar_por_matricula("ZZZ999") is None): errores += 1
if not check("eliminar_vehiculo existente",      inv.eliminar_vehiculo("BBB222") is True): errores += 1
if not check("eliminar_vehiculo inexistente",    inv.eliminar_vehiculo("ZZZ999") is False): errores += 1
if not check_excepcion("agregar no-Vehiculo",   lambda: inv.agregar_vehiculo("no soy un vehiculo")): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ RESERVA ══════")
# ══════════════════════════════════════════════════════
tarifa_r = Tarifa(50.0, 0.2, 30.0)
vr = Turismo("CCC333", "Honda", "Civic", tarifa_r, "Gris", 4, "gasolina", "Bueno", 5)
cr = Cliente("Marta Sanz", "55667788D", "marta@gmail.com", date(1995, 8, 20), 46002, 622333444)
r1 = Reserva(cr, vr, date(2025, 8, 1), date(2025, 8, 6))
if not check("Crear Reserva activa",       r1.activa is True): errores += 1
if not check("Duración 5 días",            r1.duracion() == 5): errores += 1
if not check("cancelae_reserva() → True",  r1.cancelae_reserva() is True): errores += 1
if not check("Reserva inactiva tras cancel", r1.activa is False): errores += 1
if not check("cancelae_reserva() ya cancel → False", r1.cancelae_reserva() is False): errores += 1
if not check_excepcion("fecha_fin <= fecha_inicio", lambda: Reserva(cr, vr, date(2025,8,10), date(2025,8,5))): errores += 1
if not check_excepcion("cliente no es Cliente",     lambda: Reserva("no_cliente", vr, date(2025,8,1), date(2025,8,5))): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ ALQUILER ══════")
# ══════════════════════════════════════════════════════
tarifa_a = Tarifa(50.0, 0.2, 30.0)
va = Turismo("DDD444", "BMW", "Serie 3", tarifa_a, "Negro", 4, "gasolina", "Perfecto", 5)
ca = Cliente("Pedro Mora", "99887766E", "pedro@gmail.com", date(1988, 11, 3), 46003, 633444555)
ra = Reserva(ca, va, date(2025, 9, 1), date(2025, 9, 5))   # 4 días
sa = Seguro("Todo Riesgo", 20.0, {"responsabilidad_civil": True, "robo": True, "daños_propios": True})
al = Alquiler(ra, sa)
if not check("Crear Alquiler activo",   al.activo is True): errores += 1
# 4 días × 50 €/día = 200 € vehículo + 4 días × 20 €/día = 80 € seguro → 280 €
if not check("calcular_total 280 €",   al.calcular_total() == 280.0): errores += 1
al.finalizar()
if not check("Alquiler inactivo tras finalizar", al.activo is False): errores += 1
if not check("Vehículo disponible tras finalizar", va.disponible is True): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ FACTURA ══════")
# ══════════════════════════════════════════════════════
tarifa_f = Tarifa(50.0, 0.2, 30.0)
vf = Turismo("EEE555", "Audi", "A4", tarifa_f, "Plata", 4, "gasolina", "Bueno", 5)
cf = Cliente("Laura Gil", "11223300F", "laura@gmail.com", date(1992, 4, 7), 46004, 644555666)
rf = Reserva(cf, vf, date(2025, 10, 1), date(2025, 10, 4))   # 3 días
sf = Seguro("Estándar", 10.0, {"responsabilidad_civil": True, "robo": True})
alf = Alquiler(rf, sf)
fac = Factura(alf)
if not check("Total 0 antes de generar",    fac.total == 0.0): errores += 1
total = fac.generar_total()
# 3 días × 50 € + 3 días × 10 € = 180 €
if not check("generar_total devuelve 180 €", total == 180.0): errores += 1
if not check("fac.total es 180 €",           fac.total == 180.0): errores += 1
if not check_excepcion("Factura sin Alquiler", lambda: Factura("no_alquiler")): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ SISTEMA ALQUILER (flujo completo) ══════")
# ══════════════════════════════════════════════════════
sistema = SistemaAlquiler()

# Clientes
cs1 = Cliente("Elena Torres", "22334455G", "elena@gmail.com", date(1993, 2, 14), 46005, 655666777)
cs2 = Cliente("Tomás Ruiz",   "33445566H", "tomas@gmail.com", date(1987, 7, 30), 46006, 666777888)
sistema.registrar_cliente(cs1)
sistema.registrar_cliente(cs2)
if not check("Registrar 2 clientes",          len(sistema.listar_clientes()) == 2): errores += 1
if not check_excepcion("DNI duplicado",        lambda: sistema.registrar_cliente(cs1)): errores += 1

# Vehículos
ts = Tarifa(45.0, 0.18, 25.0)
vs1 = Turismo("FFF666", "Renault", "Megane", ts, "Rojo",  4, "gasolina", "Bueno", 5)
vs2 = Furgoneta("GGG777", "Citroën", "Jumper", ts, "Blanco", 3, "diesel", "OK", 9)
vs3 = Electrico("HHH888", "Peugeot", "e-208", ts, "Azul", 4, "Nuevo", 5, 50.0, 340, 7.5)
sistema.agregar_vehiculo(vs1)
sistema.agregar_vehiculo(vs2)
sistema.agregar_vehiculo(vs3)
if not check("Añadir 3 vehículos",              len(sistema.vehiculos_disponibles()) == 3): errores += 1
if not check_excepcion("Matrícula duplicada",   lambda: sistema.agregar_vehiculo(vs1)): errores += 1

# Reservas
rs1 = sistema.crear_reserva(cs1, vs1, date(2025, 11, 1), date(2025, 11, 5))   # 4 días
rs2 = sistema.crear_reserva(cs2, vs2, date(2025, 11, 10), date(2025, 11, 12)) # 2 días
if not check("Crear 2 reservas",                len(sistema.listar_reservas()) == 2): errores += 1
if not check("reservas_activas devuelve 2",     len(sistema.reservas_activas()) == 2): errores += 1

# Cancelar reserva 2
cancelada = sistema.cancelar_reserva(rs2)
if not check("Cancelar reserva → True",         cancelada is True): errores += 1
if not check("reservas_activas devuelve 1",     len(sistema.reservas_activas()) == 1): errores += 1
if not check("Cancelar ya cancelada → False",   sistema.cancelar_reserva(rs2) is False): errores += 1

# Iniciar alquiler reserva 1
ss1 = Seguro("Básico", 5.0, {"responsabilidad_civil": True})
al1 = sistema.iniciar_alquiler(rs1, ss1)
if not check("Iniciar alquiler → activo",       al1.activo is True): errores += 1
if not check("Vehículo no disponible",          vs1.disponible is False): errores += 1
if not check("Historial cliente actualizado",   len(cs1.historial) == 1): errores += 1
if not check_excepcion("Iniciar reserva inactiva", lambda: sistema.iniciar_alquiler(rs2, ss1)): errores += 1

# Vehículos disponibles tras alquiler
if not check("2 vehículos disponibles (vs2 cancelado pero disponible)",
             len(sistema.vehiculos_disponibles()) == 2): errores += 1

# Finalizar alquiler
fac1 = sistema.finalizar_alquiler(al1)
# 4 días × 45 € + 4 días × 5 € = 200 €
if not check("Factura generada correctamente",  fac1 is not None): errores += 1
if not check("Total factura 200 €",             fac1.total == 200.0): errores += 1
if not check("Alquiler finalizado",             al1.activo is False): errores += 1
if not check("Vehículo disponible de nuevo",    vs1.disponible is True): errores += 1

# Eliminar vehículo
if not check("Eliminar vehículo disponible",    sistema.eliminar_vehiculo("GGG777") is True): errores += 1
if not check("Eliminar inexistente → False",    sistema.eliminar_vehiculo("ZZZZZZ") is False): errores += 1
vs1.alquilar()
if not check_excepcion("Eliminar vehículo alquilado", lambda: sistema.eliminar_vehiculo("FFF666")): errores += 1

# ══════════════════════════════════════════════════════
print("\n══════ RESUMEN ══════")
if errores == 0:
    print("  🎉 TODOS LOS TESTS PASARON SIN ERRORES")
else:
    print(f"  ⚠️  {errores} TEST(S) FALLARON — revisar los ❌ de arriba")