#funcoes basicas
dividas = {
    "cartao": 1500,
    "tv": 2000,
    "smartphone": 800.76,
}
proventos = {
    "salario": 7500,
}
def menu()-> None:
    #Menu Principal da aplicação mais para frente sera um GUI para melhor usabilidade
    while True:
        op = input("Bem vindo ao App de Finanças digite a opção desejada\n1: Adciona divida\n2: Adciona provento\n 3: Deleta Divida\n 4: Deleta provento\nSair: para sair\n")
        if op == '1':
            criar_divida()
        elif op == '2':
            criar_provento()
        elif op == '3':
            deletar_divida()
        elif op == '4':
            deletar_provento()
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


def criar_provento()-> None:
    # Lógica para criar uma nova entrada de provento
    valor_liquido = float(input("Digite o valor do provento: R$"))
    nome_provento = input("Nome do provento (ex.: Salário): ")
    if proventos.get(nome_provento) is None:
        proventos[nome_provento] = valor_liquido
        
    else:
        print("\nJá existe um provento com esse nome.")

def mostrar_proventos () -> None:
    # Lógica para mostrar a lista ordenada de dividas
    print(proventos)

def deletar_divida()-> None:
    # Lógica para excluir uma dívida
    nome_divida = input("Qual o nome da divida que voce quer excluir?")
    if dividas.get(nome_divida) != None:
        del dividas[nome_divida]
        print('\nDivida apagada!')
    else:
        raise  ValueError('A divida não foi encontrada.')
    
def deletar_provento()-> None:
    # Lógica para excluir uma entrada de provento
    nome_provento = input("Qual o nome do provento que voce quer excluir?")
    if proventos.get(nome_provento) != None:
        del proventos[nome_provento]
        print('\nDivida apagada!')
    else:
        raise  ValueError('O provento não foi encontrada.')


def soma_contas()-> float:
    # Lógica para modificar uma dívida ou entrada de provento existente
    valor_dividas = []
    valor_proventos= []
    for v in dividas:
        valor_dividas.append(dividas[v])
    for v in proventos:
        valor_proventos.append(proventos[v])

    return (sum(valor_proventos) - sum(valor_dividas))







def salvar_contas()-> None:
    # Lógica para salvar as contas (positivas e negativas)
    raise NotImplementedError


def definir_metas()-> None:
    # Lógica para definir metas financeiras
    raise NotImplementedError





if __name__ == '__main__':    
    print (soma_contas())
    print (dividas)