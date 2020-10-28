#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#dijkstra.py

from grafo import Grafo
from vertice import Vertice

class Dijkstra:
	
	'''
	Classe que encontra o menor caminho em um grafo a partir de
	uma origem e um destino utilizando o algoritmo de Dijkstra.
	'''

	def executaDijkstra(self, grafo, origem):
		self._inicializarGrafo(grafo, origem)

		S = []
		Q = [v for v in grafo.get_vertices()]

		while len(Q):
			u = self._extrairMin(Q)
			u.set_visitado()
			S.append(u)

			for v in u.get_adjacentes():
				if v.get_visitado():
					continue
				self._executaRelaxamento(u, v)


	def caminhoMinimoDijkstra(self, grafo, vOrigem, vDestino):
		caminhoEncontrado = []
		for v in grafo.get_vertices():
			caminho = [v.get_rotulo()]
			self.caminhoMinimo(v, caminho)

			comprimentoCaminho = len(caminho)

			if(caminho[comprimentoCaminho-1] == vOrigem and caminho[0] == vDestino):
				caminhoEncontrado.append(caminho)
		
		return caminhoEncontrado


	def _inicializarGrafo(self, grafo, origem):
		for v in grafo.get_vertices():
			v.set_distancia(float('Infinity'))

		grafo.get_vertice(origem).set_distancia(0)


	def _executaRelaxamento(self, u, v):
		if v.get_distancia() > u.get_distancia() + u.get_peso(v):
			v.set_distancia(u.get_distancia() + u.get_peso(v))
			v.set_predecessor(u)


	def _extrairMin(self, Q):
		min = Q[0]
		for v in Q:
			if v.get_distancia() < min.get_distancia():
				min = v
		Q.remove(min)
		return min