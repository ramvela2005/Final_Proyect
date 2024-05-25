import pandas as pd
import networkx as nx

def cargar_datos_usuarios(filepath):
    usuarios_cols = ["tipo_usuario", "user_id", "nombre", "apellido", "correo", "experiencia_cocina_id", "alimentos_favoritos", "alergias", "usuario", "contraseña"]
    usuarios = pd.read_csv(filepath, sep='|', header=0, names=usuarios_cols)
    usuarios = usuarios.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    usuarios["user_id"] = pd.to_numeric(usuarios["user_id"], errors='coerce')
    usuarios = usuarios.dropna(subset=["user_id"])
    usuarios["user_id"] = usuarios["user_id"].astype(int)
    return usuarios

def cargar_datos_recetas(filepath):
    recetas_cols = ["receta_id", "nombre", "descripcion", "dificultad", "tiempo_preparacion", "alergenos", "categoria"]
    recetas = pd.read_csv(filepath, sep='|', header=0, names=recetas_cols)
    recetas = recetas.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return recetas

def construir_grafo_recetas(recetas):
    G = nx.Graph()
    for idx, receta in recetas.iterrows():
        G.add_node(receta["receta_id"], descripcion=receta["descripcion"], dificultad=receta["dificultad"], alergenos=receta["alergenos"], categoria=receta["categoria"])
    for i in range(len(recetas)):
        for j in range(i + 1, len(recetas)):
            if recetas.iloc[i]["dificultad"] == recetas.iloc[j]["dificultad"]:
                G.add_edge(recetas.iloc[i]["receta_id"], recetas.iloc[j]["receta_id"])
    return G

def recomendar_recetas(user_id, usuarios, G):
    if user_id not in usuarios["user_id"].values:
        print(f"El usuario con user_id {user_id} no existe.")
        return []

    user = usuarios[usuarios["user_id"] == user_id].iloc[0]
    experiencia = user["experiencia_cocina_id"]
    favoritos = set(user["alimentos_favoritos"].split(", "))
    alergias = set(user["alergias"].split(", "))

    recomendaciones = []

    for receta_id, data in G.nodes(data=True):
        receta_dificultad = data["dificultad"]
        receta_alergenos = set(data["alergenos"].split(", "))

        if receta_dificultad == experiencia and not receta_alergenos.intersection(alergias):
            recomendaciones.append((receta_id, data["descripcion"]))

    return recomendaciones

def main(user_id):
    usuarios = cargar_datos_usuarios('Usuarios.txt')
    recetas = cargar_datos_recetas('Recetas.txt')
    G = construir_grafo_recetas(recetas)
    recomendaciones = recomendar_recetas(user_id, usuarios, G)
    for rec in recomendaciones:
        print(f"Receta ID: {rec[0]}, Descripción: {rec[1]}")

