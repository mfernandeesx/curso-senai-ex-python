#utilizado para executar comando no cmd 
import os 

#limapndo a tela 
os.system("cls")



print(""" 

██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚═════╝░
""")

resposta = "sim"

while resposta == "sim":

    nome = input ("digite seu nome: ")
    peso = float(input ("digite seu peso "))
    altura = float(input ("digite sua altura "))
    imc = peso / (altura*altura)
    print ("o seu imc é ", round (imc,2) )

    if imc >=18.5:
        situacao ="abaixo do peso"
        print("você está abaixo do peso")
    elif imc >=24.9:
        situacao = "peso normal"
        print(" você está com  o peso normal ")
    elif imc <=29.9:
        situacao =  "sobrepeso"
        print(" você esta com sobrepeso")
    elif imc <=34.9:
        situacao = "obesidade grau I"
        print("você esta com obesidade grau I")
    elif imc <=39.9:
        situacao = "obesidade grau II"
        print ("você esta com obesidade grau II")
    elif imc <=40:
        situacao = "obesidade grau III"
        print("situação: você esta com obesidade grau III")

    with open("imc_dos_paciente.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"nome: {nome}\n")
        arquivo.write(f"peso: {peso}\n")
        arquivo.write(f"altura: {altura}\n")
        arquivo.write(f"imc: {round(imc,2)}\n")
        arquivo.write(f"situação: {situacao}\n")
        arquivo.write("=======================================\n")

        print ("dados salvos com sucesso !")

    resposta = input("Gostaria de executar novamente? (sim/não): ").lower()
    os.system ("cls ")

input("\nPressione <Enter> para fechar o programa...")
