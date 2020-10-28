#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

from vertice import Vertice

class Grafo:

	def __init__(self, direcionado=False): 
		self.vertices = {}
		self.direcionado = direcionado

	def inserir_vertice(self, rotulo):
		v = Vertice(rotulo)
		self.vertices[rotulo] = v
		return v

	def inserir_aresta(self, vertice_inicial, vertice_final, peso = 0):
		if vertice_inicial not in self.vertices:
			self.inserir_vertice(vertice_inicial)
		if vertice_final not in self.vertices:
			self.inserir_vertice(vertice_final)
		self.vertices[vertice_inicial].inserir_adjacente(self.vertices[vertice_final], peso)
		if not self.direcionado:
			self.vertices[vertice_final].inserir_adjacente(self.vertices[vertice_inicial], peso)

	def get_vertices(self):
		return ([v for (k,v) in self.vertices.items()])

	def get_vertice(self, rotulo):
		if rotulo in self.vertices:
			return self.vertices[rotulo]
		else:
			return None

	def get_arestas(self):
		arestas = set()
		for rotulo, v in self.vertices.items():
			for a in v.adjacentes:
				arestas.add((v, a))
		return arestas
    
	def ler_arquivo(self, nome_arquivo):
		'''
		Monta grafo a partir de dados de um arquivo
		'''
		dados = open(nome_arquivo, "r")

        # primeira linha contem todos os rotulos dos vertices
		lista_vertices = dados.readline().replace("\n","").split(" ")
        
        # inserir todos os vertices lidos no grafo
		for v in lista_vertices:
			self.inserir_vertice(v)

        # a partir da proxima linha contem todas as arestas até o fim do documento
		linha = dados.readline()
		while linha:
			aresta = linha.replace("\n","").split(" ")
			self.inserir_aresta(aresta[0], aresta[1], float(aresta[2]))
			linha = dados.readline()

		dados.close()

	def __iter__(self):
		return iter(self.vertices.values())
