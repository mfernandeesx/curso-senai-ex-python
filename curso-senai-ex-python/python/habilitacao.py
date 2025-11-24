#1 passo - importar a biblioteca os 
import os 

#2 passo - utilizar a os para limpar tela 
os.system("cls ")

print(""" 

██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚═════╝░
""")

#texto = string = str 
#3 passo - realizar as entradas 
nome = input ("digite seu nome: ")
idade = int(input ("digite sua idade: "))



# 4 - verificar a idade do usuário 
if idade >=18:
    possui_carteira = input ("possui carteira de motorista? \n (1-sim | 2 -não): ")
    if possui_carteira== "1":
        print ("pode dirigir! ")
    else:
        print ("não pode dirigir! ")
else:
    print ("menor de idade")


