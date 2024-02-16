#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


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

    def do_create(self, arg):
        """Create a new instance of BaseModel or User,\
        save it, and print its id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of\
        an instance (BaseModel or User)."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if class_name == key.split('.')[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
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

        obj = storage.all()[key]

        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            setattr(obj, attribute_name, attr_type(attribute_value))
            obj.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
