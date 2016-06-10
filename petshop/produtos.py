## produtos ##
def lista_produtos():
    print("--------------------------------")
    print("- [1] Tapete Higienico         -")
    print("- [2] Racao Premier Golden     -")
    print("- [3] Pingente Schnauzer       -")
    print("- [4] Coleira Tenflon Rosa     -")
    print("- [5] Guia Confort Latte       -")
    print("- [6] Conjunto Fuia e Coleira  -")
    print("- [7] Bebedouro Portatil       -")
    print("- [8] Comedouro Inox           -")
    print("- [S] SAIR                     -")

def tapete_higienico():
    global nome_tapete,preco_tapete
    nome_tapete = 'Tapete Higienico'
    preco_tapete = 8
    return nome_tapete,preco_tapete



def racao_premier():
    global nome_racao,preco_racao
    nome_racao = 'Racao Premier Golden'
    preco_racao = 50

    return nome_racao,preco_racao

   


def pingente_schnauzer():
    global nome_pingente,preco_pingente
    nome_pingente = 'Pingente schnauzer'
    preco_pingente = 10

    return nome_pingente,preco_pingente


def coleira_teflon_rosa():
    global nome_coleira,preco_coleira
    nome_coleira ='Coleira Tenflon Rosa'
    preco_coleira = 7

    return nome_coleira,preco_coleira

def guia_confort():
    global nome_guia,preco_guia
    nome_guia = 'Guia Confort Latte'
    preco_guia = 30
    return nome_guia,preco_guia


def conjunto_fuia_coleira():
    global nome_conjunto,preco_conjunto
    nome_conjunto = 'Conjunto Fuia e Coleira'
    preco_conjunto = 15

    return nome_conjunto,preco_conjunto

def bebedouro_portatil():
    global nome_bebedouro,preco_bebedouro
    nome_bebedouro= 'Bebedouro Portatil Pet Drink'
    preco_bebedouro = 16

    return nome_bebedouro,preco_bebedouro

def comedouro_inox():
    global nome_comedouro,preco_comedouro
    nome_comedouro = 'Comedouro Inox'
    preco_comedouro = 3

    return nome_comedouro,preco_comedouro

   



def main():
    #lista_produtos()
    tapete_higienico()
    racao_premier()
    pingente_schnauzer()
    coleira_teflon_rosa()
    guia_confort()
    conjunto_fuia_coleira()
    bebedouro_portatil()
    comedouro_inox()



main()
    

















