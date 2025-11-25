class Producto {
    private String nombre;
    private double precio;
    private int stock;
    
    // Constructor
    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }
    
    // Método para mostrar información del producto
    public void mostrarInfo() {
        System.out.println("=== Información del Producto ===");
        System.out.println("Nombre: " + nombre);
        System.out.println("Precio: $" + precio);
        System.out.println("Stock: " + stock + " unidades");
        System.out.println();
    }
    
    // Método para actualizar el stock
    public void actualizarStock(int cantidad) {
        stock += cantidad;
        System.out.println("Stock actualizado. Nuevo stock: " + stock + " unidades\n");
    }
    
    // Método para aplicar descuento
    public void aplicarDescuento(double porcentaje) {
        double descuento = precio * (porcentaje / 100);
        precio -= descuento;
        System.out.println("Descuento aplicado del " + porcentaje + "%");
        System.out.println("Nuevo precio: $" + precio + "\n");
    }
    
    // Método main para probar la clase
    public static void main(String[] args) {
        // Crear un objeto Producto
        Producto producto1 = new Producto("Laptop Dell", 1200.50, 5);
        
        // Probar mostrarInfo()
        producto1.mostrarInfo();
        
        // Probar actualizarStock()
        System.out.println("--- Actualizando stock ---");
        producto1.actualizarStock(10);
        
        // Probar aplicarDescuento()
        System.out.println("--- Aplicando descuento ---");
        producto1.aplicarDescuento(15);
        
        // Mostrar información final
        System.out.println("--- Información Final ---");
        producto1.mostrarInfo();
    }
}