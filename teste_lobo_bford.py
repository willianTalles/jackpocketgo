﻿from grafo import Grafo
from bellman_ford import BellManFord
#from utils import caminho_minino
import sys

class peso_negativo(Exception):
    pass

def test():

	#disponivel http://www.fernandolobo.info/aed-II/teoricas/a24e25.print.pdf
	print ('Testando Grafo de exemplo das aulas do prof. Fernando Lobo da universidade Algarve in Portugal.')

	g = Grafo(direcionado=True)
	'''
	g.inserir_vertice('a')
	g.inserir_vertice('b')
	g.inserir_vertice('c')
	g.inserir_vertice('d')
	g.inserir_vertice('e')

	g.inserir_aresta('a','b',10)
	g.inserir_aresta('a','c',3)
	g.inserir_aresta('b','c',1)
	g.inserir_aresta('b','d',2)
	g.inserir_aresta('c','b',4)
	g.inserir_aresta('c','d',8)
	g.inserir_aresta('c','e',2)
	g.inserir_aresta('d','e',7)
	g.inserir_aresta('e','d',9)
	'''
	g.ler_arquivo("cenario.txt")
	bmf = BellManFord();

	if bmf.executaBellManFord(g,'AI'):
		for v in g.get_vertices():
			caminho = [v.get_rotulo()]	
			bmf.caminhoMinimo(v, caminho)
			tamanhoCaminho = len(caminho)
			if( caminho[tamanhoCaminho-1] == 'AI' and caminho[0] == "CM"):
				print ('O menor caminho é: %s com custo %s.' %(caminho[::-1], v.get_distancia())	)
	else:
		print ('Ciclo negativo encontrado')

if __name__ == "__main__":
	test()