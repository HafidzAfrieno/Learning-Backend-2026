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
        # Parser untuk 'add'
        self.parser_add = self.subparser.add_parser("add", help="Menambah Tugas Baru")
        self.parser_add.add_argument("task", type=str, help="Deskripsi tugas yang akan ditambahkan")

        # Parser untuk 'update'
        self.parser_update = self.subparser.add_parser("update", help="Mengedit Tugas")
        self.parser_update.add_argument("id", type=str, help="ID tugas yang akan diubah")
        self.parser_update.add_argument("task", type=str, help="Deskripsi tugas yang baru")

    def parse_arguments(self):
        self.args = self.parser.parse_args()
        return self.args

class JsonFileHandler(InputData):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.descriptions = ""
        self.status = "todo"
        self.createdAt = ""
        self.updatedAt = ""
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
        self.descriptions = parsed_argumens.task
        self.createdAt = created_at
        self.updatedAt = created_at

        new_task = {
            "id"           : self.id,
            "descriptions" : self.descriptions,
            "status"       : self.status,
            "createdAt"    : self.createdAt,
            "updatedAt"    : self.updatedAt
        }

        task_list = self.openFilejson()
        task_list.append(new_task)
        with open(self.fileName, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=4, ensure_ascii=False)

        print(f"Berhasil menambahkan dan menyimpan Tugas (ID: {task_id})!")

    def update_data(self, parsed_argumens):
        task_id = parsed_argumens.id
        new_description = parsed_argumens.task
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        task_list = self.openFilejson()
        updated = False

        for task in task_list:
            if task["id"] == task_id:
                task["descriptions"] = new_description
                task["updatedAt"] = updated_at
                updated = True
                break

        if updated:
            with open(self.fileName, "w", encoding="utf-8") as file:
                json.dump(task_list, file, indent=4, ensure_ascii=False)
            print(f"Berhasil memperbarui Tugas (ID: {task_id})!")
        else:
            print(f"Tugas dengan ID '{task_id}' tidak ditemukan!")


def main():
    app = JsonFileHandler()
    parsed_args = app.parse_arguments()

    if parsed_args.command == "add":
        app.create_data(parsed_args)
    elif parsed_args.command == "update":
        app.update_data(parsed_args)
    else:
        app.parser.print_help()

if __name__ == "__main__":
    main()