from persona import Persona

class Empleado(Persona):
    """
        Clase Empleado
            Representa al empleado de nuestro servicio de alguiler de vehiculos.
            Hereda las características generales de la clase Persona y añade algunas propias.

        Atributos
        -----------------
        id_empleado:
            Id único que identifica a cada empledo
        puesto:
            Rango de cada empleado
        sueldo:
            Sueldo de cada empleado

        Metodos:
        -------------
        __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: date, codigo_postal: int, telefono: int, id_empleado: int, puesto: str, sueldo: float)
            Constructor del objeto.
    """

    puestos_validos = ("gerente", "administrativo", "mecanico")

    def __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento, codigo_postal: int, telefono: int, id_empleado: int, puesto: str, sueldo: float):
        super().__init__(nombre, dni, gmail, fecha_nacimiento, codigo_postal, telefono)
        self._id_empleado = id_empleado  # (solo lectura)
        self.puesto = puesto
        self.sueldo = sueldo

        """
        Metodo constructor

        Parámetros:
        -----------------
        id_empleado: int
            Id único de cada empleado. Es un número entero
        puesto: str
            Rango de cada empleado. Debe ser un str y tiene que ser válido
        sueldo: float
            Sueldo de cada empleado. Puede ser un float o un int positivo
        """

    @property
    def id_empleado(self):
        return self._id_empleado

    @property
    def puesto(self):
        return self._puesto

    @puesto.setter
    def puesto(self, nuevo_puesto):
        if not isinstance(nuevo_puesto, str):
            raise ValueError("Puesto debe ser un str ")
        if nuevo_puesto.lower() not in Empleado.puestos_validos:
            raise ValueError("No es un puesto válido ")
        self._puesto = nuevo_puesto

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        if not isinstance(nuevo_sueldo, (int, float)) or nuevo_sueldo < 0:
            raise ValueError("Sueldo debe ser mayor que 0.")
        self._sueldo = nuevo_sueldo


    def __str__(self):
        info_padre = super().__str__()
        return  (f"{info_padre}"
            f"Id: {self.id_empleado}\n"
            f"Puesto: {self.puesto}\n"
            f"Sueldo: {self.sueldo}\n")





