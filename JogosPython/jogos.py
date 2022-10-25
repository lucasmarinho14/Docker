import forca
import adivinhacaoFOR

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu Jogo********")
    print("*********************************")

    print("Forca (1), Adivinhação (2)")

    jogo_escolhido = int(input("Qual jogo? "))

    if (jogo_escolhido == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo_escolhido == 2):
        print("Jogando Adivinhação")
        adivinhacaoFOR.jogar()


if (__name__ == "__main__"):
    escolher_jogo() 