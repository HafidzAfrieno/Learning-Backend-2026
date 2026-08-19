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
        self.repo  = self.env_loader.get_env("REPO")
        self.ref   = self.env_loader.get_env("REF")

    def get_commit_statuses(self):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/commits/{self.ref}"
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
                parsed_data = json.loads(data)
                commit_message = parsed_data["commit"]["message"]
                return commit_message
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
