public class Perro {
    private String nombre;
    private String raza;
    private int edad;

    public Perro(String nombre, String raza, int edad) {
        this.nombre = nombre;
        this.raza = raza;
        this.edad = edad;
    }

    // Getters
    public String getNombre() { return nombre; }
    public String getRaza() { return raza; }
    public int getEdad() { return edad; }

    // Setters
    public void setNombre(String nombre) { this.nombre = nombre; }
    public void setRaza(String raza) { this.raza = raza; }
    public void setEdad(int edad) { this.edad = edad; }

    public void ladrar() {
        System.out.println(nombre + " está ladrando.");
    }

    public void jugar() {
        System.out.println(nombre + " quiere jugar.");
    }

    public void comer() {
        System.out.println(nombre + " está comiendo.");
    }

    public static void main(String[] args) {
        Perro miPerro = new Perro("Rex", "Labrador", 3);
        miPerro.ladrar();
        miPerro.jugar();
        miPerro.comer();
    }
}