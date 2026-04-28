import random

alunos = [input(f"Nome do {i+1}º aluno: ") for i in range(4)]
random.shuffle(alunos)

print("\nOrdem sorteada:")
for i, nome in enumerate(alunos, 1):
    print(f"{i}º - {nome}")
