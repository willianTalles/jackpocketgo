#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cenario.py

from cordenada_cenario import CordenadaCenario as Cordenada

class Cenario:
    
    def __init__( self, dimensao ):
        super().__init__()
        self.dimensao = dimensao
        self.cenarioMatriz = []
        self.PAREDEVERTICAL = '|'
        self.PAREDEHORIZONTAL = '='
        self.OBSTACULO = '#'
        self.CAMINHO = '.'
        

    def desenha( self, grafo = None ):
        self._geraCenarioVazio()

        for i in range( 0, self.dimensao ):
            for j in range( 0, self.dimensao ):
                cordenada = Cordenada( i, j )
                  
                if( cordenada.ehParedeVertical( self.dimensao ) ):
                    self.cenarioMatriz[i][j] = self.PAREDEVERTICAL

                elif( cordenada.ehParedeHorizontal( self.dimensao ) ):
                    self.cenarioMatriz[i][j] = self.PAREDEHORIZONTAL
                
                # CONFIGURAR CONDIÇÃO PARA DESENHAR CORDENADAS DO GRAFO
                elif():
                    pass
                # CONFIGURAR CONDIÇÃO PARA DESENHAR GRAFO COMPLEMENTAR
                else:
                    pass
    
    def _geraCenarioVazio( self ):
        
        for i in range( self.dimensao ):
            linha = [] # lista vazia
            for j in range( self.dimensao ):
	            linha.append( self.CAMINHO )
	
	        # coloque linha na matriz
            self.cenarioMatriz.append( linha )

    def ehParedeVertical( self, cordenada ):
        if( self.cordenada["x"] != 0 and self.cordenada["x"] != self.dimensaoCenario
            and self.cordenada["y"] == 0 or self.cordenada["y"] == self.dimensaoCenario ):
            return True

    def imprimeCenario( self ):
        for i in range( self.dimensao ):
            for j in range( self.dimensao ):
                print( self.cenarioMatriz[i][j], end="" )
            print("\n")