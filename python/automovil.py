"""
Docstring for Programacion_Objetos_IA.python.automovil
Diseñá una clase que represente un automóvil. 
Debe incluir: 
- Marca (String) 
- Modelo (String) 
- Año (int) 
- VelocidadActual (float) 
Y los siguientes métodos: 
- acelerar(incremento: float): void 
- frenar(decremento: float): void 
- mostrarEstado(): void
"""

class Automovil:
    def __init__(self, marca: str, modelo: str, año: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__velocidad_actual = 0

    def acelerar(self, incremento: float) -> None:
           
            if incremento > 0:
                self.__velocidad_actual += incremento
                print(f"Acelerando: +{incremento} km/h")
            else:
                print("El incremento debe ser positivo")
        
    def frenar(self, decremento: float) -> None:
           
            if decremento > 0:
                velocidad= self.get_velocidad_actual()
                velocidad -= decremento
                self.__velocidad_actual = velocidad
                if velocidad < 0:
                    self.__velocidad_actual = 0
                print(f"Frenando: -{decremento} km/h")
            else:
                print("El decremento debe ser positivo")

    def mostrarEstado(self) -> None:
      
            print(f"Marca: {self.get_marca()}")
            print(f"Modelo: {self.get_modelo()}")
            print(f"Año: {self.get_año()}")
            print(f"Velocidad actual: {self.get_velocidad_actual():.1f} km/h")
    
    def get_marca(self) -> str:
        return self.__marca
    
    def get_modelo(self) -> str:
        return self.__modelo
    
    def get_año(self) ->int:
        return self.__año
    
    def get_velocidad_actual(self) -> float:
        return self.__velocidad_actual

if __name__ == "__main__":
    # Ejemplo de uso
    auto = Automovil("Toyota", "Corolla", 2023)
    auto.mostrarEstado()
    
    print("\n--- Pruebas de aceleración y frenado ---")
    auto.acelerar(60)
    auto.mostrarEstado()
    
    auto.acelerar(40)
    auto.mostrarEstado()
    
    auto.frenar(30)
    auto.mostrarEstado()
    
    auto.frenar(80)
    auto.mostrarEstado()    