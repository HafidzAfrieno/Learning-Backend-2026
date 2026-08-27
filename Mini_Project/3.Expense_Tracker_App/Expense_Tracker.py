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
        self.parser_add.add_argument("--decription",default="",type=str, help="Deskripsi Pengeluaran yang akan ditambahkan")
        self.parser_add.add_argument("--amount",default=0,type=int, help="Jumlah Uang yang akan ditambahkan")

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

class ExpenseCalculator:
    def __init__(self):
        self.nominal = 0

    def sum_all_expense(self, data: list):
        self.nominal = 0 
        for item in data:
            self.nominal += item.get("amount", 0)
        return self.nominal

class JsonFileHandler(InputData):
    def __init__(self):
        super().__init__()
        self.calcu = ExpenseCalculator()
        self.id = ""
        self.decriptions = ""
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
        expense_id = str(uuid.uuid4())[:8]
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.id = expense_id
        self.decriptions = parsed_argumens.decription
        self.amount = parsed_argumens.amount
        self.date = created_at

        new_task = {
            "id"           : self.id,
            "decriptions" : self.decriptions,
            "amount"       : self.amount,
            "date"         : self.date
        }

        task_list = self.openFilejson()
        task_list.append(new_task)
        with open(self.fileName, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=4, ensure_ascii=False)

        print(f"Expense added successfully (ID: {self.id})!")

    def list_data(self):
        expense_list = self.openFilejson()
        if not expense_list:
            print("Belum ada expense yang tersimpan.")
            return

        print(f"{'# ID':<11} {'Date':<12} {'Description':<15} {'Amount'}")
        for expense in expense_list:
            item_id = str(expense.get("id","-"))
            date    = str(expense.get("date","  ")).split(" ")[0]
            desc    = expense.get("decriptions","  ")
            amount  = expense.get('amount', 0)
            print(f"#{item_id:<10} {date:<12} {desc:<15} ${amount}")

    def summary_data(self,parsed_argumens):
        expense_list = self.openFilejson()
        if not expense_list:
            print("Belum ada expense yang tersimpan.")
            return
        month_data = getattr(parsed_argumens, "month", None)

        if month_data:
            filtered_list = []  # Mengambil bulan dari string tanggal 'YYYY-MM-DD'
            for exp in expense_list:
                date_str = exp.get("date", "")
                exp_month = int(date_str.split("-")[1])
                if exp_month == month_data:
                    filtered_list.append(exp)

            count_inMonth= self.calcu.sum_all_expense(filtered_list)
            print(f"# Total expenses: ${count_inMonth}")
        else:
            all_count = self.calcu.sum_all_expense(expense_list)
            print(f"# Total expenses: ${all_count}")

def main():
    app = JsonFileHandler()
    parsed_args = app.parse_arguments()

    if parsed_args.command == "add":
        app.create_data(parsed_args)
    elif parsed_args.command == "list":
        app.list_data()
    elif parsed_args.command == "summary":
        app.summary_data(parsed_args)

if __name__ == "__main__":
    main()