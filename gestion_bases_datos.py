import os

def cargar_datos(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip().split('|') for line in file.readlines()]
    return []

def guardar_datos(file_path, data):
    with open(file_path, 'w') as file:
        for entry in data:
            file.write('|'.join(entry) + '\n')

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Modificar Experiencia.txt")
    print("2. Modificar RecetasIngredientes.txt")
    print("3. Modificar Usuarios.txt")
    print("4. Modificar Ingredientes.txt")
    print("5. Modificar Recetas.txt")
    print("6. Salir")

def modificar_archivo(file_path):
    datos = cargar_datos(file_path)
    if not datos:
        print("No se encontraron datos en el archivo.")
        return
    
    for i, fila in enumerate(datos):
        print(f"{i + 1}. {fila}")
    
    opcion = input("Ingrese el número de la fila que desea modificar o 'a' para agregar una nueva fila: ")
    
    if opcion.lower() == 'a':
        nueva_fila = input("Ingrese los nuevos datos separados por '|': ")
        datos.append(nueva_fila.split('|'))
    else:
        indice = int(opcion) - 1
        if 0 <= indice < len(datos):
            nueva_fila = input("Ingrese los nuevos datos para esta fila separados por '|': ")
            datos[indice] = nueva_fila.split('|')
        else:
            print("Opción inválida.")
    
    guardar_datos(file_path, datos)
    print("Datos actualizados correctamente.")

def main():
    archivos = {
        "1": "Experiencia.txt",
        "2": "RecetasIngredientes.txt",
        "3": "Usuarios.txt",
        "4": "Ingredientes.txt",
        "5": "Recetas.txt"
    }
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '6':
            break
        elif opcion in archivos:
            modificar_archivo(archivos[opcion])
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()