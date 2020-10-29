#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from grafo import Grafo
from vertice import Vertice
from cenario import Cenario
from camera import Camera
from guarda import Guarda

if __name__ == "__main__":
    
    grafo = Grafo(False) #cria grafo não direcionado
    grafo.ler_arquivo("cenario.txt")

    cenario = Cenario( grafo )
    cenario.desenha( grafo )
    cenario.imprimeCenario()
    
    localizacao = cenario.procurarJackComCamera()

    guarda = Guarda( grafo )
    guarda.gerarCaminhoParaPegarJack( localizacao )
