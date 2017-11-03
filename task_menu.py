from abc import ABCMeta, abstractmethod

class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        pass
    
    
class Menu(object):
    def __init__(self, name, klass):
        self.commands = {}
        self.name = name
        self.klass = klass
        self.count = 0
    
    
    def add_command(self, name, klass):
        if not self.name:
            raise CommandException('Command must have a name!')

        if not issubclass(self.klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        
        self.commands[self.name] = self.klass


    def execute(self, name, *args, **kwargs):
        if not self.name:
            raise CommandException('Command with name "{}" not found'.format(name))
        return self.klass(*args, **kwargs).execute()   


    def __iter__(self):
       return self
       
    
    def __next__(self):
        if self.count < len(self.commands):
            i = len(self.commands) - self.count
            key = list(self.commands.keys())[i]
            self.count += 1
            return key, self.commands[key]
        
        raise StopIteration


class ShowCommand(Command):
    def execute(self):
        pass


class ListCommand(Command):
    def execute(self):
        pass
