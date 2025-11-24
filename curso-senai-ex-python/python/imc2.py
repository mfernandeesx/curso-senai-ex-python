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

nome = input ("digite seu nome: ")
peso = float(input ("digite seu peso "))
altura = float(input ("digite sua altura "))
imc = peso / (altura*altura)
print ("o seu imc é ", imc )

if imc >=18.5:
    print("você está abaixo do peso")
elif imc >=24.9:
    print("você está com  o peso normal ")
elif imc <=29.9:
    print("você esta com sobrepeso")
elif imc <=34.9:
    print("você esta com obesidade grau I")
elif imc <=39.9:
    print ("você esta com obesidade grau II")
elif imc <=40:
    print("você esta com obesidade grau III")
