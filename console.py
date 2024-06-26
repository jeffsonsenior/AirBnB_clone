#!/usr/bin/python3
"""Defines HBnB console."""
import cmd
import re
from shlex import split
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from model.state import State
from model.user import User
from models import Storage

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",")for i in split(arg)]
        else:
            laxer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
        
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        return retl
          


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving empty line"""
        pass

    def default(self, arg):
        """ default behaviour for cdm when imput is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("**Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True
    def do_EOF(self, arg):
        """
        Exit the program on EOF(Ctrl-D)
        """
        print("")
        """
        Print a newline before exiting
        """
        return True
    
    def do_create(self, arg):
        """
        Create a new instance of entered class
        class name as argument then print id
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class doesnt exist**")
        elif argl[0] not in HBNBCommand.__classes:
            print("class doesn't exist**")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
                print("**class doesn't exist**")
        elif len(argl) == 1:
            print("**instance id missing**")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("**no instances found**")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Destroy an instance based on class name and id
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exit **")
        elif len(argl) == 1:
            print("** instance id missing**")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()
        
    def do_all(self, arg):
        """
        display strings representation of all instances of a given class
        if no class specified then display all instatiated obl
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(obj1)

    def do_count(self, args):
        """ Retrive number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().value():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)    


    def do_update(self, arg):
        """
        update an instance attribute based on class name and id
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) ==0:
            print("** class name missing **")
            return False
        if argl[0] not in  HBNBCommand.__classes:
            print("** class doen't exit **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found**")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NmeError:
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
           
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and 
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
            storage.save()

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
