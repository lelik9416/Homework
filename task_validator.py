from abc import ABCMeta, abstractmethod
import os


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
    
    @staticmethod
    def add_type(name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')
        
        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))
        
        types[name] = klass 
    
    @classmethod
    def get_instance(cls, name):
        
        klass = cls.types.get(name)
        
        if klass is None:
            raise ValidatorException('ValidatorError: Validator with name "{}" not found'.format(name))
        
        return klass(name)
        



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
        return 'hi'


#print(Validator.get_instance('info@itmo-it.org'))

Validator.add_type('email', EMailValidator)
validator = Validator.get_instance('email')
#validator = Validator.get_instance('datetime')
print(validator.validate('info@itmo.org'))

"""
name = '@itmo-it.'
sig1 = name.find('@')
sig2 = name[::-1].find('.')


if sig1 != 0 and sig2 != 0:
    print(True)
    
print(sig1)
print(sig2)


ext = name.split('@')
ext1 = ext[1].split('.')
for i in ext:
    a = len(i)

if len(ext) !=0 and ext1[0] !=0 and ext1[1] !=0:
   print('True')

if a !=0:
   print('True')



_, ext = os.path.splitext(str(name).lower())
        #ext = name.split('@')
        #ext2 = name.split('.')
        #ext = name.find('@')
"""
