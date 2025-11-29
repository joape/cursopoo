"""
Docstring for Programacion_Objetos_IA.python.alumno
Diseñá una clase para representar a un alumno. 
Debe incluir: 
- Nombre (String) 
- Apellido (String) 
- Legajo (String) 
- NotaFinal (float) 
Y los siguientes métodos: 
- aprobo(): boolean 
- mostrarDatos(): void
"""
class Alumno:
    def __init__(self, nombre: str, apellido: str, legajo: str, nota_final: float):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__legajo = legajo
        self.__nota_final = nota_final
    
    def aprobo(self) -> bool:
        nota= self.get_nota_final()
        return nota >= 6.0
    
    def mostrarDatos(self) -> None:
        
        print(f"Nombre: {self.get_nombre()}")
        print(f"Apellido: {self.get_apellido()}")
        print(f"Legajo: {self.get_legajo()}")
        print(f"Nota Final: {self.get_nota_final():.1f}")
        print(f"Estado: {'Aprobado' if self.aprobo() else 'Desaprobado'}")

    def get_nombre(self) -> str:
            return self.__nombre    

    def get_apellido(self) -> str:
            return self.__apellido

    def get_legajo(self) -> str:
            return self.__legajo

    def get_nota_final(self) -> float:
            return self.__nota_final    

if __name__ == "__main__":
    # Ejemplos de uso
    alumno1 = Alumno("Juan", "Pérez", "2023001", 7.5)
    alumno1.mostrarDatos()
    
    print("\n---")
    
    alumno2 = Alumno("María", "García", "2023002", 4.8)
    alumno2.mostrarDatos()