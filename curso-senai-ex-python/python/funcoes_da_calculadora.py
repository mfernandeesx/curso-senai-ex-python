def somar (numero01,numero02):
    resultado = numero01 + numero02
    print (f"a soma é: {resultado}")

def subtrair(numero01,numero02):
    resultado = numero01 -numero02
    print (f"a subtração e: {resultado}")

def dividir (numero01, numero02):
    resultado = numero01 / numero02
    print (f"a divisão é : {resultado}")

def multiplicar (numero01, numero02):
    resultado = numero01 * numero02
    print (f"a divisão é: {resultado}")

def imprimir_msg_erro():
    print ("opção invalida ")

def calcular_resto_divisao(numero01, numero02):
    resultado = numero01 % numero02
    print (f"o resto da divisão é: {resultado}")

def somar_com_retorno(numero01,numero02):
    resultado = numero01+numero02
    return resultado

def subtrair_com_retorno(numero01, numero02):
    resultado = numero01 - numero02
    return resultado