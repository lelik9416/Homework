
class TagException(Exception):
    pass


class Tag(object):
    __slots__ = ('__name', '__attribute', '_parent', '_previous_sibling', '_next_sibling', '_first_child', '_last_child', '_children')
    
    def __init__(self, name):
        self.__name = name
        self.__attribute = {}
        self.__parent = None
        self.__previous_sibling = None
        self.__next_sibling = None
    
    @property
    def parent(self):
        return self._parent
    
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent
    
    
    @parent.deleter
    def parent(self):
        del self._parent
        
    
    @property
    def previous_sibling(self):
        return self._previous_sibling
    
    
    @previous_sibling.setter
    def previous_sibling(self, previous_sibling):
        self._previous_sibling = previous_sibling
    
    
    @previous_sibling.deleter
    def previous_sibling(self):
        del self._previous_sibling
    
            
    @property
    def next_sibling(self):
        return self._next_sibling
    
    
    @next_sibling.setter
    def next_sibling(self, next_sibling):
        self._next_sibling = next_sibling
    
    
    @next_sibling.deleter
    def next_sibling(self):
        del self._next_sibling
    
        
    @property
    def first_child(self):
        raise TryExcept('Not a container tag!')         
    
    
    @property
    def last_child(self):
        raise TryExcept('Not a container tag!')
        
    
    @property
    def children(self):
        raise TryExcept('Not a container tag!')
        
    
    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return self.__attribute.get(attr)
    
    
    def __setattr__(self, value, attr):
        try:
            return super().__setattr__(value, attr)
        except AttributeError:
            self.__attribute[value] = attr
    
    
    def __delattr__(self, attr):
        try:
            return super().__delattr__(attr)
        except AttributeError:
            self.__attribute[attr] = None
            
    
    def __str__(self):
        itog = '<' + self.__name 
        for key,value in self.__attribute.items():
            itog += ' ' + key + '="' + value + '"'
        itog += '>'
        return itog
    
    
    
class ContainerTag(Tag):
    __slots__ = ()

    def __init__(self, name, attribute=None):
        super().__init__(name, attribute)
        self.__first_child = None
        self.__last_child = None

    @property
    def first_child(self, tag):
        return self._first_child         
    
    
    @property
    def last_child(self):
        return self._last_child
        
    
    @property
    def children(self):
        a = self._first_child
        while a:
            yield a
            a = a._next_sibling
        

    def append_child(self, tag):
        pass
    
    
    def insert_before(self, tag, next_sibling):
        pass
    
    







img = Tag('img')
img.src = '/python-developer.svg'
img.alt = 'Python Разработчик'

print(img)

