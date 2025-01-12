#!/usr/bin/python3

'''
Creation of the Console 001

'''


import cmd


class HBNBCommand(cmd.Cmd):
    '''Console class'''
    prompt='(hbnb) '

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_help (self, arg):
        '''Help command to show the help'''
        return super().do_help(arg)

    def do_EOF(self):
        '''EOF command to exit the program'''
        return True

    def emptyline(self):
        pass

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()