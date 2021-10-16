from typing import List
import random




def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    enforcado = False
    acertou = False
    erros: int = 0

    while not enforcado and not acertou:  # enquanto (True), executar continuamente

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,palavra_secreta,letras_acertadas)

        else:
            erros += 1
            print("Ops, digito não encontrado, você ainda possui {} vidas restantes".format(6 - erros))
            desenha_forca(erros)

        enforcado = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta,letras_acertadas)

    print("Fim de Jogo!")


def imprime_mensagem_abertura():
    print("************************************")
    print("****Bem vindo ao jogo de Forca*****!")
    print("************************************")

def carrega_palavra_secreta(nome_arquivo="Palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras: list[str] = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return  palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual a letra?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()):
            letras_acertadas[index] = letra  # print("Encontrei a letra {} na posição {}".format(letra,index))
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta,letras_acertadas):
    print(letras_acertadas)
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()
