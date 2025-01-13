#!/usr/bin/env python3
"""Command Interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Classes"""
    prompt = "(hbnb) "

    classes = [
        'BaseModel',
    ]

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True


    
if __name__ == '__main__':
    HBNBCommand().cmdloop()