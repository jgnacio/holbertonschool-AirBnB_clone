#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:34:00 2023.

@authors: jgnacio
@description:
    (class) - HBNBCommand:
        Comand interpreter class.

        InstaceAttributes:
            prompt: The identifier of the model.

        (method) - do_quit():
            Quit command to exit the program.

        (method) - do_EOF():
            EOF command to exit the program.

        (method) - emptyline():
            if the read line is empty execute
            this method, that do nothing.

        (method) - do_create(arg):
            create command to make a new obj.

        (method) - do_show(arg):
            Print the content of the given instance.
            Example usage:
            (hbnb) show <class name> <id>.

        (method) - destroy(arg):
            Destroy the instance with given id.

            Example usage:
            (hbnb) destroy <class name> <id>.
        (method) - all(arg):
            Print all instances content.

            Example usage:
            (hbnb) all
            (hbnb) all <class name>
            #print all instances with the given class name.
        (method) - update(arg):
            Update attributes of the given model.

            Example usage:
        (hbnb) update <class name> <id> <attribute name> "<attribute value>".
"""

import cmd
from models import storage
from models.engine import classes
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

error_logs = {
    "CLASS_NAME_MISSING": "** class name missing **",
    "CLASS_NOT_FOUND": "** class doesn't exist **",
    "INSTANCE_ID_MISSING": "** instance id missing **",
    "INSTANCE_NOT_FOUND": "** no instance found **",
    "ATTRIBUTE_NAME_MISSING": "** attribute name missing **",
    "VALUE_MISSING": "** value missing **"
}


class HBNBCommand(cmd.Cmd):
    """Command class for interactive to objs."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program whit Ctrl + d."""
        return True

    # Set do_exit to the command quit
    do_exit = do_quit

    def emptyline(self):
        """Command for empty line."""

    def do_create(self, arg):
        """
        Create a new instance of the object.

        Example usage:
        (hbnb) create <class name>
        """
        if len(arg) == 0:
            print(error_logs["CLASS_NAME_MISSING"])
        elif arg not in classes:
            print(error_logs["CLASS_NOT_FOUND"])
        else:
            new_obj = eval(arg)()
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        """
        Print the content of the given instance.

        Example usage:
        (hbnb) show <class name> <id>
        """
        if len(arg) == 0:
            print(error_logs["CLASS_NAME_MISSING"])
        if len(arg.split()) > 0:
            if arg.split()[0] not in classes:
                print(error_logs["CLASS_NOT_FOUND"])
            elif len(arg.split()) < 2:
                print(error_logs["INSTANCE_ID_MISSING"])
            else:
                try:
                    print(storage.all()[f"{arg.split()[0]}.{arg.split()[1]}"])
                except KeyError:
                    print(error_logs["INSTANCE_NOT_FOUND"])

    def do_destroy(self, arg):
        """
        Destroy the instance with given id.

        Example usage:
        (hbnb) destroy <class name> <id>
        """
        if len(arg) == 0:
            print(error_logs["CLASS_NAME_MISSING"])
        if len(arg.split()) > 0:
            if arg.split()[0] not in classes:
                print(error_logs["CLASS_NOT_FOUND"])
            elif len(arg.split()) < 2:
                print(error_logs["INSTANCE_ID_MISSING"])
            else:
                try:
                    storage.all().pop(f"{arg.split()[0]}.{arg.split()[1]}")
                    storage.save()
                except KeyError:
                    print(error_logs["INSTANCE_NOT_FOUND"])

    def do_all(self, arg):
        """
        Print all instances content.

        Example usage:
        (hbnb) all
        (hbnb) all <class name>
        #print all instances with the given class name
        """
        list_obj = []
        if len(arg) == 0:
            for model in storage.all().values():
                list_obj.append(str(model))
            print(list_obj)
        else:
            if arg.strip() in classes:
                for name, model in storage.all().items():
                    if name.split('.')[0] == arg.strip():
                        list_obj.append(str(model))
            else:
                print(error_logs["CLASS_NOT_FOUND"])
                return
            print(list_obj)

    def do_update(self, arg):
        """
        Update attributes of the given model.

        Example usage:
        (hbnb) update <class name> <id> <attribute name> "<attribute value>"
        """
        if len(arg) == 0:
            print(error_logs["CLASS_NAME_MISSING"])
        if len(arg.split()) > 0:
            if arg.split()[0] not in classes:
                print(error_logs["CLASS_NOT_FOUND"])
                return
            if len(arg.split()) > 1:
                try:
                    storage.all()[f"{arg.split()[0]}.{arg.split()[1]}"]
                except KeyError:
                    print(error_logs["INSTANCE_NOT_FOUND"])
                    return
            if len(arg.split()) < 2:
                print(error_logs["INSTANCE_ID_MISSING"])
                return
            if len(arg.split()) < 3:
                print(error_logs["ATTRIBUTE_NAME_MISSING"])
                return
            if len(arg.split()) < 4:
                print(error_logs["VALUE_MISSING"])
                return
            else:
                try:
                    storage.all()[
                        f"{arg.split()[0]}.{arg.split()[1]}"].__dict__[
                            arg.split()[2]
                    ] = arg.split()[3].strip('"')
                except KeyError:
                    print(error_logs["INSTANCE_NOT_FOUND"])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
