# testar a conexão com o banco de dados
import csv
import sqlite3

# cria um novo banco de dados
conn = sqlite3.connect('./config/dados.db')

# cria uma tabela para armazenar os dados de produção de alimentos
conn.execute('''CREATE TABLE producao( 
             produto TEXT,
             quantidade INTEGER,
             preco_medio REAL,
             receita_total REAL)''')

# grava e fecha a conexao
conn.commit()
conn.close()

# abre o arquivo csv com os dados de producao de alimentos
with open('./config/producao_alimentos.csv', 'r') as file:
    # cria um leitor de CSV para leo o arquivo
    reader = csv.reader(file)
    
    #pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)
    
    # conecta ao banco de dados
    conn = sqlite3.connect('./config/dados.db')
    
    # insere cada linha do arquivo na tabela do banco de dados
    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES(?,?,?,?)', row)
    conn.commit()
    conn.close()
        
print("Job concluido com sucesso!")        
        
        

        