# Solicita la edad y determina si la persona es mayor o menor de edad
edad_input = input("Introduce la edad: ").strip()
if not edad_input.isdigit():
    print("Edad inválida (debe ser un número entero no negativo).")
else:
    edad = int(edad_input)
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")