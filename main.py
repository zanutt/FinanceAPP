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
        opcao = input("""Bem vindo ao App de Finanças digite a opcaoção desejada\n
                   [1]: Adciona Divida/Receita\n
                   [2]: Deleta Divida/Provento\n
                   [3]: Mostrar Divida/Provento\n
                   [4]: Mostar Resumo das finanças\n
                   [5]: para sair\n""")
        if opcao == '1':
            opcao_criar = input("""Selecione a opção\n
                                [1]: Adcionar Divida\n
                                [2]: Adicionar Provento\n""")
            if opcao_criar == '1':
                criar_divida()
            elif opcao_criar == '2':
                criar_provento()
            else:
                print("Opção invalida")
                continue


        elif opcao == '2':
            opcao_delete = input("""Selecione a opção\n
                                [1]: Deletar Divida\n
                                [2]: Deletar Provento\n""")
            if opcao_delete == '1':
                deletar_divida()
            elif opcao_delete == '2':
                deletar_provento()
            else:
                print("Opção invalida")
                continue
            

            
        elif opcao == '3':
            opcao_mostrar = input("""Selecione a opção\n
                                [1]: Mostrar Dividas\n
                                [2]: Mostrar Proventos\n""")
            if opcao_mostrar == '1':
                mostrar_divida()
            elif opcao_mostrar == '2':
                mostrar_provento()
            else:
                print("Opção invalida")
                continue

        elif opcao == '4':
            soma_contas() 

        elif opcao == '5':
            break

    
def criar_divida() -> None:
    # Lógica para criar uma nova dívida
    valor_divida = float(input("Digite o valor da divida: R$"))
    nome_divida = input("Nome da divida (ex.: Cartão): ")
    if dividas.get(nome_divida) is None:
        dividas[nome_divida] = valor_divida
        print(f"Divida {nome_divida} criada")
        
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
    # Salvar os dados, mudar para CSV?
    with open ('Perfis.txt', 'w') as arq:
        arq.write('\nDividas:\n')
        for k, v in dividas.items():
            arq.write(f'{k}: {v}\n')
        
        arq.write('\nProventos:\n')
        for k, v in proventos.items():
            arq.write(f'{k}: {v}\n')            
        arq.close
        
    


def definir_metas()-> None:
    # Lógica para definir metas financeiras
    raise NotImplementedError





if __name__ == '__main__':    
    menu()