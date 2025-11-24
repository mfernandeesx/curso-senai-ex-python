# 1 - importando a biblioteca os 
import os 
# 2-  limpando a tela 
os.system ("cls")

print(""" 


██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝


""")

nome = input ("digite seu nome ")

nota1 = float(input("digite sua nota "))
nota2 = float (input ("digite sua nota "))
nota3 = float(input ("digite sua nota "))

media = (nota1 + nota2 + nota3 )/3

print ("nome do aluno:", nome )
print (f"sua media foi ",round(media,2))
if media>=7:
    print ("aprovado " )
elif media>=4:
    print("recuperação " )
else:
    print("reprovado ")

input ("pressione qualquer <Enter> para fechar o programa.")