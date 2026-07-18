class ContaBancaria:
    def __init__(self, titular, saldo=0, conta_id=None):
        self.id = conta_id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        prefixo = f"ID: {self.id} - " if self.id is not None else ""
        return f"{prefixo}Titular: {self.titular} - Saldo: R${self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de R${valor:.2f}. Saldo insuficiente.")
            return False

        self.saldo -= valor
        return True

    def transferir(self, valor, conta_destino):
        if valor > self.saldo:
            print(f"Transferencia negada de R${valor:.2f}.")
            return False

        self.saldo -= valor
        conta_destino.depositar(valor)
        return True

    def consultar_saldo(self):
        return self.saldo


contabancaria = ContaBancaria

conta1 = contabancaria('João', 6000)
conta2 = contabancaria('Maria', 3500)
conta3 = contabancaria('Pedro', 400)
conta4 = contabancaria('Ana', 1500)

print(f'Conta 1: {conta1}')
print(f'Conta 2: {conta2}')
print(f'Conta 3: {conta3}')
print(f'Conta 4: {conta4}')
conta1.depositar(500)
print(f'Conta 1 após depósito: {conta1}')
conta2.sacar(2_000_000)
print(f'Conta 2 após saque: {conta2}')
conta3.transferir(300, conta4)
print(f'Conta 3 após transferência: {conta3}')
print(f'Conta 4 após transferência: {conta4}')
print(f'Saldo da Conta 1: {conta1.consultar_saldo():.2f}')
print(f'Saldo da Conta 2: {conta2.consultar_saldo():.2f}')
print(f'Saldo da Conta 3: {conta3.consultar_saldo():.2f}')
print(f'Saldo da Conta 4: {conta4.consultar_saldo():.2f}')