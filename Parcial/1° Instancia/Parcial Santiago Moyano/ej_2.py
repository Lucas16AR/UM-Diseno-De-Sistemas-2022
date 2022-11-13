"""
La universidad necesita el desarrollo de una aplicación para administrar talleres de
capacitación según los siguientes requerimientos:
Individuo, Estudiantes y Profesores
Individuo:
Cada individuo tiene dni, nombre y apellido.
Cada individuo debe poder informar sus datos personales.
Cada individuo es un estudiante o profesor:
Cada profesor tiene un CV.
Cada profesor también tiene un conjunto de habilidades o skill ["Python", "Java",
"Golang", "TypeScript"].
Un profesor puede agregar una nueva habilidad.
"""
class Individuo():

    def __init__(self, nombre:str, apellido:str, dni:str):

        self.__nombre = nombre

        self.__apellido = apellido

        self.__dni = dni
    
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_dni(self, dni):
        self.__dni = dni

class Alumno(Individuo):

    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

        self.__nombre = nombre

        self.__apellido = apellido

        self.__dni = dni

class Profesor(Individuo):
    def __init__(self, nombre: str, apellido: str, dni: str, cv: str):
        super().__init__(nombre, apellido, dni)

        self.__nombre = nombre

        self.__apellido = apellido

        self.__dni = dni

        self.__habilidades = []

        self.__cv = cv
    
    def __repr__(self):
        return super().get_nombre() + ', ' + super().get_apellido() 
   
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    def get_cv(self):
        return self.__cv
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_dni(self, dni):
        self.__dni = dni

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_dni(self, dni):
        self.__dni = dni
    
    def set_cv(self, cv):
        self.__cv = cv

    
    def agregar_habilidad(self, habilidad):
        self.__habilidades.append(habilidad)

class Taller():
    def __init__(self, fecha, tema):
        self.__fecha = fecha
        self.__tema = tema
        self.__profesores = []
        self.__alumnos = []
    
    @property
    def fecha(self, valor):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor
    @property
    def tema(self, valor):
        return self.__tema

    @tema.setter
    def tema(self, valor):
        self.__tema = valor

    @property
    def profesores(self):
        return self.__profesores

    @property
    def alumnos(self):
        return self.__alumnos
           
    def agregar_alumnos(self, alumno):
        self.__alumnos.append(alumno)
        

    def agregar_profesores(self, profesor):
        self.__profesores.append(profesor)
    

    
def main():
    taller = Taller("12-04-2022", "Charla orientativa")

    lucas = Alumno("Lucas", "Galdame", "234567896")
    danilo = Alumno("danilo", "Verardo", "231222323")
    bruno = Alumno("bruno", "Romero", "323123213")

    taller.agregar_alumnos(lucas)

    taller.agregar_alumnos(danilo)

    taller.agregar_alumnos(bruno)
    
    for alumno in taller.alumnos:
        print(alumno)

    ruben = Profesor("ruben", "gallart", "123", "cv")
    gabriel = Profesor("gabriel", "arenas", "1234", "cv")
    jose = Profesor("jose", "artal", "12345", "cv")
    taller.agregar_profesores(ruben)
    taller.agregar_profesores(gabriel)
    taller.agregar_profesores(jose)
    jose.agregar_habilidad('Rust')
    for profesor in taller.profesores:
        print(profesor)

if __name__ == "__main__":
    main()