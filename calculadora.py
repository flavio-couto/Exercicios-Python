# Incluído o validador do operador que tem que ser os já pré-definidos;
# E feita a validação da divisão por 0.

def calculadora():

    # Primeiro Número
    num_1 = float(input("\nDigite o primeiro número:"))

    # Operação
    operador = input('''
Digite o operador:
    '+' : Somar
    '-' : Subtrair
    '*' : Multiplicar
    '/' : Dividir
    ''')

    # Faz a validação para ver se o operador digitado é válido e se foi inserido apenas um dígito
    while operador not in '+-*/' or len(operador) != 1:
        operador = input('''
    
    *** Digite um operador válido (use apenas um caracter): ***
    
    '+' : Somar
    '-' : Subtrair
    '*' : Multiplicar
    '/' : Dividir
    
    ''')

    num_2 = float(input("\nDigite o segundo número:"))

    match operador:
        case '+':
            resposta = num_1 + num_2
        case '-':
            resposta = num_1 - num_2
        case '*':
            resposta = num_1 * num_2
        case '/':
            while num_2 == 0: # Valida se o número do divisor é = 0 e pede um novo número
                num_2 = float(input("Número não pode ser dividido por 0, digite outro número: "))
            resposta = num_1 / num_2

    return print(f'O resultado de {num_1} {operador} {num_2} é = {round(resposta, 2)}')


calculadora()
