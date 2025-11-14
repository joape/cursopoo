let edad = prompt("¿Cuál es tu edad?");

if (edad === null) {
    alert("Cancelaste la operación.");
} else if (isNaN(edad) || edad < 0) {
    alert("Por favor ingresa una edad válida.");
} else {
    edad = parseInt(edad);
    
    if (edad < 13) {
        alert("Eres un niño.");
    } else if (edad >= 13 && edad <= 17) {
        alert("Eres un adolescente.");
    } else if (edad >= 18 && edad <= 64) {
        alert("Eres un adulto.");
    } else {
        alert("Eres un adulto mayor.");
    }
}