import os

# função que exibe o menu 
def exibir_menu():
    print("\n === CONVERSOR DE MOEDAS ===")
    print("[1] Converter Dólar -> Real")
    print("[2] Converter Real -> Dólar")
    print("[0] Sair")

# funçao converter de dolar para real
def converter_dolar_para_real(quantia_dolar, taxa):
    return quantia_dolar * taxa

# função converter de real para dolar
def converter_real_para_dolar(quantia_real, taxa):
    return quantia_real / taxa

# função principal do programa 
def main():
    os.system("cls")  # limpa a tela (no Windows)

    # solicitando a taxa de câmbio do dia 
    taxa_cambio = float(input("Informe a taxa de câmbio do dia: "))

    resposta = "sim"
    while resposta == "sim":
        # chamando a função exibir_menu 
        exibir_menu()

        # solicitando a opção do usuário 
        opcao = input("Escolha uma opção: ")

        # verificando a opção escolhida
        if opcao == "1":
            quantia_dolar = float(input("Digite a quantia em DÓLAR: "))
            total_convertido = converter_dolar_para_real(quantia_dolar, taxa_cambio)
            print(f"DOLAR {quantia_dolar: } = REAL {total_convertido: }")

        elif opcao == "2":
            valor_real = float(input("Digite a quantia em REAL: "))
            total_convertido = converter_real_para_dolar(valor_real, taxa_cambio)
            print(f"REAL {valor_real: } = DOLAR {total_convertido: }")

        elif opcao == "0":
            print("Encerrando o programa...")
            break
             
        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")

        resposta = input("\nDeseja continuar? (sim/nao): ").lower()

# chamando a função main 
main()
