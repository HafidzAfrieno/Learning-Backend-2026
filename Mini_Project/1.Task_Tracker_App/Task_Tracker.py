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
        self.parser_add = self.subparser.add_parser("add", help="Menambah Tugas Baru")
        self.parser_add.add_argument("task", type=str, help="Deskripsi tugas yang akan ditambahkan")

        # Parser 'update'
        self.parser_update = self.subparser.add_parser("update", help="Mengedit Tugas")
        self.parser_update.add_argument("id", type=str, help="ID tugas yang akan diubah")
        self.parser_update.add_argument("task", type=str, help="Deskripsi tugas yang baru")

        # Parser 'delete'
        self.parser_delete = self.subparser.add_parser("delete", help="Menghapus Tugas")
        self.parser_delete.add_argument("id", type=str, help="ID tugas yang akan dihapus")

        # Parser untuk 'mark-done'
        self.parser_mark = self.subparser.add_parser("mark-done", help="Menandai Tugas Selesai")
        self.parser_mark.add_argument("id", type=str, help="ID tugas yang ingin ditandai selesai")

        # Parser untuk 'mark-progress'
        self.parser_mark = self.subparser.add_parser("mark-progress", help="Menandai Tugas Masih Proses")
        self.parser_mark.add_argument("id", type=str, help="ID tugas yang ingin ditandai Masih Proses")

        # Parser untuk 'list'
        self.parser_list = self.subparser.add_parser("list", help="Menampilkan Tugas Yang Dipilih")
        self.parser_list.add_argument("status",nargs="?" ,type=str, help="Status Tugas Yang Ingin Ditampilkan")

    def parse_arguments(self):
        self.args = self.parser.parse_args()
        return self.args


class JsonFileHandler(InputData):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.descriptions = ""
        self.status = "Pending"
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

    def delete_data(self,parsed_argumens):
        task_id = parsed_argumens.id
        task_list = self.openFilejson()
        filter_taskList = [task for task in task_list if task["id"] != task_id]

        if len(filter_taskList) < len(task_list):
            with open(self.fileName, "w", encoding="utf-8") as file:
                json.dump(filter_taskList, file, indent=4, ensure_ascii=False)
            print(f"Berhasil menghapus Tugas dengan ID: {task_id}!")
        else:
            print(f"Tugas dengan ID '{task_id}' tidak ditemukan!")

    def mark_done(self,parsed_argumens):
        task_id = parsed_argumens.id
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        task_list = self.openFilejson()
        updated = False

        for task in task_list:
            if task["id"] == task_id:
                task["status"] = "Done"
                task["updatedAt"] = updated_at
                updated = True
                break

        if updated:
            with open(self.fileName, "w", encoding="utf-8") as file:
                json.dump(task_list, file, indent=4, ensure_ascii=False)
            print(f"Berhasil memperbarui Status (ID: {task_id})!")
        else:
            print(f"Tugas dengan ID '{task_id}' tidak ditemukan!")

    def mark_progress(self,parsed_argumens):
            task_id = parsed_argumens.id
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
            task_list = self.openFilejson()
            updated = False
    
            for task in task_list:
                if task["id"] == task_id:
                    task["status"] = "Progress"
                    task["updatedAt"] = updated_at
                    updated = True
                    break
    
            if updated:
                with open(self.fileName, "w", encoding="utf-8") as file:
                    json.dump(task_list, file, indent=4, ensure_ascii=False)
                print(f"Berhasil memperbarui Status (ID: {task_id})!")
            else:
                print(f"Tugas dengan ID '{task_id}' tidak ditemukan!")

    def list_data(self, parsed_argumens):
        task_list = self.openFilejson()
        if not task_list:
            print("Belum ada tugas yang tersimpan.")
            return
        
        status_data = getattr(parsed_argumens, 'status', None) #supaya mengambil status opsional

        if status_data:
            task_list = [task for task in task_list if task["status"].lower() == status_data.lower()]
            if not task_list:
                print(f"Tidak ada tugas dengan status '{status_data}'.")
                return

        print("\n--- DAFTAR TUGAS ---")
        for task in task_list:
            print(f"ID     : {task['id']}")
            print(f"Task   : {task['descriptions']}")
            print(f"Status : {task['status']}")
            print(f"Dibuat : {task['createdAt']}")
            print("-" * 25)
        
def main():
    app = JsonFileHandler()
    parsed_args = app.parse_arguments()

    if parsed_args.command == "add":
        app.create_data(parsed_args)
    elif parsed_args.command == "update":
        app.update_data(parsed_args)
    elif parsed_args.command == "delete":
        app.delete_data(parsed_args)
    elif parsed_args.command == "mark-done":
        app.mark_done(parsed_args)
    elif parsed_args.command == "mark-progress":
        app.mark_progress(parsed_args)
    elif parsed_args.command == "list":
        app.list_data(parsed_args)
    else:
        app.parser.print_help()

if __name__ == "__main__":
    main()