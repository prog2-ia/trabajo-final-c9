#Atributos: puertas, combustible, estado, (color), plazas (hereda de vehiculo)
#Métodos: (usa los de vehículos), mostrar_info()
from vehiculo import Vehiculo
class Turismo(Vehiculo): 
    def __init__(self, matricula, marca, modelo, precio_dia, color, puertas, combustible, estado, plazas): 
        #constructor del padre
        super().__init__(matricula, marca, modelo, precio_dia, color)
        #atributos nuevos 
        self.puertas=puertas
        self.combustible=combustible 
        self.estado=estado 
        self.plazas=plazas
     
    def __str__(self):
        info_padre = super().__str__()
        return (f"{info_padre}, "
                f"puertas: {self.puertas}, "
                f"combustible: {self.combustible}, "
                f"estado: {self.estado}, "
                f"plazas: {self.plazas}")