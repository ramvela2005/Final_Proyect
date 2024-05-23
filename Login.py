import networkx as nx

# Definir el grafo de usuarios
grafo_usuarios = nx.DiGraph()

# Usuarios administradores
usuarios_admin = []

# Función para registrar un nuevo usuario
def registrar_usuario():
    # Pedir información del nuevo usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    experiencia_cocina_id = input("Ingrese su nivel de experiencia en cocina (1: Fácil, 2: Intermedio, 3: Avanzado): ")
    alimentos_favoritos = input("Ingrese sus alimentos favoritos separados por coma: ")
    alergias = input("Ingrese sus alergias separadas por coma: ")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Agregar el nuevo usuario al grafo
    grafo_usuarios.add_node(usuario, nombre=nombre, apellido=apellido, correo=correo, experiencia_cocina_id=experiencia_cocina_id, 
                            alimentos_favoritos=alimentos_favoritos, alergias=alergias, contraseña=contraseña)

# Función para iniciar sesión
def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Verificar si el usuario existe en el grafo
    if usuario in grafo_usuarios:
        # Verificar si la contraseña es correcta
        if grafo_usuarios.nodes[usuario]['contraseña'] == contraseña:
            tipo_usuario = "usuario" if usuario not in usuarios_admin else "usuario admin"
            print("Inicio de sesión exitoso. Bienvenido, {}.".format(tipo_usuario))
            return usuario, tipo_usuario
        else:
            print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
    else:
        print("El usuario {} no existe. Por favor, regístrese primero.".format(usuario))
    return None, None

# Funciones para las opciones de usuario
def recomendaciones_generales(usuario):
    print("Recomendaciones generales para {}.".format(usuario))

def desayuno(usuario):
    print("Opciones de desayuno para {}.".format(usuario))

def almuerzo(usuario):
    print("Opciones de almuerzo para {}.".format(usuario))

def cena(usuario):
    print("Opciones de cena para {}.".format(usuario))

def editar_info(usuario):
    print("Editar información para {}.".format(usuario))

# Funciones para las opciones de usuario admin
def cambiar_base_datos_usuarios():
    print("Cambiar la base de datos de usuarios.")

def cambiar_base_datos_recetas():
    print("Cambiar la base de datos de recetas.")

def cambiar_base_datos_ingredientes():
    print("Cambiar la base de datos de ingredientes.")

def cambiar_base_datos_recetas_ingredientes():
    print("Cambiar la base de datos de recetas-ingredientes.")

def cambiar_tipo_usuario():
    print("Cambiar el tipo de usuario.")

# Menú de opciones
menu_principal = """
--- Menú ---
1. Registrarse
2. Iniciar sesión
3. Salir
"""

menu_usuario = """
--- Opciones ---
1. Recomendaciones generales
2. Desayuno
3. Almuerzo
4. Cena
5. Editar información
6. Cerrar sesión
"""

menu_usuario_admin = """
--- Opciones ---
1. Cambiar base de datos de usuarios
2. Cambiar base de datos de recetas
3. Cambiar base de datos de ingredientes
4. Cambiar base de datos de recetas-ingredientes
5. Cambiar tipo de usuario
6. Cerrar sesión
"""

# Función para mostrar y seleccionar opciones de menú
def mostrar_menu(menu):
    print(menu)
    opcion = input("Seleccione una opción: ")
    return opcion

# Función principal
def main():
    while True:
        opcion = mostrar_menu(menu_principal)
        
        if opcion == "1":  # Registrarse
            #registrar_usuario()
        elif opcion == "2":  # Iniciar sesión
            usuario, tipo_usuario = iniciar_sesion()
            if tipo_usuario == "usuario":
                while True:
                    opcion_usuario = mostrar_menu(menu_usuario)
                    if opcion_usuario == "1":
                        recomendaciones_generales(usuario)
                    elif opcion_usuario == "2":
                        desayuno(usuario)
                    elif opcion_usuario == "3":
                        almuerzo(usuario)
                    elif opcion_usuario == "4":
                        cena(usuario)
                    elif opcion_usuario == "5":
                        editar_info(usuario)
                    elif opcion_usuario == "6":
                        print("Cerrando sesión.")
                        break
                    else:
                        print("Opción inválida.")
            elif tipo_usuario == "usuario admin":
                while True:
                    opcion_admin = mostrar_menu(menu_usuario_admin)
                    if opcion_admin == "1":
                        cambiar_base_datos_usuarios()
                    elif opcion_admin == "2":
                        cambiar_base_datos_recetas()
                    elif opcion_admin == "3":
                        cambiar_base_datos_ingredientes()
                    elif opcion_admin == "4":
                        cambiar_base_datos_recetas_ingredientes()
                    elif opcion_admin == "5":
                        cambiar_tipo_usuario()
                    elif opcion_admin == "6":
                        print("Cerrando sesión.")
                        break
                    else:
                        print("Opción inválida.")
        elif opcion == "3":  # Salir
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

