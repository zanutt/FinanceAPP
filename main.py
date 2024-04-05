## SQL Db
import psycopg2
## Iniciando a conexão com a DB
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456", port = 5432)
cur = conn.cursor()

## iniciando  o banco de dados se não existir, criar um novo banco de dados.
cur.execute("""CREATE TABLE IF NOT EXISTS finances(
            id BIGSERIAL PRIMARY KEY,
            nome VARCHAR (255),
            valor INT,
            categoria VARCHAR(50),
            finance_id INT,
            data DATE
);
""")
conn.commit()
cur.close()
conn.close()




class Divida:
    def __init__(self, nome, valor, categoria, finance_id, data):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        self.finance_id = finance_id
        self.data = data

class Provento:
    def __init__(self, nome, valor, categoria, finance_id, data):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        self.finance_id = finance_id
        self.data = data

class Financas:
    def __init__(self):
        self.dividas = []
        self.proventos = []

    def adicionar_divida(self, nome, valor, categoria, finance_id, data):
        self.dividas.append(Divida(nome, valor, categoria, finance_id, data))

    def adicionar_provento(self, nome, valor, categoria, finance_id, data):
        self.proventos.append(Provento(nome, valor, categoria, finance_id, data))

    def mostrar_dividas(self):
        for divida in self.dividas:
            print(f"{divida.nome}: R${divida.valor}")

    def mostrar_proventos(self):
        for provento in self.proventos:
            print(f"{provento.nome}: R${provento.valor}")

    def deletar_divida(self, nome):
        for divida in self.dividas:
            if divida.nome == nome:
                self.dividas.remove(divida)
                print(f"Divida {nome} deletada.")
                return
        print("Divida não encontrada.")

    def deletar_provento(self, nome):
        for provento in self.proventos:
            if provento.nome == nome:
                self.proventos.remove(provento)
                print(f"Provento {nome} deletado.")
                return
        print("Provento não encontrado.")

    def calcular_saldo(self):
        saldo = sum(provento.valor for provento in self.proventos) - sum(divida.valor for divida in self.dividas)
        return saldo
    
    ## Mudarei pra SQL
    def salvar_contas(self):
        with open('Perfis.txt', 'w') as arq:
            arq.write('Dividas:\n')
            for divida in self.dividas:
                arq.write(f"{divida.nome}: {divida.valor}\n")
            arq.write('\nProventos:\n')
            for provento in self.proventos:
                arq.write(f"{provento.nome}: {provento.valor}\n")
    ## Metas financeiras função futura
    def definir_metas(self):
        pass
    

def menu(financeiro):
    while True:
        opcao = input("""Bem vindo ao App de Finanças. Selecione a opção desejada:
            [1] Adicionar Divida/Provento
            [2] Deletar Divida/Provento
            [3] Mostrar Divida/Provento
            [4] Mostrar Resumo das Finanças
            [5] Salvar Contas
            [6] Definir Metas Financeiras
            [7] Sair\n""")
        if opcao == '1':
            opcao_criar = input("""Selecione a opção:
                                [1] Adicionar Divida
                                [2] Adicionar Provento\n""")
            if opcao_criar == '1':
                nome_divida = input("Nome da divida: ")
                valor_divida = float(input("Valor da divida: R$"))
                categoria_divida = input("Categoria da Divida: ")
                f_id = 1
                divida_vencimento = input("Data de Vencimento (DD/MM/AAAA): ")                
                financeiro.adicionar_divida(nome_divida, valor_divida, categoria_divida, f_id, divida_vencimento)
            elif opcao_criar == '2':
                nome_provento = input("Nome do provento: ")
                valor_provento = float(input("Valor do provento: R$"))
                categoria_provento = input("Categoria do provento: ")
                f_id = 2
                provento_vencimento = input("Data de Vencimento (DD/MM/AAAA): ")  
                financeiro.adicionar_provento(nome_provento, valor_provento, categoria_provento, f_id, provento_vencimento)

        elif opcao == '2':
            opcao_delete = input("""Selecione a opção:
                                [1] Deletar Divida
                                [2] Deletar Provento\n""")
            if opcao_delete == '1':
                nome_divida = input("Nome da divida a ser deletada: ")
                financeiro.deletar_divida(nome_divida)
            elif opcao_delete == '2':
                nome_provento = input("Nome do provento a ser deletado: ")
                financeiro.deletar_provento(nome_provento)

        elif opcao == '3':
            opcao_mostrar = input("""Selecione a opção:
                                [1] Mostrar Dividas
                                [2] Mostrar Proventos\n""")
            if opcao_mostrar == '1':
                financeiro.mostrar_dividas()
            elif opcao_mostrar == '2':
                financeiro.mostrar_proventos()

        elif opcao == '4':
            print(f"Saldo: R${financeiro.calcular_saldo()}")

        elif opcao == '5':
            financeiro.salvar_contas()

        elif opcao == '6':
            financeiro.definir_metas()

        elif opcao == '7':
            break


if __name__ == '__main__':
    financeiro = Financas()
    menu(financeiro)
