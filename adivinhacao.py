import random

def jogar():

    print("************************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("************************************")

    numero_secreto = round(random.randrange(1,101))

    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa in range(1, total_de_tentativas +1):
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute=int(chute_str)

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto


        if (acertou):
            print("Parabens! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Voce erro! Seu chute esta acima do número correto")
                if (tentativa == total_de_tentativas):
                    print("O numero secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif (menor):
                print("Voce erro! Seu chute esta abaixo do número correto")
                if (tentativa == total_de_tentativas):
                    print("O numero secreto era {}. Você fez {} pontos".format(numero_secreto,pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim de Jogo!")

if(__name__== "__main__"):
    jogar()