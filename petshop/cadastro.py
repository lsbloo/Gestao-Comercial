### Cadastro ###
import time #importei o time para ajudar na barra de carregamento
import random # importei o random para gerar um numero aleatorio
from produtos import * # importei o modulo produtos
#print(opcao)
global cadastro # defini o modulo cadastro como sendo uma variavel global para nao da erro nas demais funcoes
#### Listas ####
cadastro = [] # lista de cadastro
cod_cachorro_lista = [] # lista dos codigos dos cachoros
verifica_aux = [] # lista que verifica o codigo inserido
carrinho_lista=[] # lista dos produtos comprados
#####################
global opcao # defini opcao como sendo global para ter acesso a todo o programa
verifica = 0 # variaveis definidas
cod_cachorro = 0 # variaveis definidas
opcao = int(input("Digite sua Opção: ")) # pergunta a opcao do usuario.
codigo = 49946325 # Minha senha de ADM , para ter acesso a funcoes do programa
while opcao != 5: # criei um loop que enquanto a opcao for diferente de 5
    if opcao >=6: # agora se a opao or maior ou igual a 6 ele imprime o erro
        print("Opcão invalida!")
        opcao = int(input("Digite sua Opcão: ")) # pergunta novamente a opcao desejada
    else:
        def cadastros(opcao): # Funcao principal do programa cria cadastros e os armazena
            global cod_cachorro # variavel global de codigo_ cachorro
            # parte de cadastro
            if opcao == 1: # se a opcao do usuario for igual a 1 entao ele cadastra
                print("-        Cadastro         -") #imprime
                nome_cliente = input("Digite seu nome: ") # pega o nome do cliente
                cpf_cliente = input("Digite seu CPF: ") # pega o cpf do cliente
                end = input("Digite seu endereço: ") # pega o endereço do cliente
                nome_cachorro = input("Digite o nome do cachorro: ") # nome cachorro
                cod_cachorro = random.randint(1,500) # gera um codigo aleatorio para os cachorros
                cadastro.append([nome_cliente,cpf_cliente,end,nome_cachorro,cod_cachorro]) #criei um vetor que salva tudo na lista cadastro
                cod_cachorro_lista.append(cod_cachorro) # logo em seguida armezados
                for i in range(40): # criei um loop para fazer a barra de carregamento
                    time.sleep(0.1) # usei o sleep() para da um delay
                    print("#",end= '')
                print() 
                print("Cadastrado!")
                print()
                print("O codigo de",nome_cachorro,"é",cod_cachorro)
                return cadastro,cod_cachorro # em seguida retorna a lista cadastro e o codigo do cachrro
            


        def listar(opcao,codigo): #FUNCAO LISTAR PARA LISTAR OS PRODUTOS
            global cont #variavel cont para gerar erro 2x
            cont = 0
            if opcao == 2: #se a opcao for 2 entao entra na parte do ADM
                teste_cod = int(input("SÓ ADM, CODIGO: ")) 
                if teste_cod == codigo: # se o codigo for igual ao codigo_pass entao tem acesso
                    print("Acesso autorizado!")
                    for i in cadastro: # loop proucura dentro de cadastro cada elemento informando o conteudo
                        print("Nome:",i[0],"CPF",i[1],"ENDEREÇO:",i[2],"Nome Cachorro:",i[3],"CODIGO CACHORRO:",i[4])
                else: # caso contrario coddigo_pass esta errado o cont imprime 2x um erro e tira da funcao
                    print("Codigo errado")
                    teste_cod = int(input("SÓ ADM, SENHA: "))
                    cont += 1 
                    if cont == 3: # preciso ajeitar o cont para resolver o problema do erro de password
                        return cont # retorna cont

        def search(opcao,cadastro): #funcao que procura os clientes cadastrados
            aux = ''
            #cont1 = True
            sair = True 
            
            if opcao == 3: # 3> entao pergunta nome e cpf
                nome_search = ''
                cpf_search = ''
                nome_search = input("Digite o nome: ")
                cpf_search = input("CPF: ")
                while sair:
                    for disc in cadastro:
                        if nome_search == disc[0] and cpf_search == disc[1]: # se for True essa operacao
                            aux = 'Encontrado' # cliente encontrado / senao ele nao imprime nada e sai
                        
                    sair = input("SAIDA [s]: ").upper()
                    if sair == "S":
                        sair = False
                        
                return print(aux)
                    
            
                        
        def produtos(opcao): #Funcao de produtos parametro opcao == 4
            global carrinho # global carrinho
            carrinho = 0
            auxiliar = 0
            preco_total = 0
            total = 0
            res= True
            if opcao == 4:
                print("Para ter acesso a loja insira o codigo do cachorro!! ")
                time.sleep(0.2)
                global verifica
                verifica = int(input("Digite o código do cachorro: "))
                verifica_aux.append(verifica)
                if verifica in cod_cachorro_lista: # se o codigo do cachorro estiver inserido dentro da lista entao ele tem acesso
                    lista_produtos() # layout dos produtos
                    while res == True:
                        print()
                        print("--------------------------------------------------------")
                        escolha = int(input("Digite o numero do produto que deseja comprar: "))
                        print("--------------------------------------------------------")
                        if escolha == 1:
                            print("O preço do produto é de:",preco_tapete,"Reais!")
                            auxiliar = preco_tapete
                            
                        elif escolha == 2:
                            print("O preço do produto é de",preco_racao,"Reais")
                            auxiliar = preco_racao
                        
                        elif escolha == 3:
                            print("O preço do produto é de",preco_pingente,"Reais")
                            auxiliar = preco_pingente
                        elif escolha == 4:
                            print("O preço do produto é de",preco_coleira,"Reais")
                            auxiliar = preco_coleira
                        elif escolha == 5:
                            print("O preço do produto é de",preco_guia,"Reais")
                            auxiliar = preco_guia
                        elif escolha == 6:
                            print("O preço do produto é de",preco_conjunto,"Reais")
                            auxiliar = preco_conjunto
                        elif escolha == 7:
                            print("O preço do produto é de",preco_bebedouro,"Reais")
                            auxiliar = preco_bebedouro
                        elif escolha == 8:
                            print("O preço do produto é de",preco_comedouro,"Reais")
                            auxiliar = preco_comedouro
                        
                            
                        res = input("FINALIZAR COMPRA [S/N]: ").upper()
                        carrinho += auxiliar # variavel que acumula o total de compras realizadas
                        #
                        print()
                        print("O valor total da compra é de",carrinho,"Reais!")
                        print()
                        if res == "S":
                            total = carrinho # entao total recebe a variavel que acumula
                            break
                        else:
                            res = True
                    carrinho_lista.append(total) #a lista adiciona todos os totais
                elif cod_cachorro == 0:
                    print("é necessario fazer o cadastro para entrar no programa de produtos!")
                    
                else:
                    print("Codigo cachorro invalido!")
  
                return verifica,carrinho_lista #retorna verifia e a lista de compras
                    
        def arquivo(cadastro,produtos):
            """
            Essa Funcao joga todos os cadastros dentro de um arquivo e os amazena
            """
            salva = 0
            cont = 0
            arquivo = open("Cadastros_salvos.txt","w")
            print("-------------- Cadastros Salvos --------------- ",file = arquivo)
            for k in cadastro:
                nome = k[0]
                cpf = k[1]
                endereço = k[2]
                nome_cachorro = k[3]
                codigo_cachorro = k[4]
                print("Nome:",nome,file=arquivo)
                print("CPF:",cpf,file=arquivo)
                print("ENDEREÇO:",endereço,file=arquivo)
                print("Nome do Cachorro:",nome_cachorro,file=arquivo)
                print("Codigo_ cachorro:",codigo_cachorro,file=arquivo)
                print("\n",file=arquivo)
            if codigo_cachorro in verifica_aux:
                #print(carrinho_lista)
                for i in carrinho_lista:
                    salva = i
                    cont += 1
                    print("Compra realizada do cadastro:",cont,"total",salva,"Reais",file=arquivo)
            #print(carrinho_lista)
                    
            print("------------------------------------------------",file=arquivo)
            arquivo.close()
           
             
            
            
                    

        cadastros(opcao)
        listar(opcao,codigo)
        search(opcao,cadastro)
        produtos(opcao)
        arquivo(cadastro,produtos)
        encerrar = input("Deseja sair [S/N]: ").upper()
        if encerrar == "S":
            print("Voce saiu do Programa!")
            break
        else:
            opcao = int(input("Digite sua opcao: "))
    
