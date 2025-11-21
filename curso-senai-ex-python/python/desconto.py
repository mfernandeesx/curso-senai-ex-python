
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


preco_original = float(input("digite o preço original do produto: "))
porcentagem_desconto = float(input("digite a porcentagem: "))
valor_desconto = preco_original *(porcentagem_desconto/100)
preco_final = preco_original - valor_desconto 
print("valor do desconto: ", valor_desconto )
print ("\n preço final do produto: ", preco_final )