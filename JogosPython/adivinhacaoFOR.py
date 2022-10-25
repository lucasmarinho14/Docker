from importlib import import_module
import random

def jogar():

    print("*********************************")
    print("Bem vido ao jogo de adivinhação!!")
    print("*********************************")
    numero_secreto = random.randrange(1 , 101)
    total_de_tentativas = 0
    rodada = 1
    ponto = 1000
    print(numero_secreto)

    print("Selecione o nivel de dificuldade")
    print("(1) Fácil, (2) Médio, (3) Dificíl")
    nivel = int(input("Defina o Nível: "))

    if (nivel == 1):
        total_de_tentativas = 20

    if (nivel == 2):
        total_de_tentativas = 10

    if (nivel == 3):
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format (rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100 "))
        print("Voce digitou", chute)

        if (chute < 1 or chute > 100):
            print ("Você deve digitar um numero entre 1 e 100!")
            continue
            


        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if (acertou):
            print("Você acertou!")  
            break
        else :
            print("Você errou!")
            if (maior):
                print("seu chute foi muito alto")
                
                
            elif (menor):
                print("Seu chute foi muito baixo")
            
            pontos_perdidos = abs(numero_secreto - chute)
            ponto = ponto - pontos_perdidos
                
                
    print("Sua pontuação foi: ",ponto)
    print("Fim de Jogo!") 
           
if (__name__ == "__main__"):
    jogar()   
        
