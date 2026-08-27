import json
import argparse
import uuid
from os import path
from datetime import datetime

class InputData:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="APP TASK TRACKER")
        self.subparser = self.parser.add_subparsers(dest="command", help="Perintah Yang Tersedia")
        self.init_parsers()

    def init_parsers(self):
        # Parser 'add'
        self.parser_add = self.subparser.add_parser("add", help="Menambah Pengeluaran Baru")
        self.parser_add.add_argument("--description", type=str, help="Deskripsi Pengeluaran yang akan ditambahkan")
        self.parser_add.add_argument("--amount", type=int, help="Jumlah Uang yang akan ditambahkan")

        # Parser untuk 'list'
        self.parser_list = self.subparser.add_parser("list", help="Menampilkan semua pengeluaran")

        # Parser untuk 'summary'
        self.parser_list = self.subparser.add_parser("summary", help="Menampilkan Ringkasan Pengeluaran")
        self.parser_list.add_argument("--month",nargs="?" ,type=int, help="Menampilkan Ringkasan Tiap Bulan")

        # Parser 'delete'
        self.parser_delete = self.subparser.add_parser("delete", help="Menghapus Pengeluaran")
        self.parser_delete.add_argument("--id", type=str, help="ID Pengeluaran yang dihapus")

    def parse_arguments(self):
        self.args = self.parser.parse_args()
        return self.args

class JsonFileHandler(InputData):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.descriptions = ""
        self.amount = 0
        self.date = ""
        self.fileName = "data.json"

    def openFilejson(self):
        task_list = []
        if path.exists(self.fileName):
            try:
                with open(self.fileName, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        task_list = data
                    elif isinstance(data, dict):
                        task_list = [data]
            except json.JSONDecodeError:
                task_list = []
        return task_list

    def create_data(self, parsed_argumens):
        task_id = str(uuid.uuid4())[:8]
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.id = task_id
        self.descriptions = parsed_argumens.description
        self.amount = self.parse_arguments.amount
        self.date = created_at

        new_task = {
            "id"           : self.id,
            "descriptions" : self.descriptions,
            "Amount"       : self.amount,
            "Date"         : self.date
        }

        task_list = self.openFilejson()
        task_list.append(new_task)
        with open(self.fileName, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=4, ensure_ascii=False)
        print(f"Berhasil menambahkan dan menyimpan Pengeluaran (ID: {task_id})!")

    def list_data(self, parsed_argumens):
        expense_list = self.openFilejson()
        
        
            

class ExpenseCalculator:
    def __init__(self):
        self.nominal = 0
        self.date = datetime()
        self.id = ""

    def sum_all_expense(self):
        print()


        

        

def main():
    app = JsonFileHandler()
    parsed_args = app.parse_arguments()

if __name__ == "__main__":
    main()