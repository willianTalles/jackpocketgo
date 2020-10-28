#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from grafo import Grafo
from vertice import Vertice
from cenario import Cenario
from camera import Camera

if __name__ == "__main__":
    
    grafo = Grafo(False) #cria grafo não direcionado
    grafo.ler_arquivo("cenario.txt")

    cenario = Cenario()
    cenario.desenha( grafo )
    cenario.imprimeCenario()

    Camera = Camera( "PP", grafo.get_vertices() ) 