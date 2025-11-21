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




valor_total = float (input ("digite o valor "))
porcentagem = float (input ("digite sua porcentagem "))
valor_parte = valor_total *(porcentagem/100)
print ("o valor parte será : ", valor_parte )
