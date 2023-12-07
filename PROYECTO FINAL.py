import networkx as nx
import matplotlib.pyplot as plt#Importamos las librerias 
import tkinter as tk
from tkinter import ttk

def calcular_ruta():
    # Obtenemos los nodos de inicio y destino desde las opciones creadas en la interfaz gráfica
    inicio = combo_inicio.get()
    destino = combo_destino.get()
    
    # Calcular la ruta más corta y su longitud
    camino_corto = nx.shortest_path(Grafo, inicio, destino, weight='weight')
    tiempo = nx.shortest_path_length(Grafo, inicio, destino, weight='weight')
    
    # leyenda con la ruta más corta y su longitud
    leyenda = f"El Camino Corto es: {camino_corto} y toma {tiempo} Kilómetros"
    label_resultado.config(text=leyenda)

    # Creamos y mostramos el gráfico con la ruta más corta
    pos = nx.spring_layout(Grafo)
    
    # Resaltamos la ruta más corta
    edge_list = [(camino_corto[i], camino_corto[i + 1]) for i in range(len(camino_corto) - 1)]
    
    # Con esto cambiamos el color de todos los nodos a lightblue
    node_colors = ['lightblue' for _ in Grafo.nodes]
    
    # Crear un mapeo de nodos a índices numéricos
    node_to_index = {node: index for index, node in enumerate(Grafo.nodes)}
    
    # Cambiar el color del nodo de inicio a rojo
    node_colors[node_to_index[inicio]] = 'yellow'
    
    # Cambiar el color del nodo de destino a rosa
    node_colors[node_to_index[destino]] = 'pink'
    
    # Dibujar nodos con etiquetas de distancia
    nx.draw(Grafo, pos, node_size=1300, node_color=node_colors, font_size=8, font_weight='bold', with_labels=True)
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=nx.get_edge_attributes(Grafo, "weight"))
    
    # Resaltar la ruta más corta con color rojo
    nx.draw_networkx_edges(Grafo, pos, edgelist=edge_list, edge_color='red', width=2)
    
    # Mostrar el título del gráfico
    plt.title("Grafo con la Ruta Más Corta Entre Los Distritos de la Provincia de Coclé")
    
    # Guardar el gráfico como una imagen PNG
    plt.savefig("Graph.png", format="PNG")
    
    # Mostrar el gráfico
    plt.show()

# Creación el grafo
Grafo = nx.Graph()
Grafo.add_node("Aguadulce")
Grafo.add_node("Penonomé")
Grafo.add_node("Antón")
Grafo.add_node("Natá")
Grafo.add_node("La Pintada")
Grafo.add_node("Olá")
Grafo.add_node("Cienega Vieja")
Grafo.add_node("Río Grande")
Grafo.add_node("Mata Palo")
Grafo.add_node("Llano Marin")
Grafo.add_node("Llano Grande")

Grafo.add_edge("Antón", "Penonomé", weight=34.9)
Grafo.add_edge("Penonomé", "La Pintada", weight=18.3)
Grafo.add_edge("La Pintada", "Olá", weight=44.5)
Grafo.add_edge("Natá", "Olá", weight=37.6)
Grafo.add_edge("Natá", "Aguadulce", weight=19.3)
Grafo.add_edge("Antón", "Natá", weight=78.2)
Grafo.add_edge("Cienega Vieja","Penonomé", weight=20.5)
Grafo.add_edge("Río Grande","Aguadulce", weight=33.2)
Grafo.add_edge("Mata Palo","La Pintada", weight=39.1)
Grafo.add_edge("Llano Marin","Natá", weight=52.4)
Grafo.add_edge("Antón","Llano Grande", weight=35.1)

# interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de Ruta Más Corta En la provincia de Coclé")

#  etiquetas y widgets para nodos de inicio y destino
etiqueta_inicio = ttk.Label(ventana, text="Lugar de Inicio:")
etiqueta_inicio.grid(column=0, row=0, padx=10, pady=10)

combo_inicio = ttk.Combobox(ventana, values=list(Grafo.nodes), width=15)
combo_inicio.grid(column=1, row=0, padx=10, pady=10)

etiqueta_destino = ttk.Label(ventana, text="Destino:")
etiqueta_destino.grid(column=0, row=1, padx=10, pady=10)

combo_destino = ttk.Combobox(ventana, values=list(Grafo.nodes), width=15)
combo_destino.grid(column=1, row=1, padx=10, pady=10)

#  botón para calcular la ruta
boton_calcular = ttk.Button(ventana, text="Mostrar Ruta", command=calcular_ruta)
boton_calcular.grid(column=0, row=2, columnspan=2, pady=10)

# Etiquetas para mostrar el resultado
label_resultado = ttk.Label(ventana, text="")
label_resultado.grid(column=0, row=3, columnspan=2, pady=10)

# Iniciamos el bucle de la interfaz gráfica
ventana.mainloop()
