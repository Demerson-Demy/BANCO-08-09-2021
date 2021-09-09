import sqlite3

conector = sqlite3.connect("vendas1.db")
cursor = conector.cursor()

# TABELA IMAGENS
cursor.execute("""
CREATE TABLE imagens (
        Img_Codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Imagem LONGBLOB NOT NULL 


);
""")

conector.commit()
cursor.close()
conector.close()

print("Tabela criada com sucesso")
print("Fim do Programa")