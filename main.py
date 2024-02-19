class Asiento:
    def __init__(self, color, precio, registro):
        self.color = ""
        self.precio = 0
        self.registro = 0

    def cambiarColor(self, color):
        colores_validos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores_validos:
            self.color = color


class Motor:
    def __init__(self, numero_cilindros, tipo, registro):
        self.numero_cilindros = 0
        self.tipo = ""
        self.registro = 0

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
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

    def cantidadAsientos(self):
        num_asientos = 0
        for asiento in self.asientos:
            if asiento is not None:
                num_asientos += 1
        return num_asientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento is not None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"
