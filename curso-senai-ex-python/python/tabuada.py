import os 
os.system ("cls")

numero = int(input ("digite um número: "))

#contador ou incremento
i=0
while (i<=10):
    print (f"{numero} X {i} = {numero * i}")
    i+= 1
print ("o programa terminou ")
input ("pressione a tecla <enter> para finalizar ")
