"""
AliasManager manages all system aliases in MacOs.
"""

import os

class AliasManager:

    def __init__(self, filepath: str = "") -> None:
        """
        Initialization of the AliasManager. 
        Loads data from filepath and creates a backup

        param filepath: filepath of the aliases. Optional.

        returns None
        """
        self.filedata = self.__load_file(filepath)

        if not self.filedata:
            exit("Alias file could not be loaded.")

        self.__create_backup()     

    def __load_file(self, filepath: str) -> str:
        """
        Loads file from filepath

        param filepath: Filepath of the aliasses. (Optional: Will otherwise take system default)

        returns str: File data from the loaded file
        """
        paths = [filepath, f"{os.environ.get('HOME')}/.zshrc", f"{os.environ.get('USER_ZDOTDIR')}/.zshrc"]

        for path in paths:
            if os.path.exists(path):
                self.filepath = path
                with open(self.filepath, "r") as file:
                    return file.read()
            
    def __save_file(self, suffix: str = "") -> None:
        """
        Saves file to the set filepath.

        param suffix: Add a suffix to the savefile.

        returns None
        """
        try:
            with open(f"{self.filepath}{suffix}", "w") as outfile:
                outfile.write(self.filedata)
        except FileNotFoundError:
            exit(f"Couldn't write to file.")

    def __create_backup(self) -> None:
        """
        Creates a backup of the filedata

        returns None
        """
        self.__save_file(".prev")

    # PUBLIC METHODS

    def add(self, key: str, value: str) -> None:
        """
        Add an alias to the system aliases
        
        param key: Key for the alias
        param value: Command for the alias

        returns None
        """
        newline = key+'="' + value + '"'
        self.filedata = f"{self.filedata}\nalias {newline}"
        print(f"Adding line  : '{newline}'")
        self.__save_file()

    def remove(self, key: str) -> None:
        """
        Remove an alias from the system aliases
        
        param key: Key of the alias

        returns None
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
        
    def show(self, key: str = "") -> None:
        """
        Show an alias of the system aliases
        
        param key: Key of the alias

        returns None
        """
        lines = self.filedata.split("\n")
        if key:
            search_for = f"alias {key}="
        else:
            search_for = "alias "

        displayline = ""
        for line in lines:
            if line.find(search_for) >= 0:
                displayline = line.replace("alias ", "")
                print(f"Found: '{displayline}'")

        if not displayline:
            print(f"Key '{key}' not found.")


alias_manager = AliasManager()

alias_manager.remove("t")