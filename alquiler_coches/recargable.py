class Recargable:
    """
        Clase Recargable
            Representa cualquier vehículo que funciona con batería recargable.

        Atributos
        -----------------
        bateria: float
            Capacidad de la batería en kWh
        autonomia: int
            Autonomía máxima en kilómetros
        tiempo_carga: float
            Tiempo estimado de carga completa en horas

        Metodos:
        -------------
        recargar(self):
            Simula la recarga del vehículo
    """

    def __init__(self, bateria, autonomia, tiempo_carga):
        self.bateria = bateria
        self.autonomia = autonomia
        self.tiempo_carga = tiempo_carga

    def recargar(self):
        print(f"Recargando batería de {self.bateria}kWh... Tiempo estimado: {self.tiempo_carga}h")