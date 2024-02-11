import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")  # Print a new line for a better display
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
