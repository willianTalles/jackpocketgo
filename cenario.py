#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cenario.py

from cordenada_cenario import CordenadaCenario as Cordenada
from grafo import Grafo

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

        arestasGrafo = grafo.get_arestas()

        for pontoA, pontoB in arestasGrafo:
            print( "%s - %s distancia %s" %( pontoA, pontoB, pontoA.get_peso( pontoB ) ) )
            print( "rotulo do pontoA, linha: %s, coluna: %s" %( pontoA.get_rotulo()[0], pontoA.get_rotulo()[1] ) )
            print( self._converterLetraEmPosicaoDaMatriz( pontoA.get_rotulo()[0] ) )


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

    def _converterLetraEmPosicaoDaMatriz(self, letra):
        
        if letra == "A":
            return 1
        elif letra == "B":
            return 2
        elif letra == "C":
            return 3
        elif letra == "D":
            return 4
        elif letra == "E":
            return 5
        elif letra == "F":
            return 6
        elif letra == "G":
            return 7
        elif letra == "H":
            return 8
        elif letra == "I":
            return 9
        elif letra == "J":
            return 10
        elif letra == "K":
            return 11
        elif letra == "L":
            return 12
        elif letra == "M":
            return 13
        elif letra == "N":
            return 14
        elif letra == "O":
            return 15
        elif letra == "P":
            return 16
        else:
            print("Se leu e não entendeu? Se fudeu!")
            return None

    def imprimeCenario( self ):
        for i in range( self.DIMENSAO ):
            for j in range( self.DIMENSAO ):
                print( self.cenarioMatriz[i][j], end="" )
            print("\n")