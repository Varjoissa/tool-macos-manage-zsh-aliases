"""
AliasManager manages all system aliases in MacOs.
"""

import os, sys

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
            sys.exit("Alias file could not be loaded.")

        self.__create_backup()     

    def __load_file(self, filepath: str) -> str:
        """
        Loads file from filepath

        param filepath: Filepath of the aliasses. (Optional: Will otherwise take system default)

        returns str: File data from the loaded file
        """
        try:
            paths = [filepath, f"{os.environ['HOME']}/.zshrc", f"{os.environ['USER_ZDOTDIR']}/.zshrc"]
        except KeyError:
            sys.exit("Couldn't load environmental variables.")

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

    def __edit_file(self, new_line: str, line_nr = None) -> None:
        """
        Edit a line in the filedata

        param line: Line to be edited
        param line_nr: Line number to be edited

        returns None
        """
        lines = self.filedata.split("\n")
        if line_nr and line_nr < len(lines):
            lines[line_nr] = new_line
        else:
            lines.append(new_line)
        self.filedata = "\n".join(lines)


    # PUBLIC METHODS
    def add(self, key: str, value: str) -> None:
        """
        Add an alias to the system aliases
        
        param key: Key for the alias
        param value: Command for the alias

        returns None
        """
        newline = f"alias {key}='{value}'"
        
        if line_number := self.__find_key(key):
            self.__edit_file(newline, line_number)
            print(f"Updating line: '{newline}'")
        else:
            self.__edit_file(newline)
            print(f"Adding line: '{newline}'")
            
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
    
    def __find_key(self, key: str) -> str:
        """
        Find an alias from the system aliases
        
        param key: Key of the alias

        returns str: The line of the alias
        """
        lines = self.filedata.split("\n")
        line_number = 0
        search_for = f"alias {key}="
        for line in lines:
            if line.find(search_for) >= 0:
                return line_number
            line_number += 1

    def show(self, key: str = "") -> None:
        """
        Show an alias of the system aliases
        
        param key: Key of the alias

        returns None
        """
        lines = self.filedata.split("\n")
        if key:
            if line_number := self.__find_key(key):
                print(f"Displaying line: '{lines[line_number]}'")
            else:
                print(f"Key '{key}' not found.")
        else:
            for line in lines:
                if line.find("alias ") >= 0:
                    print(line)


alias_manager = AliasManager()

alias_manager.remove("t")