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
    try: 
        limpar_tela()
        print ('=== CADRASTRO DE NOVO CLIENTE ===\n ')

        nome = input("digite o nome do cliente: ")
        idade = int (input ('digite a idade do cliente: '))
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
    except:
        print ("a idade deve ser um número ")
    finally:
        voltar_ao_menu_principal()

#função que lista todos os clientes cadrastrados 
def listar_cliente_cadrastrar():
    limpar_tela()
    print ("=== LISTA DE CLIENTE CADASTRADO ===\n")

    for cliente in lista_de_clientes:
        print(f"nome: {cliente['nome']} | idade: {cliente['idade']} | e-mail: {cliente['email']} | celular: {cliente['celular']}")

    #voltar para a lista 
    voltar_ao_menu_principal()

#função que exclui um cliente cadastrado 
def excluir_cliente():
    #chamando a função que limpa a tela 
    limpar_tela()
    print ("=== REMOVER CLIENTE ===\n")


    #indice= 0

    #listando os clientes cadastrados 
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"indice {indice} | nome: {cliente['nome']} | idade: {cliente['idade']} | e-mail: {cliente['email']} | celular: {cliente['celular']}")
    
    try:
        #solicitar ao usuario o indice para remover
        indice = int (input ("\n digite o indice do cliente que deseja remover: "))

        if indice >=0 and indice <len (lista_de_clientes):
            #excluir o cliente 
            cliente_removido = lista_de_clientes.pop(indice)

            print (f"\n cliente {cliente_removido ['nome']} removido com sucesso ")
        else:
            print ("indice invalido ")
    except: 
        print ("'digite um indice valido ")

    finally: 
    #voltar ao menu principal 
    voltar_ao_menu_principal()

#função para editar um funcionario 
def editar_dados_clientes():
    limpar_tela()
    print ("==== EDITAR DADOS DO CLIENTE ====\n")

    for indice, cliente in enumerate(lista_de_clientes):
        print(f"indice {indice} | nome: {cliente['nome']} | idade: {cliente['idade']} | e-mail: {cliente['email']} | celular: {cliente['celular']}")
    try:
        indice = int (input ("\n digite o indice do cliente que deseja editar: "))

        if indice >= 0 and indice < len (lista_de_clientes):

            #capturar os dados do cliente selecionado 
            dados_do_clientes = lista_de_clientes[indice]

            #exibindo os dados do cliente selecionado
            print (f"\n EDITANDO OS DADOS DO CLIENTE {dados_do_clientes["nome"]}")

            #solicitando os novos dados 
            novo_nome = input (f"digite o novo nome: (atual -{dados_do_clientes["nome"]})")
            nova_idade = input (f"digite a nova idade: (atual -{dados_do_clientes["idade"]})") 
            novo_email = input (f"digite o novo email:(atual -{dados_do_clientes["email"]})")
            novo_celular = input (f"digite o novo celular(atual -{dados_do_clientes["celular"]}) ")
            # editar 
            dados_do_clientes["nome"] = novo_nome
            dados_do_clientes["idade"] = nova_idade
            dados_do_clientes["email"] = novo_email
            dados_do_clientes["celular"] = novo_celular
            print ("\n dados atualizados com sucesso !")
    except: 
        print ("idade ou indice, devem ser validos ")
    finally: 
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

    elif opcao == 3:
        editar_dados_clientes()

    elif opcao == 4:
        #abrir a exclusão de um cliente 
        excluir_cliente()

    elif opcao== 5:
        input("pressione <ENTER> para encerrar o programa......")
        exit()

    else:
        print ("opção invalida! tente novamente ")
        voltar_ao_menu_principal()

main()
