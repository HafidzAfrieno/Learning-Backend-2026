import os
import json
from os.path import exists
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

class EnvironmentLoader:
    def __init__(self,):
        self.filepath = ".env"
        self.__load_env()

    def __load_env(self):
        if not exists(self.filepath):
            print("file .env tidak ada!")
        with open(self.filepath,"r",encoding="utf-8") as file:
            for line in file:
                line = line.strip() # Hilangkan spasi 
                if not line or line.startswith('#'): # Abaikan baris kosong dan #
                    continue
                
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()

                    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]

                    os.environ[key] = value

    def get_env(self, key, default=None):
        return os.getenv(key, default)

class GitHubCommitService:
    def __init__(self):
        self.env_loader = EnvironmentLoader()
        self.token = self.env_loader.get_env("TOKEN")
        self.owner = self.env_loader.get_env("OWNER")

    def get_commit_statuses(self):
        url = f"https://api.github.com/users/{self.owner}/events"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "Python-App"
        }
        req = Request(url,headers=headers,method="GET")
        try:
            with urlopen(req) as response:
                data = response.read().decode("utf-8")
                events = json.loads(data)
                for event in events:
                    event_type = event.get("type")
                    repo_name = event.get("repo",{}).get("name")
                    
                    if event_type == "PushEvent":
                        commit_count = len(event.get("payload", {}).get("commits", []))
                        print(f"- Pushed {commit_count} commits to {repo_name}")
                        
                    elif event_type == "IssuesEvent":
                        action = event.get("payload", {}).get("action")
                        if action == "opened":
                            print(f"- Opened a new issue in {repo_name}")
                            
                    elif event_type == "WatchEvent":
                        print(f"- Starred {repo_name}")
        except HTTPError as error:
            print(f"Gagal HTTP Error: {error.code} - {error.reason}")
            return None
        except URLError as errorurl:
            print(f"Gagal Koneksi: {errorurl.reason}")
            return None

if __name__ == "__main__":
    service = GitHubCommitService()
    result = service.get_commit_statuses()
    print(f"Message Commits:'{result}'")
