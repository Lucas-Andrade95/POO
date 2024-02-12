class ContaBancária:
    def __init__(self, saldo=0, titular='Desconhecido'):
        self.saldo = saldo
        self.titular = titular

    def mostrar_saldo(self):
        print(f'Saldo: {self.saldo}')
    
    def depositar(self):
        deposito = float(input('Valor a ser depositado: R$'))
        self.saldo += deposito
    
    def sacar(self):
        saque = float(input('Valor do saque R$: '))
        self.saldo -= saque

conta1 = ContaBancária(0,'João')
conta2 = ContaBancária(1000,'Ana')

conta1.mostrar_saldo()
conta1.depositar()
conta1.mostrar_saldo()
conta2.sacar()
conta2.mostrar_saldo()