edad_input = input("Introduce tu edad: ").strip()
try:
    edad = int(edad_input)
    if edad < 0:
        print("Edad inválida (negativa).")
    elif edad < 13:
        print("Eres un niño.")
    elif edad <= 17:
        print("Eres un adolescente.")
    elif edad <= 64:
        print("Eres un adulto.")
    else:
        print("Eres un adulto mayor.")
except ValueError:
    print("Edad inválida (debe ser un número entero).")

# Este código solicita al usuario que introduzca su edad y clasifica la edad en diferentes categorías.