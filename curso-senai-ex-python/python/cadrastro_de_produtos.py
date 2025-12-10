import os 
os.system("cls")

print ("=== SALVANDO DADOS DO PROTUDOS EM UM ARQUIVO ===\n")

nome_produto = input ("digite o nome do produto: ")
fabricante = input ("digite o fabricante: ")
categoria = input ("digite a categoria: ")
preco = float (input ("digite o preço do produto: "))

#manipulando arquivos 
# arquivo = open ("produto.txt","a", encoding="utf-8")
with = open ("produto.txt","a", encoding="utf-8") as arquivos 

#gravando as informações dentro do arquivo 
arquivo.write(f"produto: {nome_produto} | fabricante: {fabricante} | categoria: {categoria} | preço: {preco:.2f} \n ")


# fechar o arquivo 
# arquivo.close ()
#não é necessario fechar o arquivo quando utilizamos o with 

input ("pressione a tecla <enter> para encerrar.....")

