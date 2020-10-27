#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from grafo import Grafo
from vertice import Vertice
from cenario import Cenario

if __name__ == "__main__":

    cenario = Cenario()
    cenario.desenha()
    cenario.imprimeCenario()
    
    g1 = Grafo(False) #cria grafo não direcionado
    g1.ler_arquivo("cenario.txt")

    a = g1.get_arestas()

    for t,v in a:
        print("%s - %s distancia %s" %( t, v, t.get_peso( v ) ) )