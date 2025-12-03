class Perro:
    def __init__(self, nombre: str, raza: str, edad: int):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
    
    def ladrar(self) -> None:
        print(f"{self.__nombre} está ladrando: ¡Guau guau!")
    
    def jugar(self) -> None:
        print(f"{self.__nombre} quiere jugar y está saltando alegremente")
    
    def comer(self) -> None:
        print(f"{self.__nombre} está comiendo sabroso")
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_raza(self) -> str:
        return self.__raza
    
    def get_edad(self) -> int:
        return self.__edad

if __name__ == "__main__":
    # Creo un objeto de la clase Perro
    perro1 = Perro("Rex", "Pastor Alemán", 3)
    
    print(f"Información del perro:")  # noqa: F541
    print(f"Nombre: {perro1.get_nombre()}")
    print(f"Raza: {perro1.get_raza()}")
    print(f"Edad: {perro1.get_edad()} años\n")
    
    # Usando los métodos
    perro1.ladrar()
    perro1.jugar()
    perro1.comer()