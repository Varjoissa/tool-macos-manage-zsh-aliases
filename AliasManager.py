"""
AliasManager manages all system aliases in MacOs.
"""

import os

class AliasManager:

    def __init__(self, filepath: str = "") -> None:
        """
        """
        self.filedata = self.__load_file(filepath)
        self.__create_backup()     

    def __load_file(self, filepath: str) -> str:
        """
        """
        try:
            self.filepath = filepath
            with open(filepath, "r") as file:
                return file.read()
        except FileNotFoundError:
            self.filepath = f"{os.environ.get('USER_ZDOTDIR')}/.zshrc"
            with open(self.filepath, "r") as file:
                return file.read()
            
    def __save_file(self, suffix: str = ""):
        """
        """
        try:
            with open(f"{self.filepath}{suffix}", "w") as outfile:
                outfile.write(self.filedata)
        except FileNotFoundError:
            exit(f"Couldn't write to file.")

    def __create_backup(self):
        """
        """
        self.__save_file(".prev")

    def add(self, key: str, value: str):
        """
        """
        newline = key+'="' + value + '"'
        self.filedata = f"{self.filedata}\nalias {newline}"
        print(f"Adding line  : '{newline}'")
        self.__save_file()

    def remove(self, key: str):
        """
        """
        lines = self.filedata.split("\n")
        search_for = f"alias {key}="
        newdata = ""
        for line in lines:
            if line.find(search_for) < 0:
                newdata = f"{newdata}\n{line}"
            else: 
                print(f"Removing line: '{line}'")

        self.filedata = newdata
        self.__save_file()
        
    def show(self, key: str):
        """
        """
        lines = self.filedata.split("\n")
        search_for = f"alias {key}="
        displayline = ""
        for line in lines:
            if line.find(search_for) >= 0:
                displayline = line.replace("alias ", "")
                print(f"Found: '{displayline}'")

        if not displayline:
            print(f"Key '{key}' not found.")