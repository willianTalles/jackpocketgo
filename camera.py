#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cenario.py#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#camera.py

class Camera:
    def __init__( self, posicao, vertices ):
        super().__init__()
        self.posicao = posicao
        self.DISTANCIADOCAMPODEVISAO = 4
        self.CAMPODEVISAO = self._gerarCampoDeVisao(self.posicao, vertices)

    
    def _gerarCampoDeVisao(self, posicao, vertices):
        campoDeVisao = set()
        
        for vertice in vertices:
            if vertice.get_rotulo() == posicao:
                verticeAdjacenteAPosicao = vertice.get_adjacentes()
                for verticeAdjacente in verticeAdjacenteAPosicao:
                    if int(verticeAdjacente.get_peso(vertice)) <= self.DISTANCIADOCAMPODEVISAO:
                        campoDeVisao.add( ( vertice, verticeAdjacente ) )
        
        return campoDeVisao
