#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cenario.py

from cordenada_cenario import CordenadaCenario as Cordenada

class Cenario:
    
    def __init__( self ):
        super().__init__()
        self.DIMENSAO = 16
        self.cenarioMatriz = []
        self.PAREDEVERTICAL = '|'
        self.PAREDEHORIZONTAL = '='
        self.OBSTACULO = '#'
        self.CAMINHO = '.'
        

    def desenha( self, grafo = None ):
        self._geraCenarioVazio()

    def _geraCenarioVazio( self ):
        
        for i in range( self.DIMENSAO ):
            linha = [] # lista vazia
            for j in range( self.DIMENSAO ):
	            linha.append( self.CAMINHO )
	        
            # coloque linha na matriz
            self.cenarioMatriz.append( linha )
        self._geraParedesExternas()

    def _geraParedesExternas( self ):
        for i in range( 0, self.DIMENSAO ):
            for j in range( 0, self.DIMENSAO ):
                cordenada = Cordenada( i, j )
                  
                if( cordenada.ehParedeVertical( self.DIMENSAO ) ):
                    self.cenarioMatriz[i][j] = self.PAREDEVERTICAL

                elif( cordenada.ehParedeHorizontal( self.DIMENSAO ) ):
                    self.cenarioMatriz[i][j] = self.PAREDEHORIZONTAL

    def ehParedeVertical( self, cordenada ):
        if( self.cordenada["x"] != 0 and self.cordenada["x"] != self.dimensaoCenario
            and self.cordenada["y"] == 0 or self.cordenada["y"] == self.dimensaoCenario ):
            return True

    def imprimeCenario( self ):
        for i in range( self.DIMENSAO ):
            for j in range( self.DIMENSAO ):
                print( self.cenarioMatriz[i][j], end="" )
            print("\n")