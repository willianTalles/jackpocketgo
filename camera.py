#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#camera.py#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#camera.py

class Camera:
    def __init__( self, posicao, vertices ):
        super().__init__()
        self.posicao = posicao
        self.DISTANCIADOCAMPODEVISAO = 4
        self.CAMPODEVISAO = self._gerarCampoDeVisao(self.posicao, vertices)

    def getPosicao( self ):
        return self.posicao
    
    def getCampoDeVisao( self ):
        return self.CAMPODEVISAO
    
    def _gerarCampoDeVisao(self, posicao, vertices):
        campoDeVisao = None
        
        for vertice in vertices:
            if vertice == posicao:
                campoDeVisao = vertice.get_adjacentes()

        return campoDeVisao
