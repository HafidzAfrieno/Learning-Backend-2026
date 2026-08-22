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


    class ExpenseCalculator:
        def __init__(self):
            self.nominal = 0
            self.mounth = ""

def main():
    print()

if __name__ == "__main__":
    main()