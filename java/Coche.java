public class Coche {
    // Atributos
    private String marca;
    private String modelo;
    private int año;
    private String color;
    private int velocidad_maxima;
    private int velocidad_actual;

    // Constructor
    public Coche(String marca, String modelo, int año, String color, int velocidad_maxima) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.color = color;
        this.velocidad_maxima = velocidad_maxima;
        this.velocidad_actual = 0;
    }

    // Método para acelerar
    public void acelerar(int cantidad) {
        velocidad_actual += cantidad;
        if (velocidad_actual > velocidad_maxima) {
            velocidad_actual = velocidad_maxima;
        }
        System.out.println("Acelerando " + cantidad + " km/h. Velocidad actual: " + velocidad_actual + " km/h");
    }

    // Método para frenar
    public void frenar() {
        velocidad_actual = 0;
        System.out.println("El coche ha frenado. Velocidad actual: 0 km/h");
    }

    // Método para mostrar información
    public void mostrar_info() {
        System.out.println("\n--- Información del Coche ---");
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Año: " + año);
        System.out.println("Color: " + color);
        System.out.println("Velocidad máxima: " + velocidad_maxima + " km/h");
        System.out.println("Velocidad actual: " + velocidad_actual + " km/h");
        System.out.println("-----------------------------\n");
    }

    // Método main para simular un viaje
    public static void main(String[] args) {
        // Crear un objeto Coche
        Coche miCoche = new Coche("Toyota", "Corolla", 2023, "Rojo", 200);

        // Simular un viaje
        System.out.println("=== Simulación de Viaje ===\n");
        miCoche.mostrar_info();

        miCoche.acelerar(50);
        miCoche.acelerar(40);
        miCoche.acelerar(30);
        miCoche.mostrar_info();

        miCoche.acelerar(100); // Intenta exceder la velocidad máxima
        miCoche.mostrar_info();

        miCoche.frenar();
        miCoche.mostrar_info();
    }
}