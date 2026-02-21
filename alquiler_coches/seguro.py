#Atributos: tipo_seguro, precio_dia, cobertura(características del seguro)
#Métodos: calcular_precio(dias), mostrar_info()

class Seguro: 
    def __init__(self, tipo_seguro:str, precio_dia:float, cobertura:dict): 
        self.tipo_seguro=tipo_seguro
        self.precio_dia=precio_dia
        self.cobertura=cobertura
    
    def calcular_precio(self, dias: int): 
        return self.precio_dia*dias
    
    def __str__(self): 
        return f"Tipo de seguro: {self.tipo_seguro}, precio al día: {self.precio_dia}, cobertura: {self.cobertura}"

    