#Atributos: matricula, marca, modelo, precio_dia, disponible (booleano), (color)
#Métodos: alquilar(), devolver(), mostrar_info()

class Vehiculo: 
    def __init__(self, matricula:str, marca:str, modelo:str, precio_dia:float, color:str): 
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo 
        self.precio_dia=precio_dia 
        self.color= color 
        self.disponible=True 
    
    def alquilar(self): 
        if self.disponible: 
            print("Es posible alquilar este vehículo")
            self.disponible=False 
        else: 
            print("El vehículo no está disponible")

    def devolver(self): 
        if not self.disponible:
            print("El vehículo se ha devuelto")
            self.disponible=True 
        else: 
            print("El vehículo ya estaba disponible")

    def __str__(self): 
        return f"Matrícula: {self.matricula}, marca: {self.marca}, modelo:{self.modelo}, precio al día: {self.precio_dia}, disponible: {self.disponible}, color: {self.color}"