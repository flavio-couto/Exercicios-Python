from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, nome, agencia, conta, saldo):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __str__(self):
        return f"\nOlá {self.nome}, o seu saldo é de R$ {self.saldo}"

    # Cada tipo de conta vai ter seu método sacar com suas diferenças
    @abstractmethod
    def sacar(self):
        pass

    def depositar(self):
            valor = float(input("\nDigite o valor para depósito: "))
            self.saldo += valor
            print(f'\nDepósito efetuado com sucesso.\nVocê depositou R$ {valor} reais na sua {__class__.__name__}.\nSeu saldo atual é R$ {self.saldo}')


class ContaCorrente(Conta):
    
    # A Conta corrente possui um limite que será somado ao saldo caso o valor do saque seja maior que o limite disponível
    def __init__(self, nome, agencia, conta, saldo, limite=500):
        super().__init__(nome, agencia, conta, saldo)
        self.limite = limite

    def sacar(self):
        valor = float(input("\nDigite o valor desejado para saque: R$ "))

        if valor <= self.saldo:   
            self.saldo -= valor
            print(f'\nTransação Autorizada!\nVocê sacou R$ {valor} reais.\nSeu saldo atual é R$ {self.saldo}')

        elif valor <= (self.saldo + self.limite):
            
            # Calcula o valor do limite que será usado
            limiteUsado = valor - self.saldo
            
            print(f'\nO seu saldo atual é de R$ {self.saldo}.\nSeu limite atual é de R$ {self.limite}.')
            print(f'Gostaria de usar R$ {limiteUsado:.2f} do seu limite de R$ {self.limite:.2f}?')

            opcao = int(input(f'\n1 - Utilizar Limite.\n2 - Cancelar operação.'))

            # Valida se a opção digitada é 1 ou 2
            while opcao not in(1 ,2):
                opcao = int(input(f'\nDigite uma opção válida.\n\n1 - Utilizar Limite.\n2 - Cancelar operação.'))
            
            if opcao == 1:
                self.saldo = 0
                self.limite -= limiteUsado 
                print(f'\nOperação Autorizada! Seu saldo atual é de R$ {self.saldo}.\nVocê ainda tem R$ {self.limite} de limite de saque.')
            
            if opcao == 2:
                print("\nOperação Cancelada. Obrigado por utilizar nosso banco!")

        else:
            print (f'\nSaque não autorizado.\nSeu saldo atual é de R$ {self.saldo} e seu limite é de: R$ {self.limite}.\nTotal disponível para saque {self.saldo + self.limite}')

class ContaSalario(Conta):

    def __init__(self, nome, agencia, conta, saldo, limite_saque=3):
        super().__init__(nome, agencia, conta, saldo)
        self.limite_saque = limite_saque

    def __str__(self):
        return super().__str__()

    def sacar(self):

            print(f'Saldo Disponível: {self.saldo}\nSaques disponíveis: {self.limite_saque}')

            if self.limite_saque > 0:
                valor = float(input("Digite o valor desejado para saque: R$ "))

                if valor <= self.saldo:
                    self.saldo -= valor
                    self.limite_saque -= 1
                    print(f'\nTransação Autorizada!\nVocê sacou R$ {valor} reais.\n\nSeu saldo atual é R$ {self.saldo}.\nSaques disponíveis: {self.limite_saque}')

                else:
                    print(f'Saldo indisponível. Seu saldo é de {self.saldo}. Tentativa de saque {valor}')

            else:
                 print(f'Limite de saldo esgotado. Você tem direito a 3 saques por mês!')
    
    def depositar(self):
            print(f'Na Conta Salário só a empresa pode fazer depósitos!')    

c1 = ContaCorrente("flavio", 1, 123, 700.00)
c2 = ContaSalario("estagiario", 1, 123, 300.00)

print(c1)
print(c2)

c1.depositar()
c1.sacar()
# c1.sacar()
# c1.sacar()

c2.depositar()
c2.sacar()
# c2.sacar()
# c2.sacar()
