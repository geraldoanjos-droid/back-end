import random
alunos = [input(f"Nome do {i+1}º aluno: ").strip() for i in range(4)]
print(f"\n Aluno sorteado: {random.choice(alunos)} ")
