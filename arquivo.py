import random

print("********************************")
print("Bem vindo ao jogo de Adivinhaçâo")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print(numero_secreto)
print("Qual o nível de dificuldade ?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int (input("Defina o nível: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else :
    total_de_tentativas = 5



for rodada in range (1, total_de_tentativas + 1) :
    print("Tentativas {} de {}" .format(rodada, total_de_tentativas))
    print("Ola Sr.{1} {0}".format("Araujo", "Eduardo"))
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute=int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou ! O seu chute foi maior do que o nùmero secreto")
        elif(menor):
            print("Você errou ! O seu chute foi menor do que o nùmero secreto")

            pontos_perdidos = abs(total_de_tentativas - chute)
            pontos = pontos - pontos_perdidos



    print("Fim de jogo")
