# Sistema de Alquiler de Coches

## Descripción

Sistema de gestión de alquiler de vehículos desarrollado en Python siguiendo los principios de Programación Orientada a Objetos (POO).

La aplicación permite gestionar:
- Clientes y empleados
- Vehículos de distintos tipos
- Reservas y alquileres
- Facturas y seguros
- Inventario de vehículos
- Persistencia de datos mediante ficheros de texto y binarios

El sistema incluye un menú interactivo por consola que permite realizar todas las operaciones principales de gestión de una empresa de alquiler de coches.

---

# Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Persistencia con `pickle`
- Ficheros de texto
- Modularización mediante paquetes

---

# Estructura del proyecto

```text
alquiler_coches/
│
├── personas/
│   ├── persona.py
│   ├── cliente.py
│   └── empleado.py
│
├── vehiculos/
│   ├── vehiculo.py
│   ├── turismo.py
│   ├── furgoneta.py
│   ├── electrico.py
│   └── recargable.py
│
├── gestion_alquileres/
│   ├── tarifa.py
│   ├── seguro.py
│   ├── reserva.py
│   ├── alquiler.py
│   ├── factura.py
│   ├── inventario.py
│   └── sistema_alquiler.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

## 2. Acceder al proyecto

```bash
cd alquiler_coches
```

## 3. Ejecutar el programa

```bash
python3 main.py
```

---

# Funcionalidades principales

- Registrar clientes y empleados
- Añadir y eliminar vehículos
- Crear y cancelar reservas
- Iniciar y finalizar alquileres
- Generar facturas automáticamente
- Consultar ingresos totales
- Gestión del inventario de vehículos
- Guardado y carga del sistema mediante ficheros binarios
- Exportación de facturas en ficheros de texto

---

# Características de Programación Orientada a Objetos

El proyecto implementa distintos conceptos de POO:

- Clases y objetos
- Encapsulamiento mediante atributos protegidos y propiedades
- Herencia simple
- Polimorfismo
- Clases abstractas (`ABC`)
- Sobrecarga de métodos especiales (`__str__`)
- Modularización en paquetes
- Sugerencia de tipos (`type hints`)
- Manejo de excepciones

---

# Persistencia de datos

El sistema utiliza:
- Ficheros de texto (`.txt`) para guardar facturas
- Ficheros binarios (`.dat`) mediante `pickle` para guardar el estado completo del sistema

---

# Ejemplo de uso

Al ejecutar el programa se muestra un menú interactivo con las siguientes opciones:

```text
1. Registrar cliente
2. Añadir vehículo
3. Eliminar vehículo
4. Crear reserva
5. Cancelar reserva
6. Iniciar alquiler
7. Finalizar alquiler
8. Ver vehículos disponibles
9. Ver inventario completo
10. Ver reservas
11. Ver clientes
12. Gestionar empleados
13. Ver ingresos totales
14. Guardar sistema
15. Salir
```

El usuario puede interactuar con el sistema desde consola realizando operaciones de gestión sobre clientes, vehículos, reservas y alquileres.

---

# Autores

Proyecto desarrollado por:
- Victoria Pérez Bernabeu 
- María Ripoll Gomis 