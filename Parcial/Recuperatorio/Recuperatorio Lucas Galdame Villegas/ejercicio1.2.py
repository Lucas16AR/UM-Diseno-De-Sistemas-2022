
# create a class Persona with atributes nombre, apellido, dni
class Persona:

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.dni

# create a class Alumno that inherits from Persona with atriutes nombre, apellido, dni, matricula, email, curso, promedio
class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, matricula, email, curso, promedio):
        super().__init__(nombre, apellido, dni)
        self.matricula = matricula
        self.email = email
        self.curso = curso
        self.promedio = promedio

    def __str__(self):
        return super().__str__() + " " + self.matricula + " " + self.email + " " + self.curso + " " + self.promedio

class Lista:

    alumnos: list[object] = []

    @staticmethod
    def agregar_alumno(alumno: object):
        Lista.alumnos.append(alumno)

    # return the best promedio of one course
    @staticmethod
    def mejor_promedio(curso: str):
        promedio_max = 0
        for alumno in Lista.alumnos:
            if alumno.curso == curso:
                if alumno.promedio > promedio_max:
                    promedio_max = alumno.promedio
        return promedio_max



def main():
    # create a list of Alumno objects
    alumno1 = Alumno("Juan", "Perez", "12345678", "1234", "alumno1@gmail.com", "1A", 8.5)
    alumno2 = Alumno("Maria", "Gomez", "87654321", "5678", "alumno2@gmail.com", "2B", 7.5)
    alumno3 = Alumno("Pedro", "Lopez", "13579246", "9101", "alumno3@gmail.com", "3C", 9.0)
    alumno4 = Alumno("Ana", "Martinez", "24681013", "1112", "alumno4@gmail.com", "1A", 8.0)
    alumno5 = Alumno("Jose", "Gonzalez", "31415926", "1314", "alumno5@gmail.com", "1A", 7.0)

    # add the Alumno objects to the list
    Lista.agregar_alumno(alumno1)
    Lista.agregar_alumno(alumno2)
    Lista.agregar_alumno(alumno3)
    Lista.agregar_alumno(alumno4)
    Lista.agregar_alumno(alumno5)

    print(Lista.mejor_promedio("1A"))

if __name__ == "__main__":
    main()

