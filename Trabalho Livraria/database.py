import sqlite3


class LivrariaDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS livros
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                              titulo TEXT, 
                              autor TEXT, 
                              ano_publicacao INTEGER, 
                              preco REAL)''')
        self.conn.commit()

    def adicionar_livro(self, titulo, autor, ano_publicacao, preco):
        self.cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                            (titulo, autor, ano_publicacao, preco))
        self.conn.commit()

    def exibir_livros(self):
        self.cursor.execute("SELECT * FROM livros")
        return self.cursor.fetchall()

    def atualizar_preco(self, id, preco):
        self.cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (preco, id))
        self.conn.commit()

    def remover_livro(self, id):
        self.cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
        self.conn.commit()

    def buscar_livro_por_autor(self, autor):
        self.cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor,))
        return self.cursor.fetchall()