
class TagException(Exception):
    pass


class Tag(object):
    __slots__ = ('name', 'atribute')
    
    def __init__(self, name):
        self.__name = str(name)
        self.__atribute = {}
    
    
    @property
    def parent(self):
        return self.parent
    
    
    @parent.setter
    def parent(self, parent):
        self.parent = parent
    
    
    @parent.deleter
    def parent(self):
        del self.parent
        
    
    @property
    def previous_sibling(self):
        return self.previous_sibling
    
    
    @previous_sibling.setter
    def previous_sibling(self, previous_sibling):
        self.previous_sibling = previous_sibling
    
    
    @previous_sibling.deleter
    def previous_sibling(self):
        del self.previous_sibling
    
            
    @property
    def next_sibling(self):
        return self.next_sibling
    
    
    @next_sibling.setter
    def next_sibling(self, next_sibling):
        self.next_sibling = next_sibling
    
    
    @next_sibling.deleter
    def next_sibling(self):
        del self.next_sibling
    
        
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
    
    
    def __setattr__(self, attr):
        try:
            return super().__setattr__(attr)
        except AttributeError:
            return self.__attribute.get(attr)
    
    
    def __delattr__(self, attr):
        try:
            return super().__delattr__(attr)
        except AttributeError:
            return self.__attribute.get(attr)
    
    
    def __str__(self):
        return '<img src="{}" alt="{}">'.format(src, alt)
    
    
    
class ContainerTag(Tag):
    pass
