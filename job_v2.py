# carregar somente registros com quantidade produzida superior a 10.
import csv
import sqlite3

# abre o arquivo CSV com os dados de produção de alimentos
with open('./config/producao_alimentos.csv','r') as file:
    # cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)
    # pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)
    
    # conecta ao banco de dados
    conn = sqlite3.connect('./config/dados.db')
    # deleta a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')
    
    # cria uma nova tabela para armazenar os dados de produção de alimentos
    conn.execute('''CREATE TABLE producao( 
             produto TEXT,
             quantidade INTEGER,
             preco_medio REAL,
             receita_total REAL)''')
    
    # insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
         if int(row[1]) > 10:
             conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES(?,?,?,?)', row)
    conn.commit()
    conn.close()
        
print("Job concluido com sucesso!")  