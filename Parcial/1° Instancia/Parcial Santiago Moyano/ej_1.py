"""
Representar una cuenta bancaria con Python, compuesta por los siguientes atributos:
cuenta_numero: str,
balance: float,
alias: str,
usuario: de tipo Usuario,
clase_cuenta: de tipo ClaseCuenta la cual puede ser "cuenta sueldo" o "normal"
La clase debe tener métodos para administrar las acciones de depósito y retiro de dinero.
De acuerdo al tipo usuario en la cuenta bancaria se aplican comisiones con un porcentaje
del 5% sobre balance para las cuentas que no son de "tipo sueldo".
Mostrar que depositando y retirando dinero cambia el balance de la cuenta.
Mostrar los detalles de todas cuentas creadas con su balance y comisiones cobradas.
"""

class Usuario():

    def __init__(self, nombre, dni):

        self.__nombre = nombre

        self.__dni = dni

class ClaseCuenta():

        def __init__(self, tipo: bool):
            #si tipo es = True es cuenta sueldo si tipo es = False es cuenta normal
            self.__tipo= tipo

        @property
        def tipo(self):
            return self.__tipo
        @tipo.setter
        def tipo(self, valor):
            self.__tipo = valor

class Cuenta():

    def __init__(self, cuenta_numero: str, balance: float, alias : str, usuario : Usuario, 
    clase_cuenta : ClaseCuenta):

        self.__cuenta_numero = cuenta_numero

        self.__balance = balance

        self.__alias = alias

        self.__usuario = usuario

        self.__clase_cuenta = clase_cuenta

        self.__comision_total = 0
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, valor):
        self.__balance = valor

    @property
    def comision_total(self):
        return self.__comision_total
    
    @comision_total.setter
    def comision_total(self, valor):
        self.__comision_total = valor

    def retirar_dinero(self, valor):
        if self.__clase_cuenta.tipo:
            self.__balance -= valor
        else:
            comision = valor * 0.05
            self.__comision_total += comision
            self.__balance -= (valor + comision)
            print(f'Saldo Actual, {self.__balance}')
    
    def depositar_dinero(self, valor):

        self.__balance += valor
        print(f'Saldo Actual, {self.__balance}')


if __name__ == "__main__":
    usuario1 = Usuario("Santiago", "34567883")
    usuario2 = Usuario("Bruno", "324334332")
    cuenta_normal = ClaseCuenta(False)
    cuenta_sueldo = ClaseCuenta(True)
    cuenta_bancaria1 = Cuenta("1111", 0, "Santiago.mp", usuario1, cuenta_normal)
    cuenta_bancaria2 = Cuenta("2222", 100, "Bruno.uala", usuario2, cuenta_sueldo)
    cuentas = [cuenta_bancaria1, cuenta_bancaria2]
    cuenta_bancaria1.depositar_dinero(100)
    cuenta_bancaria2.depositar_dinero(100)
    cuenta_bancaria1.retirar_dinero(20)
    cuenta_bancaria2.retirar_dinero(40)
    for cuenta in cuentas:
        print(cuenta.balance, cuenta.comision_total)