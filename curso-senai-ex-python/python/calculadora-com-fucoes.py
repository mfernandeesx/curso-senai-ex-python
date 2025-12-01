
#limpar a  tela 
import os 
os.system("cls")

#importar as funções 
import funcoes_da_calculadora as funcoes 

resposta = "sim "

while resposta == "sim ":

    os.system("cls")
    print ("calculadora com funções ")

    numero01 = float(input ("digite o primeiro número: "))
    numero02 = float(input ("digite o segundo número: "))

    #mostrando as opções 
    print ("==============================")
    print ('selecione uma opção abaixo ')
    print ("[1] - soma ")
    print ("[2] - subtração ")
    print ('[3] - divisão ')
    print ("[4] - multiplicação")
    print ("[5] - resto da divisão")

    opcao = input ("escolha uma  opção: ")

    #verificar a opção escolhida 
    if opcao == "1":
        print(f"a soma: {funcoes.somar_com_retorno(numero01,numero02)}")

    elif opcao == "2":
        print(f"a subtração é : {funcoes.subtrair_com_retorno(numero01, numero02)}")

    elif opcao == "3":
        funcoes.dividir(numero01, numero02)

    elif opcao == "4":
        funcoes.multiplicar(numero01, numero02)

    elif opcao == "5":
        funcoes.calcular_resto_divisao(numero01, numero02)

    else:
        funcoes.imprimir_msg_erro()

    resposta = input ("deseja executar novamanete? (SIM ou NÃO ").lower()

print ("progrma encerrado com sucesso!")



