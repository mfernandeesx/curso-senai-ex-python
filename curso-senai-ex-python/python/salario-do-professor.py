import os 
os.system("cls")


print ("qual é o seu nivel:\n 1- nivel 1 \n 2- nivel 2 \n 3- nivel 3")
nivel = input ("qual é o seu nivel: ")

qtd_aulas =int(input ("qual é sua qtd de aulas por semana: "))

if nivel == "1":
    salario = (qtd_aulas *12) *4
elif nivel == "2":
    salario =(qtd_aulas *17)*4
elif nivel == "3":
    salario = (qtd_aulas *25)*4
else:
    print ("o nivel digitado é invalido ")
    
print (f"o seu salario será: {salario}")


input ("pressione <enter> para finalizar... ")
