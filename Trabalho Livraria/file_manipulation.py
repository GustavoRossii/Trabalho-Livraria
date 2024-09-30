import os
import pathlib
import csv
import shutil
from datetime import datetime

class FileManipulator:

    def __init__(self, backup_dir):
        self.backup_dir = pathlib.Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def exportar_dados_para_csv(self, data):
        file_path = self.backup_dir / 'livros.csv'
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "titulo", "autor", "ano_publicacao", "preco"])
            for row in data:
                writer.writerow(row)


    def importar_dados_de_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            data = []
            for row in reader:
                data.append({
                    'id': int(row[0]),
                    'titulo': row[1],
                    'autor': row[2],
                    'ano_publicacao': int(row[3]),
                    'preco': float(row[4])
                })
            return data

    def fazer_backup_do_banco_de_dados(self, db_file):
        backup_file = self.backup_dir / f'backup_{db_file}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'
        shutil.copy(db_file, backup_file)

    def limpar_backups_antigos(self):
        backups = sorted(self.backup_dir.glob('backup_*'), reverse=True)
        for backup in backups[5:]:
            os.remove(backup)
