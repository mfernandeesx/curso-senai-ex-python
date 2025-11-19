#utilizado para executar comando no cmd 
import os 

#limapndo a tela 
os.system("cls")

nome_carro = input ("digite o nome do carro: ")
valor_carro = float (input ("digite o valor do carro: "))
consumo_por_litro = float (input ("digite o consumo pot litro: "))
print("-----------------------------")
print ("| carro: ", nome_carro )
print("|valor: ", valor_carro)
print ("|consumo por litro: ",consumo_por_litro )
print("------------------------------")