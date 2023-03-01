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

    def do_create(self, args):
        """new instance of base model"""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in storage.class_list():
            print("** class doesn't exist **")
        else:
            X = eval(args)()
            x.save()
            print(x.id)

    def do_show(self , args):
        """print string representation"""
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif (argv[0] not in storage.class_list()):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            m = args[0] + "." + args[1]
            dic = storage.all()
            try:
                print(dic[m])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif tokens[1] is None:
            print("** instance id missing **")
        else:
            m = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                storage.delete(m)
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, args).
        tokens = models.storage.all()
        if len(args):
            if globals().get(args) is None:
                print("** class doesn't exist **")
                return
        tokens = []
        for key, value in tokens.items():
            if value.__class__.__name__ == args or len(args) == 0:
                tokens.append(value.__str__())
        print(tokens)

    def do_update(self, args):
        """Updates an instance based on the class name"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            f = tokens[0] + "." + tokens[1]
            try:
                value = dic[f]
            except Exception:
                print("** no instance found **")
            if len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                tokens[3].replace('"', "")
                setattr(dic[f], tokens[2], tokens[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
