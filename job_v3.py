# remover o caracter "ponto" na última coluna do arquivo para evitar que o número seja truncado
import csv
import sqlite3

# função para remover o ponto nos dados da última coluna
def remove_ponto(valor):
    return(valor.replace('.',''))

# abre o arquivo csv com os dados de produção de alimentos
with open('./config/producao_alimentos.csv','r') as file:
    # cria um leitor de csv para ler o aqruivo
    reader = csv.reader(file)
    
    # pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)
    
    # conecta ao banco d dados
    conn = sqlite3.connect('./config/dados.db')
    
    # deleta a tabela existente, se houer
    conn.execute('DROP TABLE IF EXISTS producao')
    
    # cria uma nova tabela para armazenar os dados de produção de alimentos
    conn.execute('''CREATE TABLE producao( 
                            produto TEXT,
                            quantidade INTEGER,
                            preco_medio REAL,
                            receita_total REAL)
                ''')
    
    # insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            # remove o ponto do valor da última coluna e econverte para inteiro
            row[3] = remove_ponto(row[3])
            # insere o registro no banco de dados
            conn.execute('INSERT INTO producao(produto, quantidade, preco_medio, receita_total) VALUES(?,?,?,?)', row)
    conn.commit()
    conn.close()
    
print("Job concluido com sucesso!")
            