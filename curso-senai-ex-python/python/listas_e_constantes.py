import os 

os.system ("cls ")


#definindo constantes no python 
# TAXA_CAMBIO = 5.50

# quantia_dolar = float (input ("digite o valor em dólares: "))

# TAXA_CAMBIO = float (input ("digite a taxa de cambio:  "))

# valor_em_real = quantia_dolar * TAXA_CAMBIO

# print (f"o valor convertido em reais é R$: {valor_em_real}")

#exemplos de criação de lista 
numeros = [1,2,3,4,50]
nomes = ["joaquim","maria", "ana"]

print ("lista inicial")
print (nomes)

print ("=============================")

#alterando um elemento na lista
nomes [0] = "carlos"
print (f"nome da posição 0 : {nomes[0]}")

#adcionanar um novo elemento no final da lista 
nomes.append ("roberval")
nomes.append ("ricardo")


#adcionando um elemento em uma posição especifica da lista 
nomes.insert(1, "fernanda")

print ("lista atualizada! ")
print(nomes)

#removendo o elemento da posição 3 [ana ]
del nomes [3]

print ("lista atualizada após a remoção da ana ")
print (nomes)

#removendo e retornando o elemento no indice 2 
nome_removido = nomes.pop(2)
print (f"o nome removido foi: {nome_removido}  ")

print ("lista atualizada após o POP")
print (nomes)

#apagar todos os elementos da lista 
nomes.clear ()
print ("lista atualizada após o CLEAR")
print (nomes)
