"""
Docstring for Programacion_Objetos_IA.python.produto
Diseñá una clase que represente un producto que se vende en una tienda. 
Debe incluir: 
- Código (int) 
- Descripción (String) 
- Precio (float) 
Y los siguientes métodos: 
- calcularDescuento(porcentaje: float): float 
- mostrarInformacion(): void

"""

class Producto:
    def __init__(self, codigo: int, descripcion: str, precio: float):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
    
    def calcularDescuento(self, porcentaje: float) -> float:
        descuento = self.get_precio() * (porcentaje / 100)
        return self.__precio - descuento
    
    def mostrarInformacion(self) -> None:
        print(f"Código: {self.get_codigo()}")
        print(f"Descripción: {self.get_descripcion()}")
        print(f"Precio: ${self.get_precio():.2f}")

    def get_precio(self) -> float:
        return self.__precio
    
    def get_codigo(self) -> int:
        return self.__codigo
    
    def get_descripcion(self) -> str:
        return self.__descripcion

if __name__ == "__main__":
    # Ejemplo de uso
    producto = Producto(101, "Laptop Dell", 1500.00)
    producto.mostrarInformacion()
    
    precio_con_descuento = producto.calcularDescuento(15)
    print(f"Precio con 15% descuento: ${precio_con_descuento:.2f}")