import os
import gestion_bases_datos
import Recomendacion

def cargar_usuarios(filename):
    usuarios = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            next(file)  
            for line in file:
                data = line.strip().split('|')
                if len(data) == 10:  
                    usuarios.append({
                        "tipo_usuario": data[0].strip(),
                        "user_id": int(data[1].strip()),  
                        "nombre": data[2].strip(),
                        "apellido": data[3].strip(),
                        "correo": data[4].strip(),
                        "experiencia_cocina_id": int(data[5].strip()),  
                        "alimentos_favoritos": data[6].strip(),
                        "alergias": data[7].strip(),
                        "usuario": data[8].strip(),
                        "contraseña": data[9].strip()
                    })
                else:
                    print("Línea con formato incorrecto encontrada y omitida.")
    return usuarios

def guardar_usuario(filename, usuario):
    with open(filename, 'a') as file:
        file.write('|'.join(str(value) for value in usuario.values()) + '\n')

def registrar_usuario(filename):
    print("Registro de nuevo usuario")
    tipo_usuario = input("Tipo de Usuario (admin/usuario): ")
    user_id = int(input("ID de Usuario: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    experiencia_cocina_id = int(input("Experiencia en cocina (ID): "))
    alimentos_favoritos = input("Alimentos Favoritos: ")
    alergias = input("Alergias: ")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    nuevo_usuario = {
        "tipo_usuario": tipo_usuario,
        "user_id": user_id,
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "experiencia_cocina_id": experiencia_cocina_id,
        "alimentos_favoritos": alimentos_favoritos,
        "alergias": alergias,
        "usuario": usuario,
        "contraseña": contraseña
    }

    guardar_usuario(filename, nuevo_usuario)
    print("Usuario registrado exitosamente.\n")

def iniciar_sesion(filename):
    print("Iniciar sesión")
    usuarios = cargar_usuarios(filename)
    usuario_input = input("Nombre de usuario: ")
    contraseña_input = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["usuario"] == usuario_input and usuario["contraseña"] == contraseña_input:
            print(f"Bienvenido, {usuario['nombre']} {usuario['apellido']}")
            return usuario
    print("Nombre de usuario o contraseña incorrectos.")
    return None

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    return lineas

def escribir_archivo(nombre_archivo, lineas):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(lineas)

def modificar_usuario(nombre_archivo, user_id, campo, nuevo_valor):
    lineas = leer_archivo(nombre_archivo)
    cabecera = lineas[0]
    datos = lineas[1:]
    
    # Encontrar el índice del campo que queremos modificar
    campos = [campo.strip() for campo in cabecera.strip().split('|')]
    if campo not in campos:
        raise ValueError(f"Campo '{campo}' no encontrado en el archivo.")
    indice_campo = campos.index(campo)
    
    # Buscar el usuario y modificar el campo especificado
    usuario_encontrado = False
    for i, linea in enumerate(datos):
        partes = [parte.strip() for parte in linea.strip().split('|')]
        if int(partes[1]) == user_id:  # Índice 1 corresponde a user_id
            partes[indice_campo] = nuevo_valor
            datos[i] = '|'.join(partes) + '\n'
            usuario_encontrado = True
            break
    
    if not usuario_encontrado:
        raise ValueError(f"Usuario con user_id '{user_id}' no encontrado.")
    
    # Escribir los datos modificados de vuelta en el archivo
    escribir_archivo(nombre_archivo, [cabecera] + datos)
    print(f"Usuario con user_id '{user_id}' modificado. Campo '{campo}' actualizado a '{nuevo_valor}'.")

def menu_admin():
    print("Menú de Administrador")
    gestion_bases_datos.main()
    # Agrega aquí las opciones y funcionalidades específicas del administrador
    pass

def menu_usuario(usuario):
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Mostrar recomendaciones")
        print("2. Modificar informacion")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            print("Recomendaciones")
            user_id = int(usuario["user_id"])
            Recomendacion.main(user_id)
        elif opcion == '2':
            user_id = int(usuario["user_id"])
            campo = input("Ingresa el campo que deseas modificar: ")
            nuevo_valor = input(f"Ingresa el nuevo valor para el campo '{campo}': ")
            try:
                modificar_usuario("Usuarios.txt", user_id, campo, nuevo_valor)
            except ValueError as e:
                print(e)
        elif opcion == '3':
            print("Saliendo del menú de usuario.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

def main():
    filename = "Usuarios.txt"
    while True:
        print("Bienvenido al sistema")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")
        
        if opcion == '1':
            registrar_usuario(filename)
        elif opcion == '2':
            usuario = iniciar_sesion(filename)
            if usuario:
                if usuario["tipo_usuario"] == "Admin":
                    menu_admin()
                elif usuario["tipo_usuario"] == "Usuario":
                    menu_usuario(usuario)
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.")

if __name__ == "__main__":
    main()