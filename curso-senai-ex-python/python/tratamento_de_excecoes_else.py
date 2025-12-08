import os 
os.system ("cls ")

try: 
    numero = int (input ("digite um número inteiro:  "))
    resultado = 10 / numero 

except ZeroDivisionError: 
    print ("erro: não é possivel dividir por zero ")

except ValueError:
    print ("erro: você não digitou um numero válido ")

else: 
    print (f"o resultado da divisão é : {resultado}")

finally: 
    print ("encerrando a operação ")