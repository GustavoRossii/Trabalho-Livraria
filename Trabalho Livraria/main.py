# main.py
import database
import file_manipulation
import datetime
import shutil

def main():
    db_file = ' livraria.db'
    backup_dir = 'backup'

    db = database.LivrariaDB(db_file)
    file_manipulator = file_manipulation.FileManipulator(backup_dir)

    while True:
        print("\033[1;34mMenu:\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[1].\033[0m \033[1;32m Adicionar novo livro\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[2].\033[0m \033[1;32m Exibir todos os livros\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[3].\033[0m \033[1;32m Atualizar preço de um livro\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[4].\033[0m \033[1;32m Remover um livro\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[5].\033[0m \033[1;32m Buscar livros por autor\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[6].\033[0m \033[1;32m Exportar dados para CSV\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[7].\033[0m \033[1;32m Importar dados de CSV\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;34m|[8].\033[0m \033[1;32m Fazer backup do banco de dados\033[0m")
        print("\033[1;33m|------------------------------------\033[0m")
        print("\033[1;31m|[9]. Sair\033[0m")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = int(input("Digite o ano de publicação do livro: "))
            preco = float(input("Digite o preço do livro: "))
            db.adicionar_livro(titulo, autor, ano_publicacao, preco)
            file_manipulator.fazer_backup_do_banco_de_dados(db_file)

        elif choice == '2':
            livros = db.exibir_livros()
            for livro in livros:
                print(livro)

        elif choice == '3':
            id = int(input("Digite o ID do livro: "))
            preco = float(input("Digite o novo preço do livro: "))
            db.atualizar_preco(id, preco)
            file_manipulator.fazer_backup_do_banco_de_dados(db_file)

        elif choice == '4':
            id = int(input("Digite o ID do livro: "))
            db.remover_livro(id)
            file_manipulator.fazer_backup_do_banco_de_dados(db_file)

        elif choice == '5':
            autor = input("Digite o autor do livro: ")
            livros = db.buscar_livro_por_autor(autor)
            for livro in livros:
                print(livro)

        elif choice == '6':
            livros = db.exibir_livros()
            file_manipulator.exportar_dados_para_csv(livros)

        elif choice == '7':
            file_path = input("Digite o caminho do arquivo CSV: ")
            livros = file_manipulator.importar_dados_de_csv(file_path)
            for livro in livros:
                db.adicionar_livro(livro['titulo'], livro['autor'], livro['ano_publicacao'], livro['preco'])

        elif choice == '8':
            file_manipulator.fazer_backup_do_banco_de_dados(db_file)

        elif choice == '9':
            break

        else:
            print("\033[1;31m Opção inválida. Tente novamente.\033[0m")

if __name__ == "__main__":
    main()