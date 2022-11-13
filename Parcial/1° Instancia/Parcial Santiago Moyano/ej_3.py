"""
Realiza POO en Python, para obtener el total de cada tipo de salario de N cantidad de
personal de acuerdo a los siguientes requerimientos:
En una empresa existen dos categorías de personal: el personal con salario fijo y el
personal a comisión. Los empleados con salario fijo tienen un sueldo básico y un
porcentaje adicional en función del número de años que llevan:
• Menor de dos años cobra salario base.
• de 2 a 5 años: 5% + salario base.
• de 5 a 10 años: 10% + salario base.
• de 10 a 20 años: 15% + salario base.
• más de 20 años: 20% + salario base.
Los empleados a Comisión tienen un salario base más una comisión.
Si en el mes las ventas promedio por empleados (incluyendo a persona con salario fijo) de
la empresa, superan al salario base, se le dará además del salario base un bono de 35.000
pesos a los empleados a Comision.
"""

class Personal():
    
    def __init__(self, nombre: str, años : int):
        self.__nombre = nombre
        self.__años = años

    @property
    def años(self):
        return self.__años

    @años.setter   
    def años(self, value):
        self.__años = value

class PersonalFijo(Personal):
    
    def __init__(self,nombre : str, sueldo_basico : int, años : int):
        self.__sueldo_basico = sueldo_basico
        super().__init__(nombre, años)

    def calcular_porcentaje(self):
        if int(super().años) < 2:
            print(self.__sueldo_basico)
        if 2 <= int(super().años) <= 5:
            plus = self.__sueldo_basico * 0.05
        if 5 <= int(super().años) <= 10:
            plus = self.__sueldo_basico * 0.10
        if 10 <= int(super().años) <= 20:
            plus = self.__sueldo_basico * 0.15
        if int(super().años) > 20:
            plus = self.__sueldo_basico * 0.20

        return plus

class PersonalComision(Personal):

    def __init__(self,nombre: str, salario_base: int):
        self.__salario_base = salario_base
        super().__init__(nombre, años = 0)

    def calcular_comision(self,ventas):
        if ventas > self.__salario_base:
            comision = self.__salario_base + 35.000
            return comision
        else:
            return self.__salario_base

if __name__ == "__main__":
    ventas_mensuales = 100000

    personal1 = PersonalFijo('Carlos', 70000, 7)

    personal2 = PersonalComision('Saul', 40000)

    personal3 = PersonalFijo('Shoberto', 80000, 10)

    personal4 = PersonalComision('Capi', 50000)
    
    personal = [personal1,personal2, personal3, personal4]
    promedio_ventas = ventas_mensuales / len(personal)
    for persona in personal:
        if isinstance(persona, PersonalFijo):
            print(persona.calcular_porcentaje())
        else:
            print(persona.calcular_comision(promedio_ventas))