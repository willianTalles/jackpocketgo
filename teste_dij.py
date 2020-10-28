#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from grafo import Grafo
from vertice import Vertice
from cenario import Cenario
from dijkstra import Dijkstra

if __name__ == "__main__":
    
    grafo = Grafo(False) #cria grafo não direcionado
    grafo.ler_arquivo("cenario.txt")

    dij = Dijkstra()
    
    print(dij)
    
    verticeOrigem = grafo.get_vertices()[3].get_rotulo()
    verticeDestino = grafo.get_vertices()[64].get_rotulo()
    
    caminho = []
    
    if dij.executaDijkstra(grafo, verticeOrigem):
        caminho = dij.caminhoMinimoDijkstra(grafo, verticeOrigem, verticeDestino)
        
        for c in caminho:
            print(c[::-1])