from abc import ABCMeta, abstractmethod

class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        pass
    
    
class Menu(object):
    def __init__(self):
        self.commands = {}
        self.count = 0
    
    
    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        
        self.commands[name] = klass


    def execute(self, name, *args, **kwargs):
        klass = self.commands.get(name)
        
        if not name:
            raise CommandException('Command with name "{}" not found'.format(name))
            
        return klass(*args, **kwargs).execute()   


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
    def __init__(self, task_id):
        self.task_id = task_id
    
    def execute(self):
        return 'execute show task {}'.format(self.task_id) 


class ListCommand(Command):
    def execute(self):
        pass


menu = Menu()
menu.add_command('show', ShowCommand)
#menu.add_command('list', ListCommand)

menu.execute('show', 1)

print(menu)
