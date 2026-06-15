
def saludar(nombre):
    return f"¡Hola, {nombre}!"

def main():
    nombre = input("Ingresa tu nombre: ")
    mensaje = saludar(nombre)
    print(mensaje)

if __name__ == "__main__":
    main()