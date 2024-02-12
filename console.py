#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # New line for aesthetics
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
