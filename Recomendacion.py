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