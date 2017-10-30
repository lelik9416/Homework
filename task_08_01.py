"""
Задача №1
Попробуйте перенести в ОО-код следующий пример из реального мира:
- есть курсы, учителя и ученики
- у каждого курса есть свой учитель
- у каждого учителя есть своя группа учеников
- у каждого ученика есть свой учитель
и т.д.

Определите какие объекты есть в этом примере, какие у них свойства и какие методы, 
как эти объекты будут между собой взаимодействовать, например, к курсу можно добавить учителя.

Создайте все необходимые классы и приведите пример их использования.

Вопросы по ДЗ пишите в наш общий чат. Я не против, если решение будет коллективное.
"""

class Course(object):
    def __init__(self, name='New', duration=0):
        self.course = self.add_course(name)
        self.duration = self.add_duration(duration)


    def add_course(self, name):
        self.name = name
    
    
    def add_duration(self, duration):
        self.duration = duration
    
    def get_course(self):
        return self.course
    
        
    def print_info_course(self):
        print('Курс "{}". Продолжительность курса  {} часов.'.format(self.name, self.duration)



class Teacher(object):
    def __init__(self, firstname_t, lastname_t, skills=None, age_t=None, course=None):
        self.firstname_t = firstname_t
        self.lastname_t  = lastname_t
        self.skills      = set_skills(skills)
        self.age_t       = set_age_t(age_t)
        self.course      = get_course()
        self.student     = {}
        
                
         
    def get_teacher(self):
        return '{} {} ({} years old). Skills - {}. Course - {}'.format(self.firstname_t, 
                                                                       self.lastname_t, 
                                                                       sel.age_t, 
                                                                       self.skills, 
                                                                       self.course)
    
    
    def set_teacher(self, firstname, lastname):
        self.firstname_t = firstname_t
        self.lastname_t  = lastname_t
        
    
    def set_student(self, studentN, firstname, lastname, age, teacher):
        student = {}
        student[studentN] = [firstname, lastname, age, teacher]
        self.student = student
        
        
    def set_age_t(self, age_t):
        self.age_t = age_t
        
        
    def set_skills(self, skills):
        self.skills = skills
        
        

