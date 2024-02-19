class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores_validos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores_validos:
            self.color = color


class Motor:
    def __init__(self, numero_cilindros, tipo, registro):
        self.numero_cilindros = numero_cilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipos_validos = ["electrico", "gasolina"]
        if tipo in tipos_validos:
            self.tipo = tipo


class Auto:
    cantidad_creados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
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
                if asiento is not None and asiento.registro != self.registro:  
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"
