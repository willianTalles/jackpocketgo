#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from grafo import Grafo
from vertice import Vertice
from cenario import Cenario
#from dijkstra import dijkstra
from bellman_ford import BellManFord

if __name__ == "__main__":
    
    grafo = Grafo(False) #cria grafo não direcionado
    grafo.ler_arquivo("cenario.txt")

    #cenario = Cenario()
    #cenario.desenha( grafo )
    #cenario.imprimeCenario()

    bmf = BellManFord()
    print(bmf)
    verticeOrigem = grafo.get_vertices()[3].get_rotulo()
    verticeDestino = grafo.get_vertices()[64].get_rotulo()
    
    caminho = []
    if bmf.executaBellManFord( grafo, verticeOrigem ):
        #caminho = bmf.caminhoMinimoBellmanFord(grafo,verticeOrigem,verticeDestino)
        caminho = bmf.caminhoMinimoBellmanFord(grafo,verticeOrigem,verticeDestino)
        for c in caminho:
            print(c[::-1])
'''
    if bmf.executaBellManFord(grafo ,verticeOrigem):
        for v in grafo.get_vertices():
            caminho = [v.get_rotulo()]
            #bmf.caminhoMinino(v, caminho)
            bmf.caminhoMinimo( v, caminho )
            print ('O menor caminho é: %s com custo %d.' %(caminho[::-1], v.get_distancia()))
        
        else:
            print("Ciclo negativo encontrado")
'''
    

