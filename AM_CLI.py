from AliasManager import AliasManager
import argparse

def __main__():

    parser = argparse.ArgumentParser(
        prog = 'AliasManager',
        description = 'Manages aliasses for MacOS.'
    )
    subparsers = parser.add_subparsers(
        help='sub-command help',
        dest="action"
        )

    # SHOW command
    parser_show = subparsers.add_parser(
        name = 'show', 
        help='Shows a specific or all aliases.'
    )
    parser_show.add_argument(
        '--key',
        '-k', 
        type=str, 
        default="",
        help='Key of the alias to find.'
        )

    # ADD command
    parser_add = subparsers.add_parser(
        name = 'add', 
        help='Adds an alias.')
    parser_add.add_argument(
        'key',
        type=str, 
        help='Key of the alias to add.'
        )
    parser_add.add_argument(
        'value',
        type=str,
        nargs="+", 
        help='Command to add to the alias.'
        )


    # REMOVE command
    parser_remove = subparsers.add_parser(
        name = 'remove', 
        help='Removes an alias.')
    parser_remove.add_argument(
        'key', 
        type=str, 
        help='Key of the alias to remove.'
        )
    
    args = parser.parse_args()

    # Load AliasManager
    alias_manager = AliasManager()

    if args.action == 'show':
        alias_manager.show(args.key)

    elif args.action == 'add':
        alias_manager.add(args.key, str(" ".join(args.value)))

    elif args.action == 'remove':
        alias_manager.remove(args.key)

__main__()