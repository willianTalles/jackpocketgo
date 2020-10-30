#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#guarda.py#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#guarda.py

from bellman_ford import BellManFord
from dijkstra import Dijkstra

class Guarda():
    def __init__( self, grafo ):
        self.posicao = grafo.get_vertices()[4]
        self.caminhosDoCenario = grafo
    
    def gerarCaminhoParaPegarJack( self, destino ):
        destinoPrincipal = None
        destidoSecundario = None

        for destinoPrincipal, destidoSecundario in destino:
            print("Meu destino principal é:", destinoPrincipal, "meu destino secundario é:", destidoSecundario)

        self._procurarMenorCaminhoAteJack( self.posicao, destinoPrincipal )

    def _procurarMenorCaminhoAteJack( self, verticeOrigem, verticeDestino):
        verticesDoCaminho = []

        print("Guarda na posição: ", self.posicao)
        print("Encontrou caminho mais curto até Jack: ", end="")

        DKST = Dijkstra()
        DKST.executaDijkstra(self.caminhosDoCenario, verticeOrigem.get_rotulo())
        caminho = DKST.caminhoMinimoDijkstra(self.caminhosDoCenario, verticeOrigem.get_rotulo(), verticeDestino.get_rotulo() )
        for c in caminho:
            print(c[::-1])