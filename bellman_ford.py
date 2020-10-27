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

        for u in grafo.getListaVertices():
            for u,v in grafo.getArestas():
                if v.getVisitado():
                    continue
                
                self._executaRelaxamento( u, v )
        
        for u,v in grafo.getArestas():
            if v.getDistancia() > u.getDistancia() + u.getCusto( v ):
                return False
        
        return True                

    
    def _inicializarGrafo( self, grafo, origem ):
        for v in grafo.getListaVertices():
            v.setDistancia( float('inf') )
        
        grafo.getVertice( origem ).setDistancia( 0 )
    
    def _executaRelaxamento( self, u, v ):
        if v.getDistancia() > u.getDistancia() + u.getCusto( v ):
            v.setDistancia( u.getDistancia() + u.getCusto( v ) )
            v.setAnterior( u )
    
    def _caminhoMinimo( self, v, caminho ):
        if v.getAnterior():
            caminho.append( v.getAnterior().getRotulo() )
            self._caminhoMinimo( v.getAnterior(), caminho )
        
        return


        