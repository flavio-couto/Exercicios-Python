# Dois exercícios para exercitar um pouco de lógica.
# O primeiro verifica se o número digitado é primo e retorna se é SIM ou NÃO
# O segundo verifica quais os números anteriores ao digitado é primo ou não e os coloca em uma lista de primos ou não primos. 

'''
###############################################
###########   PRIMEIRO EXERCÍCIO    ###########
###############################################
'''

numero = int(input("Digite um número para verificar se ele é primo: "))

primo = True

for i in range(2, numero):

    if numero % i == 0:
        primo = False

if primo:
    print(f'O número {numero} É Primo!')
else:
    print(f'O número {numero} NÃO É Primo!')

'''
###############################################
###########    SEGUNDO EXERCÍCIO    ###########
###############################################
'''

primos = []
naoprimos = []

numero = int(input("Digite um número para saber quais são os números primos até ele: "))

for num in range(1, numero):
    print(f'O número a ser verificado se é primo é o {num}')
    primo = True
    
    # faz a divisão por todos os números anteriores ao que está sendo verificado
    for i in range(2, num):
        print(f'Resto de {num} / {i} = {num%i}')
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f'O número {num} é primo')
        primos.append(num)
    else:
        naoprimos.append(num)

print(f'''
Verificando os números de De 0 a {num+1} esse é o resultado:

Primos: {primos}

Não Primos: {naoprimos}
''')