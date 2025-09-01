num_alunos = int(input("digite o numero de alunos: "))

alunos_dados = []

soma_geral_turma = 0


for aluno in range(1,num_alunos + 1):
    print(f"\n--- Coletando dados do Aluno {aluno} ---")
   
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    alunos_dados.append([nome,nota1,nota2,nota3])

    media_aluno =(nota1 + nota2 + nota3) / 3
    soma_geral_turma += media_aluno

if num_alunos > 0:
    print("\n================== RESUMO DA TURMA ==================")
    
    for aluno in alunos_dados:
        nome = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        nota3 = aluno[3]
        
        media_aluno = (nota1 + nota2 + nota3) / 3
        
        if media_aluno >= 7.0:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
            
        print(f"\nNome: {nome}")
        print(f"Notas: {nota1}, {nota2}, {nota3}")
        print(f"Média: {media_aluno:.2f}")
        print(f"Situação: {situacao}")

    
    media_geral_turma = soma_geral_turma / num_alunos
    print(f"\n--- MÉDIA GERAL ---")
    print(f"Média geral da turma: {media_geral_turma:.2f}")

else:
    print("\nNenhum aluno foi registrado.")

