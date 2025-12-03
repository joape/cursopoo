public class CuentaBancaria {
    private String titular;
    private String numero_cuenta;
    private double saldo;

    public CuentaBancaria(String titular, String numero_cuenta) {
        this.titular = titular;
        this.numero_cuenta = numero_cuenta;
        this.saldo = 0.0;
    }

    public void ingresar_dinero(double cantidad) {
        saldo += cantidad;
    }

    public void retirar_dinero(double cantidad) {
        if (cantidad <= saldo) {
            saldo -= cantidad;
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }

    public void mostrar_saldo() {
        System.out.println("Saldo actual: " + saldo);
    }

    // Método para obtener el saldo
    protected double getSaldo() {
        return saldo;
    }
}

class CuentaJoven extends CuentaBancaria {
    private double limite_extraccion;

    public CuentaJoven(String titular, String numero_cuenta, double limite_extraccion) {
        super(titular, numero_cuenta);
        this.limite_extraccion = limite_extraccion;
    }

    @Override
    public void retirar_dinero(double cantidad) {
        if (cantidad <= getSaldo() && cantidad <= limite_extraccion) {
            super.retirar_dinero(cantidad);
        } else {
            System.out.println("No se puede retirar esa cantidad.");
        }
    }
}