import json
import argparse

class InputData:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="APP TASK TRACKER")
        self.subparser = self.parser.add_subparsers(dest="Commnad",help="Perintah Yang Tersedia")

    def add_data(self):
        self.parser_add = self.subparser.add_parser("add",help="Menambah Tugas Baru")
        self.parser_add.add_argument("task",type=str,help="Deskripsi tugas yang akan ditambahkan")
        self.args = self.parser.parse_args()
        return self.args

def main():
    argument = InputData()
    parsed_args = argument.add_data()
    
    if parsed_args.Commnad == "add":
        print(f"Berhasil menambahkan Tugas: {parsed_args.task}")
    else:
        argument.parser.print_help()

if __name__ == "__main__":
    main()
