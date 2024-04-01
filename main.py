#funcoes basicas
dividas = {}
liquidez = {}
def menu()-> None:
    #Menu Principal da aplicação mais para frente sera um GUI para melhor usabilidade
    while True:
        op = input("Bem vindo ao App de Finanças digite a opção desejada\n1: Adciona divida\n2: Adciona Lucro\n 3: Deleta Divida\n 4: Deleta lucro\nSair: para sair\n")
        if op == '1':
            criar_divida()
        elif op == '2':
            criar_lucro()
        elif op == '3':
            deletar_divida()
        elif op == '4':
            deletar_lucro()
        elif op == 'sair':
            break

    
def criar_divida() -> None:
    # Lógica para criar uma nova dívida
    valor_divida = float(input("Digite o valor da divida: R$"))
    nome_divida = input("Nome da divida (ex.: Cartão): ")
    if dividas.get(nome_divida) is None:
        dividas[nome_divida] = valor_divida
        
    else:
        print("\nJá existe uma divida com esse nome.")
    
def mostrar_dividas () -> None:
    # Lógica para mostrar a lista ordenada de dividas
    print(dividas)


def criar_lucro()-> None:
    # Lógica para criar uma nova entrada de lucro
    valor_liquido = float(input("Digite o valor do provento: R$"))
    nome_provento = input("Nome do provento (ex.: Salário): ")
    if liquidez.get(nome_provento) is None:
        liquidez[nome_provento] = valor_liquido
        
    else:
        print("\nJá existe um provento com esse nome.")

def deletar_divida()-> None:
    # Lógica para excluir uma dívida
    nome_divida = input("Qual o nome da divida que voce quer excluir?")
    if dividas.get(nome_divida) != None:
        del dividas[nome_divida]
        print('\nDivida apagada!')
    else:
        raise  ValueError('A divida não foi encontrada.')
    
def deletar_lucro()-> None:
    # Lógica para excluir uma entrada de lucro
    nome_lucro = input("Qual o nome do provento que voce quer excluir?")
    if liquidez.get(nome_lucro) != None:
        del liquidez[nome_lucro]
        print('\nDivida apagada!')
    else:
        raise  ValueError('O provento não foi encontrada.')


def soma_contas()-> None:
    # Lógica para modificar uma dívida ou entrada de lucro existente
    raise NotImplementedError


def salvar_contas()-> None:
    # Lógica para salvar as contas (positivas e negativas)
    raise NotImplementedError


def definir_metas()-> None:
    # Lógica para definir metas financeiras
    raise NotImplementedError





if __name__ == '__main__':    
    menu()
    print (dividas)