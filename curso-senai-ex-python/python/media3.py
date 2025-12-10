# 1 - importando a biblioteca os 
import os 

# 2 - limpando a tela 
os.system("cls")

print(""" 

██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝

""")

resposta = "sim"

while resposta == "sim":

    nome = input("Digite seu nome: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    print("\n--- RESULTADO ---")
    print("Nome do aluno:", nome)
    print("Média:", round(media, 2))

    if media >= 7:
        situacao = "Aprovado"
        print("Situação: Aprovado")
    elif media >= 4:
        situacao = "Recuperação"
        print("Situação: Recuperação")
    else:
        situacao = "Reprovado"
        print("Situação: Reprovado")

    # Gravando no arquivo
    with open("notas_dos_alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome do aluno: {nome}\n")
        arquivo.write(f"Nota 01: {nota1}\n")
        arquivo.write(f"Nota 02: {nota2}\n")
        arquivo.write(f"Nota 03: {nota3}\n")
        arquivo.write(f"Média: {round(media,2)}\n")
        arquivo.write(f"Situação: {situacao}\n")
        arquivo.write("=======================================\n\n")

    print("\nDados salvos com sucesso!\n")

    resposta = input("Gostaria de executar novamente? (sim/nao): ").lower()
    os.system ("cls ")

input("\nPressione <Enter> para fechar o programa...")
