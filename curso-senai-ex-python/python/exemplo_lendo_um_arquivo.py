import os 

os.system("cls")

print("=== LENDO DADOS DE UM ARQUIVO ===\n")

input('Pressione a tecla <enter> para continuar...')

os.system("cls")

# acessando o arquivo para ler os dados
with open("produto.txt", "r", encoding="utf-8") as arquivo:
    print("=== Dados do arquivo ===\n")
    
    # # exibindo os dados
    # print(arquivo.read())

    #lendo linha por linha  do arquivo 
    for linha in arquivo:
        print (f"conteúdo da linha: {linha.strip()}")

input("Pressione a tecla <enter> para encerrar....")
