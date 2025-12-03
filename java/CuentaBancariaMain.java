// Clase principal y demostración en un único archivo (main)

public class CuentaBancariaMain {
    public static void main(String[] args) {
        // Crear una cuenta bancaria normal
        CuentaBancaria cuenta1 = new CuentaBancaria("Ana Pérez", "ES00112233", 500.0);
        cuenta1.mostrar_saldo();                     // Mostrar saldo inicial
        cuenta1.ingresar_dinero(150.0);              // Ingresar dinero
        cuenta1.mostrar_saldo();                     // Mostrar saldo después del ingreso
        cuenta1.retirar_dinero(200.0);               // Retirar dinero (suficiente saldo)
        cuenta1.mostrar_saldo();                     // Mostrar saldo después del retiro
        cuenta1.retirar_dinero(1000.0);              // Intento de retirar más de lo disponible

        System.out.println(); // Separador de salida

        // Crear una cuenta joven con límite de extracción
        CuentaJoven cuentaJoven = new CuentaJoven("Luis Gómez", "ES00998877", 300.0, 100.0);
        cuentaJoven.mostrar_saldo();                 // Saldo inicial de la cuenta joven
        cuentaJoven.retirar_dinero(120.0);           // Intento de retirar por encima del límite
        cuentaJoven.retirar_dinero(80.0);            // Retiro dentro del límite
        cuentaJoven.mostrar_saldo();                 // Saldo final
    }
}

// Clase que representa una cuenta bancaria básica
class CuentaBancaria {
    // Atributos públicos/protegidos para simplicidad (fácil de entender)
    protected String titular;
    protected String numero_cuenta;
    protected double saldo;

    // Constructor para inicializar la cuenta
    public CuentaBancaria(String titular, String numero_cuenta, double saldo) {
        this.titular = titular;
        this.numero_cuenta = numero_cuenta;
        this.saldo = saldo;
    }

    // Método para ingresar dinero: aumenta el saldo si la cantidad es positiva
    public void ingresar_dinero(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
            System.out.printf("Ingresados %.2f€ en la cuenta de %s.%n", cantidad, titular);
        } else {
            System.out.println("La cantidad a ingresar debe ser positiva.");
        }
    }

    // Método para retirar dinero: decrementa el saldo si hay suficiente y la cantidad es positiva
    public boolean retirar_dinero(double cantidad) {
        if (cantidad <= 0) {
            System.out.println("La cantidad a retirar debe ser positiva.");
            return false;
        }
        if (saldo >= cantidad) {
            saldo -= cantidad;
            System.out.printf("Retirados %.2f€ de la cuenta de %s.%n", cantidad, titular);
            return true;
        } else {
            System.out.println("Saldo insuficiente para realizar el retiro.");
            return false;
        }
    }

    // Método para mostrar el saldo actual
    public void mostrar_saldo() {
        System.out.printf("Titular: %s | Cuenta: %s | Saldo: %.2f€%n", titular, numero_cuenta, saldo);
    }
}

// Clase que hereda de CuentaBancaria y añade un límite de extracción
class CuentaJoven extends CuentaBancaria {
    private double limite_extraccion; // límite máximo por operación

    // Constructor que llama al constructor de la clase base
    public CuentaJoven(String titular, String numero_cuenta, double saldo, double limite_extraccion) {
        super(titular, numero_cuenta, saldo);
        this.limite_extraccion = limite_extraccion;
    }

    // Sobrescribir retirar_dinero para incluir la restricción del límite
    @Override
    public boolean retirar_dinero(double cantidad) {
        if (cantidad > limite_extraccion) {
            System.out.printf("Operación denegada: el retiro (%.2f€) supera el límite de extracción (%.2f€).%n",
                    cantidad, limite_extraccion);
            return false;
        }
        // Si está dentro del límite, usar la lógica de la clase base (saldo suficiente, etc.)
        return super.retirar_dinero(cantidad);
    }

    // Método opcional para mostrar el límite (no solicitado pero útil)
    public void mostrar_limite() {
        System.out.printf("Límite de extracción: %.2f€%n", limite_extraccion);
    }
}