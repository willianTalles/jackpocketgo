#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#guarda.py#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#guarda.py

from bellman_ford import BellManFord

class Guarda():
    def __init__( self, grafo ):
        self.posicao = grafo.get_vertices()[4]
        self.caminhosDoCenario = grafo
    
    def gerarCaminhoParaPegarJack( self, destino ):
        destinoPrincipal = None
        destidoSecundario = None

        for destinoPrincipal, destidoSecundario in destino:
            print("Meu destino principal é:", destinoPrincipal, "meu destino secundario é:", destidoSecundario)

        self._procurarMenorCaminhaAteJackComBellmanFord( self.posicao, destinoPrincipal )

    def _procurarMenorCaminhaAteJackComBellmanFord( self, verticeOrigem, verticeDestino):
        verticesDoCaminho = []
        
        bellmanFord = BellManFord()
        if bellmanFord.executaBellManFord( self.caminhosDoCenario, verticeOrigem ):
            verticesDoCaminho = bellmanFord.caminhoMinimoBellmanFord( self.caminhosDoCenario, verticeOrigem, verticeDestino )
        
        for vertice in verticesDoCaminho:
            print(vertice)