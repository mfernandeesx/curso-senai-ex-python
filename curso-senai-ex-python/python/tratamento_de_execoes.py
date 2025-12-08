import os 

os.system ("cls ")

print ("exemplos de tratamento de exceções")


try: 
    numero1 = int (input ("digite o primeiro número: "))
    numero2 = int (input ("digite o segundo número: "))

    resultado = numero1 / numero2
    print (f" o resultado da divisão é {resultado}")
except ValueError as erro:
    print (f"aconteceu o erro {erro}")
    print ("você digitou um valor invalido")




