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
        """Quits the console program

        Args:
            arg (_type_): object argument

        Returns:
            bool : True to quit
        """
        return True

    def do_EOF(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        print("")
        return True

if __name__ == '__main__':
    HBnBCommand().cmdloop()
