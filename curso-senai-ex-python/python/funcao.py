
#limpando tela 
import os 
os.system ("cls")


#exemplo de função sem parametros 
def escreva():
    print("bem-vindo ao sistema ")

#exemplo de função com parametros
def exibir_idade (suaidade,nome):
    print (f"{nome} tem {suaidade} anos!")

def soma(n1,n2):
    resultado = n1+n2
    print (f"soma dos resultados e: {resultado}")

#exemplo de função com retorno 
def subtrair (valor1, valor2):
    resultado = valor1 - valor2 
    return resultado 


print ("executou o programa ")


#chamando uma função sem parametros 
escreva ()

#chmando uma função com parametros
exibir_idade(19, "Maria")
exibir_idade(38, "Caio")
soma(50,90)

#chamando uma função com retorno 
print (f"A subtração é: {subtrair(5,2)}")



