def calculadora():

    num_1 = int(input("Digite o primeiro número:"))

    operador = input('''
    Digite o operador: ''')
    
    num_2 = int(input("Digite o segundo número:"))

    match operador:
        case '+':
            resposta = num_1 + num_2
        case '-':
            resposta = num_1 - num_2
        case '*':
           resposta = num_1 * num_2
        case '/':
            if num_2 == 0:
                resposta = f'O divisor tem que ser diferente de 0.'

    return print(resposta)

calculadora()


# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def fazer_calculo():
#     n1 = int(input("Digite o primeiro número: "))
#     n2 = int(input("Digite o segundo número: "))


