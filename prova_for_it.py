pergunta_inicial = input("voce deseja saber a soma dos numero pares de determinado intervalo? (s/n) ")
if pergunta_inicial == "s":
    try:
        numero_inicial = int(input("digite o numero inicial: "))
        numero_final = int(input("digite o numero final: "))
        soma = 0
        for numero in range(numero_inicial, numero_final + 1):
            if numero % 2 == 0:
                soma += numero
        print(f"A soma dos números pares no intervalo é: {soma}")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros para o intervalo.")

elif pergunta_inicial == "n":
    print("tudo bem, até a proxima.")

else:
  print("digite uma resposta valida.")
