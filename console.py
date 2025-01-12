#!/usr/bin/python3
import cmd

"""
This module contains the HBNBCommand class, which is a command interpreter
for the HBNB project. It provides a command-line interface to interact with
the application.

Classes:
    HBNBCommand: A command interpreter class that inherits from cmd.Cmd.

Methods:
    do_quit(self, arg): Quit command to exit the program.
    do_EOF(self, arg): EOF command to exit the program.
    emptyline(self): Do nothing on empty input line.
"""


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
