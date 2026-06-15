
def saludar(nombre):
    return f"¡Hola, {nombre}!"

def main():
    name = input("Ingresa tu nombre: ")
    mensaje = saludar(name)
    print(mensaje)

if __name__ == "__main__":
    main()