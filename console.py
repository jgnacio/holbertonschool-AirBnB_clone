#!/usr/bin/python3
"""interpreter"""


import json

def do_create(self, arg):
    """new instance of base model"""
    if len(arg) == 0:
        print("** class name missing **")
    else:
        
