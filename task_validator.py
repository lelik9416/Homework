from abc import ABCMeta, abstractmethod
import os
import datetime

class ValidatorException(Exception):
    pass


class Validator(metaclass=ABCMeta):
    types = {}
    
    @abstractmethod
    def validate(self):
        pass
        
    @classmethod    
    def get_types(cls):
        return cls.types
    
    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')
        
        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))
        
        cls.types[name] = klass 
    
    @classmethod
    def get_instance(cls, name):
        
        klass = cls.types.get(name)
        
        if klass is None:
            raise ValidatorException('ValidatorError: Validator with name "{}" not found'.format(name))
        
        return klass()
        



class EMailValidator(Validator):
    def validate(self, value):
        #проверка на наличие @ в email
        if '@' not in value:
            return False
        #проверка на наличие . в email
        if '.' not in value:
            return False
        
        sig1 = value.find('@')
        #проверка на вхождение второй @
        if value.rfind('@') != sig1:
                return False
            
        sig2 = value[::-1].find('.')
        sig3 = abs(sig1 - value.find('.') + 1)

        if sig1 != 0 and sig2 != 0 and sig3 != 0:
            return True
        
        return False
"""
            --------------     
        ext = value.split('@')
        ext1 = ext[1].split('.')
        if len(ext[0]) !=0 and len(ext1[0]) !=0 and len(ext1[1]) !=0:
            return True
"""     
           
        
        
class DateTimeValidator(Validator):
    def validate(self, value):
        #row = value.split()
        date_format = ['%Y-%m-%d %H:%M:%S',
                       '%Y-%m-%d %H:%M',
                       '%Y-%m-%d', 
                       '%Y-%m-%j %H:%M:%S', 
                       '%Y-%m-%j %H:%M',
                       '%Y-%m-%j', 
                       '%Y-%n-%j %H:%M:%S',
                       '%Y-%n-%j %H:%M',
                       '%Y-%n-%j', 
                       '%j.%n.%Y %H:%M:%S', 
                       '%j.%n.%Y %H:%M',
                       '%j.%n.%Y',
                       '%j.%m.%Y %H:%M:%S',
                       '%j.%m.%Y %H:%M',
                       '%j.%m.%Y', 
                       '%d.%m.%Y %H:%M:%S',
                       '%d.%m.%Y %H:%M',
                       '%d.%m.%Y', 
                       '%j/%n/%Y %H:%M:%S',
                       '%j/%n/%Y %H:%M',
                       '%j/%n/%Y', 
                       '%j/%m/%Y %H:%M:%S', 
                       '%j/%m/%Y %H:%M',
                       '%j/%m/%Y', 
                       '%d/%m/%Y %H:%M:%S',
                       '%d/%m/%Y %H:%M',
                       '%d/%m/%Y'
                       ]
        
        for form in date_format:
            try:
                datetime.datetime.strptime(value, form)
                return True
            except:
                continue  
                
        return False
        
        
        




Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)

validator = Validator.get_instance('email')
validator1 = Validator.get_instance('datetime')

