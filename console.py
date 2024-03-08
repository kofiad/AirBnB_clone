#!/usr/bin/python3
"""AirBnB clone (hbnb) console definition"""
import cmd


class HBnBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

HBnBCommand().cmdloop()
