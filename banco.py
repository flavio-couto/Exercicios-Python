class Conta:
    
    def __init__(self, nome, agencia, conta, saldo):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __str__(self):
        return f"Olá {self.nome}, o seu saldo é de R$ {self.saldo}"


    def sacar(self):
        pass

    def depositar(self):
            valor = float(input("Digite o valor para depósito: "))
            self.saldo += valor
            print(f'Depósito efetuado com sucesso.\nVocê depositou R$ {valor} reais. Seu saldo atual é R$ {self.saldo}')        

class ContaCorrente(Conta):
    
    def __init__(self, nome, agencia, conta, saldo, limite=500):
        super().__init__(nome, agencia, conta, saldo)
        self.limite = limite

    def sacar(self):

        valor = float(input("Digite o valor desejado para saque: R$ "))

        if valor <= self.saldo:
    
            self.saldo -= valor
            print(f'Transação Autorizada!\nVocê sacou R$ {valor} reais.\nSeu saldo atual é R$ {self.saldo}')

        elif valor <= (self.saldo + self.limite):

            limiteUsado = valor - self.saldo
            
            print(f'O seu saldo atual é de R$ {self.saldo}.\nSeu limite atual é de R$ {self.limite}.')
            print(f'Gostaria de usar R$ {limiteUsado:.2f} do seu limite de R$ {self.limite:.2f}?')

            opcao = int(input(f'1 - Utilizar Limite.\n2 - Cancelar operação.'))
            if opcao == 1:
                self.saldo -= valor
                self.limite -= limiteUsado 
                print(f'Operação Autorizada! Seu saldo atual é de R$ {self.saldo}.\nVocê ainda tem R$ {self.limite} de limite de saque.')

            else:
                print("Operação Cancelada. Obrigado por utilizar nosso banco!")

        elif valor <= self.limite:

            opcao = int(input(f'1 - Deseja utilizar R$ {valor} do seu limite de R$ {self.limite}.\n2 - Cancelar operação.'))
            if opcao == 1:
                self.saldo -= valor
                self.limite -= valor
                print(f'Operação Autorizada! Seu saldo atual é de R$ {self.saldo}.\nVocê ainda tem R$ {self.limite} de limite de saque.')

            elif opcao == 2:
                print(f'Operação Cancelada.')

            else:
                print(f'Opção inválida. Cancelando Operação.')

        else:
            print (f'Limite indisponível. O seu limite é de R$ {self.limite}.')

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
                    print(f'\nTransação Autorizada!\nVocê sacou R$ {valor} reais.\nSeu saldo atual é R$ {self.saldo}.\nSaques disponíveis: {self.limite_saque}')

                else:
                    print(f'Saldo indisponível. Seu saldo é de {self.saldo}. Tentativa de saque {valor}')

            else:
                 print(f'Limite de saldo esgotado. Você tem direito a 3 saques por mês!')
    
    def depositar(self):
            print(f'Na conta salário ({__class__.__name__}) só a empresa pode fazer depósitos!')    

c1 = ContaCorrente("flavio", 1, 123, 700.00)
c2 = ContaSalario("estagiario", 1, 123, 300.00)

# print(c1)
# print(c2)
# c1.sacar()
c2.sacar()