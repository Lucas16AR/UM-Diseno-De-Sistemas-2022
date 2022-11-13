tipo_cuentas: dict[int: str] = {
    1: 'Sueldo',
    2: 'Normal',
}

class User:

    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Cuenta:

    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def __repr__(self) -> str:
        return f'{self.tipo}'

class BankAccount:

    def __init__(self, cuenta_numero: int, alias: str, usuario: User, clase_cuenta: Cuenta, balance: float = 0.0) -> None:
        self.cuenta_numero = cuenta_numero
        self.alias = alias
        self.usuario = usuario
        self.clase_cuenta = clase_cuenta
        self.balance = balance

    def depositar(self, monto: float) -> None:
        if self.clase_cuenta.tipo == 'Normal':
            self.balance += monto - (monto * 0.05)
            return
        self.balance += monto

    def retirar(self, monto: float) -> None:
        if self.clase_cuenta.tipo == 'Normal':
            self.balance -= monto + (monto * 0.05)
            return
        self.balance -= monto

    def __repr__(self) -> str:
        return f'BankAccount(cuenta_numero={self.cuenta_numero}, alias={self.alias}, usuario={self.usuario}, clase_cuenta={self.clase_cuenta}, balance={self.balance})'

if __name__ == '__main__':
    user = User('Juan', 'Perez')
    user2 = User('Martin', 'Garcia')
    cuenta = Cuenta(tipo_cuentas[1])
    cuenta2 = Cuenta(tipo_cuentas[2])
    bank_account = BankAccount(123, 'juanpe', user, cuenta)
    bank_account2 = BankAccount(124, 'marga', user2, cuenta2)
    bank_account.depositar(100)
    bank_account2.depositar(100)
    print(bank_account)
    print(bank_account2)
    bank_account.retirar(50)
    bank_account2.retirar(50)
    print(bank_account)
    print(bank_account2)