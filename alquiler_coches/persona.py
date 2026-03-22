#Atributos: nombre, dni, telefono, codigo_postal, email, fecha_nacimiento 
#Métodos: mostra_info()

#Debería de ser abstracta(COMENTAR CON VICTORIA)
from abc import ABC
from datetime import date

class Persona(ABC):
    """
        Clase Persona
            Cubre lo básico de cualquier persona.
            Clase madre de todas las demás clases que son consideradas personas

        Atributos
        -----------------
        nombre: str
            Nombre de la persona
        dni: str
            Documento Nacional Identificador de la persona.
        gmail: str
            El correo electrónico de la persona
        fecha_nacimiento: date
            Fecha de nacimiento de la persona.
        codigo_postal: int
            El Código postal de la persona
        telefono: int
            El telefono de la persona


        Metodos:
        -------------
        __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: str, codigo_postal: int, telefono: int) -> None:
            Constructor del objeto.
    """

    def __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: date, codigo_postal: int, telefono: int):
        """
        Metodo constructor

        Parámetros:
        -----------------
        nombre: str
            Nombre de la persona
        dni: str
            Dni de la persona. Forma primaria de identificación
        fecha_nacimiento: date
            Fecha de nacimiento de la persona en formato date (yyyy/mm/dd)
       codigo_postal: int
            El Código postal es un número formado por cinco dígitos
        telefono: int
            El telefono es un número formado por nueve dígitos

        """

        self._nombre = nombre
        self._dni = dni
        self._gmail = gmail
        self.fecha_nacimiento = fecha_nacimiento
        self._codigo_postal = codigo_postal
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def gmail(self):
        return self._gmail

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        if not isinstance(fecha_nacimiento, date):
            raise ValueError("La fecha de inicio será un objeto date")
        self._fecha_nacimiento= fecha_nacimiento

    @property
    def telefono(self):
        return self._telefono

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"DNI: {self.dni}\n"
                f"Gmail: {self.gmail}\n"
                f"Fecha nacimiento: {self._fecha_nacimiento}\n"
                f"Código postal: {self._codigo_postal}\n"
                f"Teléfono: {self.telefono}\n")

