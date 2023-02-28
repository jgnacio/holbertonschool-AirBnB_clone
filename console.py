#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:34:00 2023.

@authors: jgnacio & Mauro Trenche
@description:
    (class) - HBNBCommand:
        Comand interpreter class.

        InstaceAttributes:
            prompt: The identifier of the model.

        (method) - do_quit():
            Quit command to exit the program.

        (method) - do_EOF():
            EOF command to exit the program.

        (method) - do_create():
            create command to make a new obj.

        (method) - emptyline():
            if the read line is empty execute
            this method, that do nothing.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command class for interactive to objs."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program whit Ctrl + d."""
        return True

    def emptyline(self):
        """Command for empty line."""
        pass

    def do_create(self, arg):
        """Make instance of base model."""
        import json

        if len(arg) == 0:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
