# enriquecer os dados adicionando no destino uma coluna com a margem de lucro de cada produto
import csv
import sqlite3

# função para remover o ponto da última coluna
def remove_ponto(valor):
    return int(valor.replace('.',''))

# abre o arquivo csv com os dados da produção de alimentos
with open('./config/producao_alimentos.csv','r') as file:
    # cria um leitor de csv para ler o arquivo
    reader = csv.reader(file)
    
    # pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # conect ao banco de dados
    conn = sqlite3.connect('./config/dados.db')

    # deleta a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    # cria uma nova tabela para armazenar os dados de produção de alimentos com a nova coluna 'margem_de_lucro'
    conn.execute('''CREATE TABLE producao(
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER,
                    margem_lucro REAL
                    )''')

    # insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            #remove o ponto do valor da última coluna e converte para inteiro
            row[3] = remove_ponto(row[3])
            
            # calcula a margem de lucro bruta com base no valor médio de vendas e na receita total
            margem_lucro = (row[3] / float(row[1])) - float(row[2])
            
            # insere a linha com a nova coluna 'margem_lucro' na tabela do banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES(?,?,?,?,?)',(row[0],row[1],row[2],row[3], margem_lucro))
    conn.commit()
    conn.close()

print("Job concluído com sucesso!")

