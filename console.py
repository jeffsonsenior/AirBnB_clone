#!/usr/bin/python3
import cmd
from datetime import datetime
from typing import Any
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from model.state import State
from model.user import User
from models import Storage
from typing import Any

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = "(hbnb)"
    intro = "this is a ComandLine interpreter for AirBnB project"

    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review}
    __cli_kwargs = {}
        
        def do_quit(self, arg):
        """
        Exit the program
        """
        return True
    def do_EOF(self, arg):
        """
        Exit the program on EOF(Ctrl-D)
        """
        print()
        """
        Print a newline before exiting
        """
        return True
    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass
    def do_create(self, arg):
        """
        Create a new instance of entered class
        class name as argument then print id
        """
        if arg ==""
            print("** class name missing **")
        elif arg not in self.__classes.keys():
            print("class doesn't exist**"
        else:
            for k, v, in self.__classes.items():
                if arg == k:
                    print(v(self.__cli_kwargs).id)

def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return class_name, obj_id = args[0], args[1]
        try:
            module_name = class_name.lower()
            module = __import__(module_name)
            cls = getattr(module, class_name)
            instance = cls.get(obj_id)
            print(instance)
        except (AttributeError, ImportError, KeyError):
            print("** no instance found **")
    def do_destroy(self, arg):
        """
        Destroy an instance based on class name and id
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return class_name, obj_id = args[0], args[1]
        try:
            module_name = class_name.lower()
            module = __import__(module_name)
            cls = getattr(module, class_name)
            instance = cls.get(obj_id)
            instance.delete()
        except (AttributeError, ImportError, KeyError):
            print("** no instance found **")
    def do_all(self, arg):
        """
        print all string representations
        """
        if not arg:
            """
            print all instances
            """
            instances = storage.all()
        else:
            """
            print instances of the specified class
            """
            try:
                module_name = arg.lower()
                module = __import__(module_name)
                cls = getattr(module, arg)
                instances = storage.all(cls)
            except (AttributeError, ImportError):
                print("** class doesn't exist **")
                return
        print([str(instances) for instance in instances.values()])
    def do_update(self, arg):
        """
        update an instance attribute based on class name and id
        """
        args = arg.split()
        if len(args) < 4:
            print("** class name missing **")
            return class_name, obj_id, attr_name, attr_value = args[0],
            args[1], args[2], args[3]
        try:
            module_name = class_name.lower()
            module = __import__(module_name)
            cls = getattr(module, class_name)
            instance = cls.get(obj_id)
        if hasattr(instance, attr_name):
            instance.save()
        else:
            print("** attribute name missing **")
        except (AttributeError, ImportError, KeyError):
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

