'''
Exercício prático para reforçar conceitos de Python, comparando diferentes formas de criar
e manipular listas. Utilizei laços de repetição, *list comprehensions*, funções `lambda`,
 `map()` e `filter()` para gerar listas, calcular dobros e separar números pares e ímpares.
'''

# ============ SIMPLES (_S) ==========

lista_S = []
listaDobro_S = []
pares_S = []
impares_S =  []


# Gerar lista
for i in range(1, 11):
    lista_S.append(i)

print(lista_S)

# Dobro dos itens da lista
for i in lista_S:
    listaDobro_S.append(i * 2)

print(listaDobro_S)

# Pares e ímpares
for i in range(1, 11):
    if i % 2 == 0:
        pares_S.append(i)
    else:
        impares_S.append(i)

print(pares_S)
print(impares_S)

# ========================================
# ============ TERNÁRIOS (_T) ============
# ========================================

lista_T = [i for i in range(1, 11)]
print(lista_T)

listaDobro_T = [i * 2 for i in lista_T]
print(listaDobro_T)

pares_T = [p for p in lista_T if p % 2 == 0]
print(pares_T)

impares_T = [i for i in lista_T if i % 2 != 0]
print(impares_T)

# =========================================
# ============ FUNÇÃO LAMBDA (_L) =========
# =========================================

lista_L = list(map(lambda x: x, range(0,11)))
print(lista_L)

listaDobro_L = list(map(lambda x: x * 2, lista_L))
print(listaDobro_L)

pares_L = list(filter(lambda x: x % 2 == 0, lista_L))
print(pares_L)

impares_L = list(filter(lambda x: x % 2 != 0, lista_L))
print(impares_L)

impares_L = list(filter(lambda x: x % 2 != 0, lista_L))
print(impares_L)