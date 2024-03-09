#!/usr/bin/python3
"""AirBnB clone (hbnb) console definition"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """takes a string arg as an argument and
    parses it based on certain patterns

    Args:
        arg : argument

    Returns:
        string: parsed strings
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(brackets.group())
        return retl

class HBnBCommand(cmd.Cmd):
    """console class inheriting from cmd module

    Args:
        cmd (class): cmd module method class
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel"
        "User"
        "State"
        "City"
        "Place"
        "Amenity"
        "Review"
    }

    def emptyline(self):
        """Nothing is done when an empty line is inputed"""
        pass

    def default(self, arg):
        """Cmd module default behaviour upon invalid input"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span90[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quits the console program

        Args:
            arg : object argument
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the console

        Args:
            arg : object argument
        """
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new class instance and prints its id."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBnBCommand.__classes:
            print("** class doesn't exist ***")
        else:
            print(eval(argl[0])().id)
            storage.save()

if __name__ == '__main__':
    HBnBCommand().cmdloop()
