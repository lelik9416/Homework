from abc import ABCMeta, abstractmethod
import os
import pickle
import json

"""
class ParamHandler (metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}
    
    
    def add_param(self, key, value):
        self.params[key] = value
    
    
    def get_all_params(self):
        return self.params

    
    @abstractmethod
    def read(self):
        pass

    
    @abstractmethod
    def write(self):
        pass


    @staticmethod
    def get_instance(source):
        _, ext = os.path.splitext(str(source).lower())
        if ext == '.xml':
            return XmlParamHandler(source)

        return TextParamHandler(source)
"""

class ParamHandlerException(Exception):
    pass


class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}
    
    
    def add_param(self, key, value):
        self.params[key] = value
    
    
    def get_all_params(self):
        return self.params

    
    @abstractmethod
    def read(self):
        pass
        
    
    @abstractmethod
    def write(self, data):
        pass


    @classmethod 
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))
        
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        
        return klass(source, *args, **kwargs)




class PickleParamHandler(ParamHandler):
    def read(self):
        """
        Чтение из pickle файла и присвоение значений в self.params
        """
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)
            return self.params        


    def write(self, data):
        """
        Запись в pickle файл параметров self.params
        """
        with open(self.source, 'wb') as f:
            self.params = pickle.dump(data, f)
            

        

class JsonParamHandler(ParamHandler):
    def read(self):
        """
        Чтение bp json и присвоение значений в self.params
        """
        with open(self.source) as f:
            self.params = json.load(f)
            return self.params


    def write(self, data):
        """
        Запись в json параметров self.params
        """
        with open(self.source, 'w') as f:
            self.params = json.dump(data, f, indent=4)
        

"""
pickle_pars = ParamHandler.add_type('pickle', PickleParamHandler)
json_pars   = ParamHandler.add_type('json', JsonParamHandler)

pickle_pars = ParamHandler.get_instance('users.pickle')
json_pars = ParamHandler.get_instance('users.json')
#print(pickle_pars.read())
json_pars.read()
print(json_pars.get_all_params())

data = {
    'ola': [
        {
            'id': 0,
            'name': 'Belial',
            'skills': ('Python')
        }
        ]
}
json_pars2 = ParamHandler.get_instance('ola.json')
print(json_pars2.read())


pickle_pars2 = ParamHandler.get_instance('ola.pickle')
#pickle_pars2 = pickle_pars2.write(data)
print(pickle_pars2.read())
"""
