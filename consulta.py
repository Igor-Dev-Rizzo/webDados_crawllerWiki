import mysql.connector

conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='scraping')
cursor = conexao.cursor()
consulta = ("select titulo, url, conteudo from paginas")
cursor.execute(consulta)

for (titulo, url, conteudo) in cursor:
    print(f"titulo: {titulo}, url: {url}, conteudo: {conteudo}")
cursor.close()
conexao.close()