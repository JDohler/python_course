# Person class
#-------------------------------------------------------------------


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def print_Person(self):
        print(self.firstname + ' ' + self.lastname)

#name = Person("Jessica", "Dohler")
#name.print_Person()


# Student class
#-------------------------------------------------------------------


class Student(Person):
    def __init__(self, firstname, lastname, area):
        super().__init__(firstname, lastname)
        self.area = area
        
    def print_NameSubject(self):
        print(self.firstname + ' ' + self.lastname + ', ' + self.area)
        
 
#name_st = Student("Lorena", "Camelo", "chemistry")
#name_st.print_NameSubject()        
 
# Teacher class
#-------------------------------------------------------------------  

      
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course
        
    def print_TeacherCourse(self):
        print(self.firstname + ' ' + self.lastname + ', ' + self.course)
        
#name_te = Teacher("Filipe", "Maia", "python 2022")
#name_te.print_TeacherCourse()