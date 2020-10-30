#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cenario.py

from cordenada_cenario import CordenadaCenario as Cordenada
from grafo import Grafo
from camera import Camera

class Cenario:
    
    def __init__( self, grafo ):
        super().__init__()
        self.camera = Camera( grafo.get_vertices()[6], grafo.get_vertices() )
        self.PAREDEHORIZONTAL = '='
        self.PAREDEVERTICAL = '|'
        self.cenarioMatriz = []
        self.OBSTACULO = '#'
        self.DIMENSAO = 18
        self.CAMINHO = '.'
        self.JACK = 'J'
        self.GUARDA = 'G'

    def desenha( self, grafo = None ):
        self._geraCenarioVazio()

        arestasGrafo = grafo.get_arestas()

        for pontoA, pontoB in arestasGrafo:
            # print( "%s - %s distancia %s" %( pontoA, pontoB, pontoA.get_peso( pontoB ) ) )
            # print( "rotulo do pontoA, linha: %s, coluna: %s" %( pontoA.get_rotulo()[0], pontoA.get_rotulo()[1] ) )
            # print( self._converterLetraEmPosicaoDaMatriz( pontoA.get_rotulo()[0] ) )
            
            linhaPontoA = pontoA.get_rotulo()[0]
            colunaPontoA = pontoA.get_rotulo()[1]

            linhaPontoB = pontoB.get_rotulo()[0]
            colunaPontoB = pontoB.get_rotulo()[1]

            linhaCenarioMatriz = self._converterLetraEmPosicaoDaMatriz( linhaPontoA )
            colunaCenarioMatriz = self._converterLetraEmPosicaoDaMatriz( colunaPontoA )

            self.cenarioMatriz[ linhaCenarioMatriz ][ colunaCenarioMatriz ] = self.CAMINHO

            # gostaria de refatorar esse if
            if linhaPontoA == linhaPontoB:
                for contadorCaminho in range( int( pontoA.get_peso( pontoB ) ) - 1 ):
                    colunaCenarioMatriz = colunaCenarioMatriz + 1
                    if colunaCenarioMatriz < self._converterLetraEmPosicaoDaMatriz( colunaPontoB ) and colunaCenarioMatriz < self.DIMENSAO - 1:
                        self.cenarioMatriz[ linhaCenarioMatriz ][ colunaCenarioMatriz ] = self.CAMINHO
            else:
                for contadorCaminho in range( int( pontoA.get_peso( pontoB ) ) - 1 ):
                    linhaCenarioMatriz = linhaCenarioMatriz + 1
                    if linhaCenarioMatriz < self._converterLetraEmPosicaoDaMatriz( linhaPontoB ) and linhaCenarioMatriz < self.DIMENSAO - 1:
                        self.cenarioMatriz[ linhaCenarioMatriz ][ colunaCenarioMatriz ] = self.CAMINHO

        self.cenarioMatriz[5][5] = self.JACK

    def _geraCenarioVazio( self ):
        
        for i in range( self.DIMENSAO ):
            linha = [] # lista vazia
            for j in range( self.DIMENSAO ):
	            linha.append( self.OBSTACULO )
	        
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

    def _converterLetraEmPosicaoDaMatriz( self, letra ):   
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
    
    
    def procurarJackComCamera( self ):
    # esse metodo retorna uma tupla com a aresta 
    # (verticeA, VerticeB) que está Jack
        print("Procurando Jack com a câmera...")
        posicaoDaCamera = self.camera.getPosicao()
        campoDeVisaoDaCamera = self.camera.getCampoDeVisao()

        localizacaoDeJack = set()
        
        for verticeAdjacente in campoDeVisaoDaCamera:
            
            linhaposicaoDaCamera = posicaoDaCamera.get_rotulo()[0]
            linhaposicaoDaCamera = self._converterLetraEmPosicaoDaMatriz( linhaposicaoDaCamera )

            colunaposicaoDaCamera = posicaoDaCamera.get_rotulo()[1]
            colunaposicaoDaCamera = self._converterLetraEmPosicaoDaMatriz( colunaposicaoDaCamera )

            linhaverticeAdjacente = verticeAdjacente.get_rotulo()[0]
            linhaverticeAdjacente = self._converterLetraEmPosicaoDaMatriz( linhaverticeAdjacente )
            
            colunaverticeAdjacente = verticeAdjacente.get_rotulo()[1]
            colunaverticeAdjacente = self._converterLetraEmPosicaoDaMatriz( colunaverticeAdjacente )
            
            if linhaposicaoDaCamera == linhaverticeAdjacente:
                if colunaposicaoDaCamera > colunaverticeAdjacente:
                    for contadorDeCaminho in range(4):
                        colunaverticeAdjacente = colunaverticeAdjacente + 1
                        
                        if self.cenarioMatriz[ linhaverticeAdjacente ][ colunaverticeAdjacente] == self.JACK:
                            print("1 Detectou jack na aresta!", posicaoDaCamera,"-", verticeAdjacente)
                            localizacaoDeJack.add( ( posicaoDaCamera, verticeAdjacente ) )
                            return localizacaoDeJack
                else:
                    for contadorDeCaminho in range(4):
                        colunaposicaoDaCamera = colunaposicaoDaCamera + 1
                        
                        if self.cenarioMatriz[ linhaposicaoDaCamera ][ colunaposicaoDaCamera ] == self.JACK:
                            print("2 Detectou jack na aresta!", posicaoDaCamera,"-", verticeAdjacente)
                            localizacaoDeJack.add( ( posicaoDaCamera, verticeAdjacente ) )
                            return localizacaoDeJack
            else:
               
                if linhaposicaoDaCamera > linhaverticeAdjacente:
                    for contadorDeCaminho in range(4):
                        linhaverticeAdjacente = linhaverticeAdjacente + 1
                        
                        if self.cenarioMatriz[ linhaverticeAdjacente ][ colunaverticeAdjacente] == self.JACK:
                            print("3 Detectou jack na aresta!", posicaoDaCamera,"-", verticeAdjacente)
                            localizacaoDeJack.add( ( posicaoDaCamera, verticeAdjacente ) )
                            return localizacaoDeJack
                else:
                    for contadorDeCaminho in range(4):
                        linhaposicaoDaCamera = linhaposicaoDaCamera + 1
                        
                        if self.cenarioMatriz[ linhaposicaoDaCamera ][ colunaposicaoDaCamera ] == self.JACK:
                            print("4 Detectou jack na aresta!", posicaoDaCamera,"-", verticeAdjacente)
                            localizacaoDeJack.add( ( posicaoDaCamera, verticeAdjacente ) )
                            return localizacaoDeJack