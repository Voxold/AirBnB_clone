#!/usr/bin/env python3
"""
This is the console module for the AirBnB project.
"""

import cmd
import models


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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """

        args = arg.split()
        if not args or args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        instances = [str(inst) for inst in models.storage.all().values()
                     if type(inst).__name__ == args[0]]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating
        attribute (save the change into the JSON file).
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = models.storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
