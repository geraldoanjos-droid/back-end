numero = int(input("Digite um número inteiro: "))

print("\n1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL")
opcao = int(input("\nSua opção: "))

if opcao == 1:
    print(f"\n{numero} em binário: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"\n{numero} em octal: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"\n{numero} em hexadecimal: {hex(numero)[2:].upper()}")
else:
    print("\nOpção inválida!")
