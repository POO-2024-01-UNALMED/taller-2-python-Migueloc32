class Asiento:
    def __init__(self, color, precio, registro):
        self.color = ""
        self.precio = 0
        self.registro = 0

    def cambiar_color(self, color):
        colores_validos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores_validos:
            self.color = color


class Motor:
    def __init__(self, numero_cilindros, tipo, registro):
        self.numero_cilindros = 0
        self.tipo = ""
        self.registro = 0

    def cambiar_registro(self, registro):
        self.registro = registro

    def asignar_tipo(self, tipo):
        tipos_validos = ["electrico", "gasolina"]
        if tipo in tipos_validos:
            self.tipo = tipo


class Auto:
    cantidad_creados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = ""
        self.precio = 0
        self.asientos = asientos
        self.marca = ""
        self.motor = motor
        self.registro = 0
        Auto.cantidad_creados += 1

    def cantidad_asientos(self):
        total_asientos = 0
        for asiento in self.asientos:
            if asiento is not None:
                total_asientos += 1
        return total_asientos

    def verificar_integridad(self):
        if self.motor.registro == self.registro:
            for asiento in self.asientos:
                if asiento is not None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"
