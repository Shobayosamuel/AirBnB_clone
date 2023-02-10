#!/usr/bin/python3
"""
Module that contains entry point of the cmd interpreter
"""
from models.base_model import BaseModel
import cmd
import models
from shlex import split
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class for the command interpreter
"""
    prompt = "(hbnb) "
    classes = {
            'BaseModel': BaseModel()
            }

    def do_quit(self, line):
        """
        exit the program
        """
        return True

    def do_EOF(self, line):
        """
        End of the file character
        """
        return True

    def do_create(self, line):
        """
        Create a new instance of BaseModel
        Usage: create <class>
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.classes[args[0]]
            new.save()
            print(new.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs.keys():
                print("** no instance found **")
            else:
                print(str(all_objs[key]))

    def do_destroy(self, line):
        """
        Usage: destroy <class> <id>
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs.keys():
                print("** no instance found **")
            else:
                del all_objs[key]

    def do_all(self, line):
        """
        Usage: all <optional class>
        Prints all string representation of all instances
        based or not on the class name
        """
        args = line.split()
        result = []
        if len(args) == 0:
            for vals in models.storage.all().values():
                result.append(str(vals))
            print(result)
        else:
            if line not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for k, v in models.storage.all().items():
                    if line in k:
                        result.append(str(v))
            print(result)

    def do_update(self, line):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) > 0:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(args[0], args[1])
                if instance_id in self.storage.all():
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if args[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[args[2]])
                            setattr(obj, args[2], v_type(args[3]))
                        else:
                            setattr(obj, args[2], args[3])
                else:
                    print("** no instance found **")
            self.storage.save()
    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
