class Producto {
    // Constructor
    constructor(nombre, precio, stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }
    
    // Método para mostrar información del producto
    mostrarInfo() {
        console.log("=== Información del Producto ===");
        console.log("Nombre: " + this.nombre);
        console.log("Precio: $" + this.precio);
        console.log("Stock: " + this.stock + " unidades");
        console.log();
    }
    
    // Método para actualizar el stock
    actualizarStock(cantidad) {
        this.stock += cantidad;
        console.log("Stock actualizado. Nuevo stock: " + this.stock + " unidades\n");
    }
    
    // Método para aplicar descuento
    aplicarDescuento(porcentaje) {
        const descuento = this.precio * (porcentaje / 100);
        this.precio -= descuento;
        console.log("Descuento aplicado del " + porcentaje + "%");
        console.log("Nuevo precio: $" + this.precio + "\n");
    }
}

// Crear un objeto Producto y probar los métodos
const producto1 = new Producto("Laptop Dell", 1200.50, 5);

// Probar mostrarInfo()
producto1.mostrarInfo();

// Probar actualizarStock()
console.log("--- Actualizando stock ---");
producto1.actualizarStock(10);

// Probar aplicarDescuento()
console.log("--- Aplicando descuento ---");
producto1.aplicarDescuento(15);

// Mostrar información final
console.log("--- Información Final ---");
producto1.mostrarInfo();