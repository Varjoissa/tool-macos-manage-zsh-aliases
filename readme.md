# Alias Manager

*For MacOS*

This Alias Manager shows, adds and removes aliases from the `.zshrc` file. 

## Dependencies

This Alias Manager is dependent of the OhMyZsh framework. Please download and install through [HERE](https://ohmyz.sh/).

## How to use

Aliasmanager has three public methods that can be called:

Command | Params | Description | Example
---|---|---|---
add | key<br>value | Key of the alias to add.<br>Command for the alias | `python AM_CLI.py add name this is the command`
remove | key | Key of the alias to remove | `python AM_CLI.py remove name`
show | key (optional) | Alias to show. If not specified, all aliasses will be shown. | `python AM_CLI.py show`

After adding an alias, make sure to update the zsh environment by using the command `source ~/.zshrc`


## Recommendations

In order to make quick use of this alias manager, add the following aliasses:

**am** - Alias Manager
`python AM_CLI.py add am python AM_CLI.py`
--> am="python AM_CLI.py" - make sure to use the right pathing to the CLI script.

**amr** - Refresh Zsh
`python AM_CLI.py add amr source ~/.zshrc`
--> amr="source ~/.zshrc"
