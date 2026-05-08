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
        fecha_nacimiento: str
            Fecha de nacimiento de la persona.
        codigo_postal: str
            El Código postal de la persona
        telefono: str
            El telefono de la persona

        Metodos:
        -------------
        __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: str, codigo_postal: int, telefono: int)
            Constructor del objeto.
    """

    def __init__(self, nombre: str, dni: str, gmail: str, fecha_nacimiento: date, codigo_postal: int, telefono: int) -> None:
        """
        Metodo constructor

        Parámetros:
        -----------------
        nombre: str
            Nombre de la persona
        dni: str
            Dni de la persona. Forma primaria de identificación
        fecha_nacimiento: str
            Fecha de nacimiento de la persona
       codigo_postal: int
            El Código postal de la persona
        telefono: int
            El telefono de la persona
        """

        self._nombre = nombre
        self._dni = dni
        self._gmail = gmail
        self._fecha_nacimiento = fecha_nacimiento
        self._codigo_postal = codigo_postal
        self._telefono = telefono

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def dni(self) -> str:
        return self._dni

    @property
    def gmail(self) -> str:
        return self._gmail

    @property
    def fecha_nacimiento(self) -> date:
        return self._fecha_nacimiento

    @property
    def telefono(self) -> int:
        return self._telefono

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre}\n"
                f"DNI: {self.dni}\n"
                f"Gmail: {self.gmail}\n"
                f"Fecha nacimiento: {self._fecha_nacimiento}\n"
                f"Código postal: {self._codigo_postal}\n"
                f"Teléfono: {self.telefono}\n")

