from cenario import Cenario

class peso_negativo(Exception):
    pass

def test():

    cenario = Cenario( 16 )

    cenario.desenha()
    #cenario._geraCenarioVazio()

    cenario.imprimeCenario()

if __name__ == "__main__":
	test()