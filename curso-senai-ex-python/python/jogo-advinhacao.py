import os 
import random

#função que sorteia um número secreto 
def sortear_numero_secreto():
    numero_secreto = random.randint(1,50)
    return numero_secreto

#função que solicita um palpite 
def solicitar_palpite ():
    palpite = int(input("digite seu palpite: "))
    return palpite 

#função que verifica o palpite do jogador 
def verificar_palpite (palpite, numero_secreto):
    #verificar se o palpite é menor que número que o numero_secreto
    if palpite < numero_secreto:
        return "menor"
    #verificar se o palpite é maior que no numero_secreto
    elif palpite > numero_secreto:
        return "maior"
    #verificar se o palpite é igual ao numero_secreto 
    else:
        return "igual"

#função principal
def main ():
    #gera o número secreto 
    numero_secreto = sortear_numero_secreto()
    print (f"número secreto: {numero_secreto}")
    #limpa a tela
    os.system("cls")

    #controla o número de tentativas 
    tentativas = 0

    print ("bem-vindo ao jogo da advinhação!")
    print ("tente advinhar o número entre 1 e 50 \n ")
    input ("digite <enter> para continuar ")

    while tentativas<=5:
    
        #acresentar o números de tentativas 
        tentativas += 1
        
        #solicitando palpite 
        palpite = solicitar_palpite()

        #verificar o palpite do jogador 
        resultado = verificar_palpite(palpite,numero_secreto)
        
        if resultado == "menor":
            print ("seu palpite foi menor que o número secreto,tente novamente ")
            input ("digite <enter> para continuar ")
        elif resultado == "maior":
            print ("seu palpite foi maior que o número secreto, tente novamente  ")
            input ("digite <enter> para continuar ")
        else:
            print (f"parabens! você acertou as {tentativas} tentativas! ")
            input ("digite <enter> para continuar ")
            break
    else:
        print ("fim de jogo!")

#chamar a função main 
main()



