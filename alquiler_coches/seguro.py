class Seguro:
    """
        Clase Seguro
            Representa un seguro asociado a un servicio o producto.
            Controla el tipo de seguro, su precio diario y sus coberturas.

        Atributos
        -----------------
        tipo_seguro: str
            Nombre o categoría del seguro (Básico, Premium, Todo Riesgo...)
        precio_dia: float
            Precio por día del seguro. Debe ser positivo
        cobertura: dict
            Diccionario con las coberturas incluidas en el seguro

        Métodos
        -------------
        __init__(self, tipo_seguro: str, precio_dia: float, cobertura: dict) -> None
            Constructor del objeto

        calcular_precio(self, dias: int) -> float
            Calcula el coste total del seguro según los días contratados

        __str__(self) -> str
            Devuelve la información del seguro en formato legible
    """

    def __init__(self, tipo_seguro: str, precio_dia: float, cobertura: dict) -> None:
        """
        Metodo constructor

        Parámetros
        -----------------
        tipo_seguro: str
            Tipo de seguro contratado
        precio_dia: float
            Precio diario del seguro (mayor que 0)
        cobertura: dict
            Conjunto de coberturas incluidas
        """

        self.tipo_seguro = tipo_seguro
        self.precio_dia = precio_dia
        self.cobertura = cobertura

    @property
    def tipo_seguro(self) -> str:
        return self._tipo_seguro

    @tipo_seguro.setter
    def tipo_seguro(self, nuevo: str) -> None:
        """
        Establece el tipo de seguro validando que no esté vacío
        """
        if not isinstance(nuevo, str) or not nuevo.strip():
            raise ValueError("El tipo de seguro debe ser un texto no vacío")
        self._tipo_seguro = nuevo.strip()

    @property
    def precio_dia(self) -> float:
        return self._precio_dia

    @precio_dia.setter
    def precio_dia(self, nuevo: float) -> None:
        """
        Establece el precio por día validando que sea positivo
        """
        if not isinstance(nuevo, (int, float)) or nuevo <= 0:
            raise ValueError("El precio por día debe ser positivo")
        self._precio_dia = float(nuevo)

    @property
    def cobertura(self) -> dict[str, str]:
        return self._cobertura.copy()

    @cobertura.setter
    def cobertura(self, nuevo: dict[str, str]) -> None:
        """
        Establece la cobertura validando que sea un diccionario no vacío
        """
        if not isinstance(nuevo, dict) or len(nuevo) == 0:
            raise ValueError("La cobertura debe ser un diccionario no vacío")
        self._cobertura = nuevo.copy()

    def calcular_precio(self, dias: int) -> float:
        """
        Calcula el precio total del seguro

        Parámetros
        -----------------
        dias: int
            Número de días contratados (mayor que 0)

        Retorno
        -----------------
        float
            Precio total del seguro
        """
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("Los días deben ser un entero positivo")
        return self.precio_dia * dias

    def __str__(self) -> str:
        return (f"--- SEGURO ---\n"
                f"Tipo: {self.tipo_seguro}\n"
                f"Precio/día: {self.precio_dia}\n")

