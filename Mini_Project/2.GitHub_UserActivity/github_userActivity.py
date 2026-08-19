from urllib.request import Request
from os.path import exists
import os

class EnvironmentLoader:
    def __init__(self,filepath = ".env"):
        self.filepath = filepath
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
                    key,value = line.split("=",1)
                    key = key.strip()
                    value = value.strip()
        os.environ[key] = value

    def get_env(self, key, default=None):
        return os.getenv(key, default)

class RequestApi:
    def __init__(self):
        pass



