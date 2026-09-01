from os import path
import json
import datetime
import uuid

class JsonFileHandler():
    def __init__(self):
        super().__init__()
        self.id = ""
        self.datetime = datetime
        self.title = ""
        self.content = ""
        self.fileName = "../data/database_article.json"

    def openFilejson(self):
        article_list = []
        if path.exists(self.fileName):
            try:
                with open(self.fileName, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        article_list = data
                    elif isinstance(data, dict):
                        article_list = [data]
            except json.JSONDecodeError:
                article_list = []
        return article_list

    def create_article(self, title: str, content: str, created_at: str = None):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.content = content
        
        if not created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.created_at = created_at

        new_article = {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at
        }

        article_list = self.openFilejson()
        article_list.append(new_article)
        
        with open(self.fileName, "w", encoding="utf-8") as file:
            json.dump(article_list, file, indent=4, ensure_ascii=False)
        return new_article

    def update_data(self, article_id: str, title: str, content: str):
        article_list = self.openFilejson()
        updated = False

        for article in article_list:
            if article["id"] == article_id:
                article["title"] = title
                article["content"] = content
                article["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated = True
                break

        if updated:
            with open(self.fileName, "w", encoding="utf-8") as file:
                json.dump(article_list, file, indent=4, ensure_ascii=False)
            return True
        return False

    def delete_data(self, article_id: str):
        article_list = self.openFilejson()
        filter_articleList = [article for article in article_list if article["id"] != article_id]

        if len(filter_articleList) < len(article_list):
            with open(self.fileName, "w", encoding="utf-8") as file:
                json.dump(filter_articleList, file, indent=4, ensure_ascii=False)
            return True
        return False

    def list_data(self, article_id: str = None):
        article_list = self.openFilejson()

        if article_id:
            for article in article_list:
                if article["id"] == article_id:
                    return article
            return None
        return article_list

    