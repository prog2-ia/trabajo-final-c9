# Sistema de Alquiler de Coches

## Descripción
Sistema de gestión de alquiler de vehículos desarrollado en Python. 
Permite gestionar clientes, empleados, vehículos, reservas, alquileres y facturas.

## Instalación
1. Clona el repositorio
2. Entra en la carpeta del proyecto:
   cd alquiler_coches

## Uso
Ejecuta el programa principal:
   python3 main.py

## Estructura del proyecto
- `persona.py` — Clase base abstracta para personas
- `cliente.py` — Gestión de clientes
- `empleado.py` — Gestión de empleados
- `vehiculo.py` — Clase base abstracta para vehículos
- `turismo.py` — Vehículo tipo turismo
- `furgoneta.py` — Vehículo tipo furgoneta
- `electrico.py` — Vehículo eléctrico
- `tarifa.py` — Gestión de tarifas
- `reserva.py` — Gestión de reservas
- `seguro.py` — Gestión de seguros
- `alquiler.py` — Gestión de alquileres
- `factura.py` — Generación de facturas
- `inventario.py` — Control del inventario de vehículos
- `sistema_alquiler.py` — Controlador principal del sistema
- `main.py` — Menú interactivo

## Ejemplo de uso
Al ejecutar el programa aparece un menú con 14 opciones que permiten
registrar clientes, añadir vehículos, crear reservas, iniciar y finalizar
alquileres, ver facturas e ingresos totales.