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
        ##conn.commit()
        ##cur.close()
        ##conn.close()





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


    def adicionar_divida(self, nome, valor, categoria, data, finance_id=1):
        try:
            cur.execute('INSERT INTO finances VALUES (DEFAULT, %s, %s, %s, %s, %s)',
                        (nome, valor, categoria, finance_id, data))
            conn.commit()
        except Exception as e:
            print("Error:", e)
            conn.rollback()  
        finally:
            pass

    def adicionar_provento(self, nome, valor, categoria, data, finance_id=2):
        try:
            cur.execute('INSERT INTO finances VALUES (DEFAULT, %s, %s, %s, %s, %s)',
                        (nome, valor, categoria, finance_id, data))
            conn.commit()
        except Exception as e:
            print("Error:", e)
            conn.rollback()  
        finally:
            pass
        
    def mostrar_dividas(self, finance_id=1):
        # Execute a consulta SQL para dívidas com base no finance_id
        cur.execute("SELECT * FROM finances WHERE finance_id = %s AND categoria = 'divida'", (finance_id,))
        # Recupere os resultados
        dividas = cur.fetchall()
        # Imprima os resultados
        for divida in dividas:
            print(divida)

    def mostrar_proventos(self, finance_id=2):
        # Execute a consulta SQL para proventos com base no finance_id
        cur.execute("SELECT * FROM finances WHERE finance_id = %s AND categoria = 'provento'", (finance_id,))
        # Recupere os resultados
        proventos = cur.fetchall()
        # Imprima os resultados
        for provento in proventos:
            print(provento)

    def deletar_divida(self, nome, finance_id=1):
        try:
            cur.execute("DELETE FROM finances WHERE nome = %s AND finance_id = %s", (nome, finance_id))
            conn.commit()
            print(f"Dívida {nome} deletada.")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    def deletar_provento(self, nome, finance_id=2):
        try:
            cur.execute("DELETE FROM finances WHERE nome = %s AND finance_id = %s", (nome, finance_id))
            conn.commit()
            print(f"Provento {nome} deletado.")
        except Exception as e:
            print("Error:", e)
            conn.rollback()


    def calcular_saldo(self, finance_id=1):
        try:
            cur.execute("SELECT SUM(CASE WHEN finance_id = %s THEN valor ELSE -valor END) AS saldo FROM finances", (finance_id,))
            saldo = cur.fetchone()[0]
            print(f"Saldo: R${saldo}")
        except Exception as e:
            print("Error:", e)

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

    # Feche o cursor e a conexão
    cur.close()
    conn.close()
