import random

class JogoAdvinhacao:
    def __init__(self):
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0

    def iniciar_jogo(self):
        print('Bem-vindo ao Jogo da Advinhação!')
        print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

        while True:
            try:
                palpite = int(input('Digite seu palpite: '))
                if palpite < 1 or palpite > 100:
                    raise ValueError("O palpite deve estar entre 1 e 100!")
                self.__tentativas += 1

                if palpite < self.__numero_secreto:
                    print("O número secreto é maior. Tente novamente!")
                elif palpite > self.__numero_secreto:
                    print("O número secreto é menor. Tente novamente!")
                else:
                    print(f'Parabéns! Você acertou! O número secreto é {self.__numero_secreto} em '
                          f'{self.__tentativas} tentativas.')
                    break
            except ValueError as ve:
                print(ve)

        self.jogar_novamente()

    def jogar_novamente(self):
        while True:
            jogar_novamente = input('Deseja jogar novamente? (sim/não): ')
            if jogar_novamente.lower() == 'sim':
                self.__numero_secreto = random.randint(1, 100)
                self.__tentativas = 0
                self.iniciar_jogo()
                break
            elif jogar_novamente == "não":
                print("Obrigado por jogar!")
                break
            else:
                print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

game = JogoAdvinhacao()
game.iniciar_jogo()
