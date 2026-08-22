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
        print("hallo")

def main():
    print()

if __name__ == "__main__":
    main()