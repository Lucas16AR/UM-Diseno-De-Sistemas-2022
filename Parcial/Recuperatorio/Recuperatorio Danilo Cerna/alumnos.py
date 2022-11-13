"""
1. Crear una clase Persona con atributos como: nombre, apellido, dni y por otro lado una
clase Alumno que extiende de Persona con los siguientes atributos: matricula, email,
Año de Cursado, promedio de nota.
Programar:
▪ Que se puede añadir los alumnos a una lista.
▪ Que una vez finalizada la carga de alumnos:
• Se pueda obtener el total de alumnos por año cursado y promedio total de
notas por año.
• Que devuelva el alumno con mejor promedio de nota por año cursado.
"""

class Persona:
    def __init__(self, nombre, apellido, dni, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__email = email


class Alumno(Persona):

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def año_cursado(self):
        return self.__año_cursado

    @año_cursado.setter
    def año_cursado(self, año_cursado):
        self.__año_cursado = año_cursado

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio

    def get_nombre(self): 
        return self._Persona__nombre
    
    def get_apellido(self):
        return self._Persona__apellido

    def get_dni(self):
        return self._Persona__dni
    
    def set_dni(self, dni): 
        self._Persona__dni = dni
    
    def set_nombre(self, nombre):
        self._Persona__nombre = nombre
    
    def set_apellido(self, apellido):
        self._Persona__apellido = apellido
    
    

    def __init__(self, nombre, apellido, dni, matricula, email, año_cursado, promedio):
        super().__init__(nombre, apellido, dni, email)
        self.matricula = matricula
        self.email = email
        self.año_cursado = año_cursado
        self.promedio = promedio
    
    def __str__(self):
        return f"Nombre: {self.get_nombre()}, Apellido: {self.get_apellido()}, DNI: {self.get_dni()}, Matricula: {self.matricula}, Email: {self.email}, Año Cursado: {self.año_cursado}, Promedio: {self.promedio}"

def main(): 
    alumnos = []
    alumnos.append(Alumno("Juan", "Perez", 12345678, 1234, "  Juan@mail.com ", 1, 8))
    alumnos.append(Alumno("Pedro", "Gomez", 87654321, 5678, "  Pedro@mail.com ", 2, 9))
    alumnos.append(Alumno("Maria", "Lopez", 13579246, 9101, " Maria@mail.com  ", 3, 10))
    alumnos.append(Alumno("Jose", "Martinez", 24681012, 1112, "  Jose@mail.com ", 4, 7))
    alumnos.append(Alumno("Ana", "Gonzalez", 31415926, 1314, "  Ana@mail.com ", 5, 6))
    alumnos.append(Alumno("Lucas", "Rodriguez", 27182818, 1516, "  Lucas@mail.com ", 6, 5))
    alumnos.append(Alumno("Sofia", "Fernandez", 14142135, 1718, "  Sofia@mail.com ", 7, 4))
    alumnos.append(Alumno("Miguel", "Alvarez", 16180339, 1920, "  Miguel@mail.com ", 8, 3))
    alumnos.append(Alumno("Julieta", "Sanchez", 11235813, 2122, "  Julieta@mail.com ", 9, 2))

    for alumno in alumnos:
        print(alumno)
    
    print("Total de alumnos por año cursado y promedio total de notas por año")
    for i in range(1, 10): 
        total_alumnos = 0
        promedio_total = 0
        for alumno in alumnos:
            if alumno.año_cursado == i:
                total_alumnos += 1
                promedio_total += alumno.promedio
        print(f"Año: {i}, Total de alumnos: {total_alumnos}, Promedio total: {promedio_total/total_alumnos}")

    print("Alumno con mejor promedio de nota por año cursado")

    for i in range(1, 10): 
        mejor_promedio = 0
        for alumno in alumnos:
            if alumno.año_cursado == i:
                if alumno.promedio > mejor_promedio:
                    mejor_promedio = alumno.promedio
                    mejor_alumno = alumno
        print(f"Año: {i}, Mejor promedio: {mejor_promedio}, Alumno: {mejor_alumno.get_nombre()} {mejor_alumno.get_apellido()}")

if __name__ == "__main__":
    main()


   
   

