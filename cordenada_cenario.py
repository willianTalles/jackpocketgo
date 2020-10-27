#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

class CordenadaCenario:
    '''
    Formato (linha, coluna)
    '''

    def __init__( self, linha, coluna ):
        super().__init__()
        self._linha = linha
        self._coluna = coluna

    def getLinha( self ):
        return self._linha

    def setLinha( self, linha ):
        self._linha = linha

    def getColuna( self ):
        return self._coluna

    def setColuna( self, coluna ):
        self._coluna = coluna

    def ehParedeVertical( self, dimensaoCenario ):
        if( self._coluna == 0 or self._coluna == dimensaoCenario-1 ):
            
            return True
        
        return False

    def ehParedeHorizontal( self, dimensaoCenario ):
        if( self._linha == 0 or self._linha == dimensaoCenario-1
            and self._coluna != 0 and self._coluna != dimensaoCenario-1 ):
            
            return True
        
        return False