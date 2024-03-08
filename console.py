#!/usr/bin/python3
"""AirBnB clone (hbnb) console definition"""
import cmd


class HBnBCommand(cmd.Cmd):
    """console class inheriting from cmd module

    Args:
        cmd (class): cmd module method class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """function to quit the console

        Args:
            arg (_type_): object argument

        Returns:
            bool : True to quit 
        """
        return True

HBnBCommand().cmdloop()
