class Person:

    def __init__(self,name:str, surname:str, id:str):
        self.__name = name
        self.__surname = surname
        self.__id = id

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_id(self, id):
        self.__id = id


class Pupil(Person):

    def __init__(self,name:str, surname:str, id:str, license:str, mail=str, year=int, mark=float):
        super().__init__(name, surname, id)
        self.__name = name
        self.__surname = surname
        self.__id = id
        self.__license = license
        self.__mail = mail
        self.__year = year
        self.__mark = mark

   
    def __str__(self):
        return f'Alumno: {self.__name} {self.__surname}, ID: {self.__id}, Matricula: {self.__license}, Mail: {self.__mail}, Año: {self.__year}, Nota Promedio: {self.__mark}'


    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_id(self):
        return self.__id

    def get_license(self):
        return self.__license
    
    def get_mail(self):
        return self.__mail

    def get_year(self):
        return self.__year
    
    def get_mark(self):
        return self.__mark


    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_id(self, id):
        self.__id = id
    
    def set_license(self, license):
        self.__license = license

    def set_mail(self, mail):
        self.__mail = mail

    def set_year(self, year):
        self.__year = year

    def set_mark(self, mark):
        self.__mark = mark


class Class():
    
    def __init__(self, name):
        self.__name = name
        self.__pupils = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self):
        return self.__name

    @property
    def pupils(self):
        return self.__pupils
           
    def add(self, pupil):
        self.__pupils.append(pupil)


def main():

    pupils = []
    subject = Class("Diseño de Sistemas")

    lucas = Pupil("Lucas", "Galdame", "0123456789", "59114", "luqui@mail.com", 4, 7.5)
    danilo = Pupil("Danilo", "Cerna", "1234567890", "59110", "danilo@mail.com", 3, 7.0)
    santiago = Pupil("Santiago", "Moyano", "2345678901", "59116", "santiago@mail.com", 4, 7.2)
    bruno = Pupil("Bruno", "Romero", "3456789012", "59112", "bruno@mail.com", 4, 7.4)
    aaron = Pupil("Aaron", "Moyano", "4567890123", "59118", "aaron@mail.com", 3, 8.5)
    delfina = Pupil("Delfina" , "Quinteros", "5678901234", "59115", "delfina@mail.com", 5, 9.0)
    daniel = Pupil("Daniel" , "Beato", "6789012345", "59111", "daniel@mail.com", 5, 8.8)

    subject.add(lucas)
    subject.add(danilo)
    subject.add(santiago)
    subject.add(bruno)
    subject.add(aaron)

    for pupil in subject.pupils:
        print(pupil)
        
if __name__ == "__main__":
    main()