def main():
    import networkx as nx

    # Crear un grafo dirigido para representar las relaciones
    G = nx.DiGraph()

    # Agregar nodos de recetas
    for _, row in recetas.iterrows():
        G.add_node(row['receta_id'], name=row['nombre'], description=row['descripción'], difficulty=row['dificultad'], preparation_time=row['tiempo_preparación'], allergens=row['alergenos'], category=row['categoria'])

    # Agregar nodos de ingredientes
    for _, row in ingredientes.iterrows():
        G.add_node(row['ingrediente_id'], name=row['nombre'], type=row['tipo'])

    # Agregar aristas entre recetas e ingredientes
    for _, row in recetas_ingredientes.iterrows():
        G.add_edge(row['receta_id'], row['ingrediente_id'])

    # Función para recomendar recetas a un usuario
    def recommend_recetas(user_id):
        recommended_recetas = []
        for receta_id in G.neighbors(user_id):
            for neighbor_receta_id in G.neighbors(receta_id):
                if neighbor_receta_id not in recommended_recetas:
                    recommended_recetas.append(neighbor_receta_id)
        return recommended_recetas

    # Funciones para las opciones del menú
    def mostrar_recomendaciones_generales(user_id):
        print("Recomendaciones generales para el usuario {}:".format(user_id))
        recommended_recetas = recommend_recetas(user_id)
        for receta_id in recommended_recetas:
            print("- Receta ID {}: {}".format(receta_id, G.nodes[receta_id]['name']))

    def mostrar_desayuno(user_id):
        print("Opciones de desayuno para el usuario {}:".format(user_id))
        # Implementa la lógica para mostrar opciones de desayuno

    def mostrar_almuerzo(user_id):
        print("Opciones de almuerzo para el usuario {}:".format(user_id))
        # Implementa la lógica para mostrar opciones de almuerzo

    def mostrar_cena(user_id):
        print("Opciones de cena para el usuario {}:".format(user_id))
        # Implementa la lógica para mostrar opciones de cena

    def editar_informacion(user_id):
        print("Editar información para el usuario {}:".format(user_id))
        # Implementa la lógica para editar información del usuario

    # Ejemplo de uso
    user_id = 1
    while True:
        print("\nMenú:")
        print("1. Recomendaciones generales")
        print("2. Desayuno")
        print("3. Almuerzo")
        print("4. Cena")
        print("5. Editar información")
        print("6. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_recomendaciones_generales(user_id)
        elif opcion == "2":
            mostrar_desayuno(user_id)
        elif opcion == "3":
            mostrar_almuerzo(user_id)
        elif opcion == "4":
            mostrar_cena(user_id)
        elif opcion == "5":
            editar_informacion(user_id)
        elif opcion == "6":
            print("Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")