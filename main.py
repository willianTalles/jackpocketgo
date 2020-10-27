#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from grafo import Grafo
from vertice import Vertice
from cenario import Cenario

if __name__ == "__main__":
    
    g1 = Grafo(False) #cria grafo não direcionado
    g1.ler_arquivo("cenario.txt")

    a = g1.get_arestas()

    cenario = Cenario()
    cenario.desenha( g1 )
    cenario.imprimeCenario()