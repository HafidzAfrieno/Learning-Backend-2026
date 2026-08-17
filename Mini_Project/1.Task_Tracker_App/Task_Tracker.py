import json
import argparse
import uuid
from os import path
from datetime import datetime

class InputData:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="APP TASK TRACKER")
        self.subparser = self.parser.add_subparsers(dest="Commnad",help="Perintah Yang Tersedia")

    def add_data(self):
        self.parser_add = self.subparser.add_parser("add",help="Menambah Tugas Baru")
        self.parser_add.add_argument("task",type=str,help="Deskripsi tugas yang akan ditambahkan")
        self.args = self.parser.parse_args()
        return self.args

class JsonFileHandler(InputData):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.descriptions = ""
        self.status = "todo"  # Default status
        self.createdAt = ""
        self.updatedAt = ""
        self.fileName = "data.json"

    def openFilejson(self):
        task_list = []
        if path.exists(self.file):
            try:
                with open(self.file,"r",encoding="utf-8") as file:
                    task_list = json.load(file)
            except json.JSONDecodeError:
                task_list = []
        return task_list
        
    def create_data(self):
        parsed_argumens = self.add_data()
        if parsed_argumens.Commmand == "add":
            task_id = str(uuid.uuid4())[:3]
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.id = task_id
            self.descriptions = parsed_argumens.task
            self.createdAt = created_at
            self.updatedAt = created_at

        new_task = {
            "id"            : self.id,
            "descriptions"  : self.descriptions,
            "status"        : self.status,
            "createdAt"     : self.createdAt,
            "updatedAt"     : self.updatedAt
        }

        tasks_list = self.openFilejson()
        tasks_list.append(new_task)
        with open(self.fileName, "w", encoding="utf-8") as file:
            json.dump(tasks_list, file, indent=4, ensure_ascii=False)

        print(f"Berhasil menambahkan dan menyimpan Tugas (ID: {self.id})!")

def main():
    app = JsonFileHandler()
    app.create_data()

if __name__ == "__main__":
    main()
