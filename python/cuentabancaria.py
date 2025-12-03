class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    # Getters
    def get_titular(self):
        return self.__titular

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    # Setters
    def set_titular(self, titular):
        self.__titular = titular

    def set_numero_cuenta(self, numero):
        self.__numero_cuenta = numero

    def set_saldo(self, saldo):
        if saldo < 0:
            return
        self.__saldo = saldo

    def ingresar_dinero(self, cantidad):
        if cantidad <= 0:
            return
        self.__saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

class CuentaJoven(CuentaBancaria):
    def __init__(self, titular, numero_cuenta, saldo=0, limite_extraccion=0):        
        self._CuentaBancaria__titular = titular
        self._CuentaBancaria__numero_cuenta = numero_cuenta
        self._CuentaBancaria__saldo = saldo
        self.__limite_extraccion = limite_extraccion

    # Getter y setter para limite_extraccion
    def get_limite_extraccion(self):
        return self.__limite_extraccion

    def set_limite_extraccion(self, limite):
        if limite < 0:
            return
        self.__limite_extraccion = limite

    # Retirar respetando el límite joven
    def retirar_dinero(self, cantidad):
        saldo_actual = self._CuentaBancaria__saldo
        if cantidad <= saldo_actual and cantidad <= self.__limite_extraccion:
            self._CuentaBancaria__saldo -= cantidad
        else:
            print("No se puede retirar esa cantidad.")

# Código para probar las clases
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Juan Perez", "123456789", 1000)
    cuenta1.mostrar_saldo()
    cuenta1.ingresar_dinero(500)
    cuenta1.mostrar_saldo()
    cuenta1.retirar_dinero(300)
    cuenta1.mostrar_saldo()
    cuenta1.retirar_dinero(1500)

    cuenta_joven = CuentaJoven("Maria Lopez", "987654321", 500, 200)
    cuenta_joven.mostrar_saldo()
    cuenta_joven.ingresar_dinero(300)
    cuenta_joven.mostrar_saldo()
    cuenta_joven.retirar_dinero(150)
    cuenta_joven.mostrar_saldo()
    cuenta_joven.retirar_dinero(250)