import os 

#lista que armazena todos os clientes 
lista_de_clientes = [
    {
        "nome": "Ana Souza",
        "idade": 28,
        "email": "ana.souza@example.com",
        "celular": "(11) 91234-5678"
    },
    {
        "nome": "Bruno Lima",
        "idade": 35,
        "email": "bruno.lima@example.com",
        "celular": "(21) 99876-5432"
    },
    {
        "nome": "Carla Mendes",
        "idade": 42,
        "email": "carla.mendes@example.com",
        "celular": "(31) 98765-4321"
    },
    {
        "nome": "Diego Rocha",
        "idade": 30,
        "email": "diego.rocha@example.com",
        "celular": "(41) 97654-3210"
    },
    {
        "nome": "Eduarda Alves",
        "idade": 25,
        "email": "eduarda.alves@example.com",
        "celular": "(51) 96543-2109"
    }
]


#função que limpa a tela 
def limpar_tela():
    os.system("cls")

#função que exibe o menu na tela 
def exibir_menu():
    print ("\n=== MENU PRINCIPAL=====")
    print ("[1] - cadrastro de clientes")
    print ("[2] - listar clientes cadastrados ")
    print ("[3] - editar dados de clientes ")
    print ("[4] - excluir um cliente ")
    print ("[5] - sair do sistema \n ")

#função que volta ao menu principal
def voltar_ao_menu_principal():
    input ("\n pressione <enter> para voltar ao menu inicial...")
    main()

#função que cadrastra movo cliente 
def cadastrar_novo_cliente():
    limpar_tela()
    print ('=== cadrastro de novo cliente ===\n ')

    nome = input("digite o nome do cliente: ")
    idade = input ('digite a idade do cliente: ')
    email = input ("digite o e-mail do cliente: ")
    celular = input ("digite o celular do cliente: ")

    dados_clientes = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'celular': celular 
    }

    # ADICIONAR O DICIONÁRIO E NÃO O NOME
    lista_de_clientes.append(dados_clientes)

    print (f"\n o cliente {nome} foi cadrastrado com sucesso ")
    voltar_ao_menu_principal()

#função que lista todos os clientes cadrastrados 
def listar_cliente_cadrastrar():
    limpar_tela()
    print ("=== lista de clientes cadastrado ===\n")

    for cliente in lista_de_clientes:
        print(f"nome: {cliente['nome']} | idade: {cliente['idade']} | e-mail: {cliente['email']} | celular: {cliente['celular']}")

    #voltar para a lista 
    voltar_ao_menu_principal()

#função que exclui um cliente cadastrado 
def excluir_cliente():
    #chamando a função que limpa a tela 
    limpar_tela()
    print ("=== remover cliente ===\n")


    #indice= 0

    #listando os clientes cadastrados 
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"indice {indice} | nome: {cliente['nome']} | idade: {cliente['idade']} | e-mail: {cliente['email']} | celular: {cliente['celular']}")
    
    #solicitar ao usuario o indice para remover
    indice = int (input ("\n digite o indice do cliente que deseja remover: "))

    #excluir o cliente 
    cliente_removido = lista_de_clientes.pop(indice)

    print (f"\n cliente {cliente_removido ['nome']} removido com sucesso ")

    #voltar ao menu principal 
    voltar_ao_menu_principal()

#função principal do meu programa 
def main():
    limpar_tela()
    print ("bem-vindo ao gerenciador de clientes ")

    exibir_menu()
    
    opcao = int(input ("escolha uma opção: "))
    
    if opcao == 1:
        cadastrar_novo_cliente()
    
    elif opcao == 2:
        listar_cliente_cadrastrar()
    elif opcao == 4:
        #abrir a exclusão de um cliente 
        excluir_cliente()
    else:
        print ("opção invalida! tente novamente ")
        voltar_ao_menu_principal()

main()
