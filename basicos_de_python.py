nome = input("Digite seu nome: ")

print(f"Seu nome é {nome}")

try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos")
except ValueError:
    print("Digite um número")