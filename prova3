numero_secreto = 7
tentativas_restantes = 3 

while tentativas_restantes > 0:
    tentativa = int(input(f"Tente adivinhar o numero (você tem {tentativas_restantes} tentativas): "))

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou! O número era {numero_secreto}")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Você errou! Tente novamente. Você ainda pode tentar mais {tentativas_restantes} vezes.")
       
else:
    print(f"Infelizmente, suas tentativas terminaram! O número secreto era {numero_secreto}.")
    print("Mais sorte na próxima.")
