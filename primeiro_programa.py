import random

#variaveis do jogo
tentativas = 0
limite_tentativas = 9
tentativas_restantes = 10

while True: 
    dificuldade = int((input("escolha a dificuldade: 1-facil 2-medio e 3-dificil ")))

# Verifica se a dificuldade é válida
    if int(dificuldade) in [1, 2, 3]:
        dificuldade = int(dificuldade)
        break
    else:
        print("Escolha um número válido!")

#funcionamento da dificuldade
if dificuldade == 1:
    print(f"voce esta na dificuldade {dificuldade}, acerte entre 1 e 100 em 10 chances")
    numero_secreto = random.randint(1, 100)
elif dificuldade == 2:
    print(f"voce esta na dificuldade {dificuldade}, acerte entre 1 e 200 em 10 chances") 
    numero_secreto = random.randint(1, 200)
elif dificuldade == 3:
    print(f"voce esta na dificuldade {dificuldade}, acerte entre 1 e 300 em 10 chances")
    numero_secreto = random.randint(1, 300)

    


while True: 
    #funcionamento do acerto do numero
    palpite = int(input("digite seu palpite "))
    tentativas += 1
    tentativas_restantes -= 1
    
    if palpite == numero_secreto:
        print(f"parabens voce acertou com {tentativas} tentativas, o numero é {numero_secreto}")
        break
    elif palpite < numero_secreto and tentativas_restantes > 0:
        print(f"quase lá, é maior e voce ainda tem {tentativas_restantes} tentativas restantes")
    elif palpite > numero_secreto and tentativas_restantes > 0:
        print(f"é menor, e voce ainda tem {tentativas_restantes} tentativas restantes")
        
    if tentativas > limite_tentativas:
        print(f"voce atingiu o maximo de tentativas e perdeu, o numero era {numero_secreto}")
        break