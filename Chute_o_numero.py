# Projeto 3 - Chute o numero
# Objetivo do projeto: criar um algoritimo que gera um valor aleatorio e eu tenho q ficar tentando acertar o numero que ira aparecer.
import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.Tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.Tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print("chute um numero mais baixo!")
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print("Chute um numero maior!")
                self.PedirValorAleatorio()
            self.Tentar_novamente = False
            print('Parabens voce acertou!!')    

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()