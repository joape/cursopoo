class Coche:
    def __init__(self, marca, modelo, año, color, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def get_color(self):
        return self.__color

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    def get_velocidad_actual(self):
        return self.__velocidad_actual

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_año(self, año):
        self.__año = año

    def set_color(self, color):
        self.__color = color

    def set_velocidad_maxima(self, velocidad):
        if velocidad < 0:
            return
        self.__velocidad_maxima = velocidad
        if self.__velocidad_actual > velocidad:
            self.__velocidad_actual = velocidad

    def set_velocidad_actual(self, velocidad):
        if velocidad < 0:
            self.__velocidad_actual = 0
        elif velocidad > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual = velocidad

    # Comportamiento
    def acelerar(self, cantidad):
        nueva = self.__velocidad_actual + cantidad
        self.set_velocidad_actual(nueva)

    def frenar(self):
        self.set_velocidad_actual(0)

    def mostrar_info(self):
        print(f"Coche: {self.get_marca()} {self.get_modelo()}, Año: {self.get_año()}, Color: {self.get_color()}, Velocidad Máxima: {self.get_velocidad_maxima()} km/h, Velocidad Actual: {self.get_velocidad_actual()} km/h")

# Ejemplo de uso
if __name__ == "__main__":
    mi_coche = Coche("Toyota", "Corolla", 2020, "Rojo", 180)
    mi_coche.mostrar_info()
    mi_coche.acelerar(50)
    mi_coche.mostrar_info()
    mi_coche.frenar()
    mi_coche.mostrar_info()