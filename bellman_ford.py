#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#bellman_ford.py

from grafo import Grafo
from vertice import Vertice

class BellManFord:
    '''
    Classe que encontra o menor caminho em um grafo a partir de
    uma origem e um destino utilizando o algoritmo de Bellman-Ford.
    Teremos para nossa origem a posição de um guarda. Para o nosso
    destino teremos a posição de Jack.
    '''

    def executaBellManFord( self, grafo, origem ):
        '''
        Método para execução da busca do menor caminho.
        param grafo objeto do tipo grafo para realizar a busca
        param origem ponto de partida para o caminho mais curto
        '''
        self._inicializarGrafo( grafo, origem )

        for u in grafo.get_vertices():
            for u,v in grafo.get_arestas():
                if v.get_visitado():
                    continue
                
                self._executaRelaxamento( u, v )
        
        for u,v in grafo.get_arestas():
            if v.get_distancia() > u.get_distancia() + u.get_peso( v ):
                return False
        
        return True                

    
    def _inicializarGrafo( self, grafo, origem ):
        for v in grafo.get_vertices():
            v.set_distancia( float('Infinity') )
    
        grafo.get_vertice( origem ).set_distancia( 0 )
    
    def _executaRelaxamento( self, u, v ):
        if v.get_distancia() > u.get_distancia() + u.get_peso( v ):
            v.set_distancia( u.get_distancia() + u.get_peso( v ) )
            v.set_predecessor( u )
    
    def caminhoMinimo( self, v, caminho ):
        if v.get_predecessor():
            caminho.append( v.get_predecessor().get_rotulo() )
            self.caminhoMinimo( v.get_predecessor(), caminho )
        
        return
    
    def caminhoMinimoBellmanFord( self, grafo, verticeOrigem, verticeDestino ):
        caminhoEncontrado = []
        for v in grafo.get_vertices():
                
            caminho = [v.get_rotulo()]
            self.caminhoMinimo( v,caminho )
            #print ('O menor caminho é: %s com custo %d.' %(caminho[::-1], v.get_distancia()))

            comprimentoCaminho = len(caminho)
            if(caminho[comprimentoCaminho-1] == verticeOrigem and caminho[0] == verticeDestino):
                caminhoEncontrado.append(caminho)
        
        return caminhoEncontrado