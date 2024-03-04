#!/usr/bin/env python3
"""
This is the console module for the AirBnB project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Called when an empty line is entered.
        """

        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """

        return True

    def do_EOF(self, arg):
        """
        Handle the EOF (Ctrl-D) to exit the program.
        """

        print()
        return True

    def help_quit(self):
        """
        Help documentation for quit command.
        """

        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help documentation for EOF command.
        """

        print("Handle the EOF (Ctrl-D) to exit the program.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()