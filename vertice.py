#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#cordenada_cenario.py

class Vertice:

	def __init__(self, rotulo): 
		self.rotulo = rotulo 
		self.adjacentes = {}
		self.distancia = 0
		self.visitado  = False
		self.predecessor = None

	def get_rotulo(self):
		return self.rotulo

	def inserir_adjacente(self, vertice_final = None, peso = 0):
		self.adjacentes[vertice_final] = peso

	def get_adjacentes(self):
		return self.adjacentes.keys() 

	def get_distancia(self):
		return self.distancia

	def set_distancia(self, distancia):
		self.distancia = distancia

	def set_visitado(self):
		self.visitado = True

	def get_visitado(self):
		return self.visitado

	def get_peso(self, vertice_final):
		return self.adjacentes[vertice_final]

	def set_predecessor(self, predecessor):
		self.predecessor = predecessor

	def get_predecessor(self):
		return self.predecessor

	def __str__(self):
		return str(self.rotulo)