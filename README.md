# Exercicios-Python

Esse repositório foi criado para que eu possa refazer alguns exercícios que já fiz no passado, aqueles clássicos que a gente aprende em qualquer linguagem como calculadora, verificar números pares, primos, simulação de agência bancária, trabalhar com listas, operador ternário, list comprehension, dentre outras coisas.

A intenção é reforçar esses conceitos de lógica (if, else, while, for), POO(Hierarquia, herança, polimorfismo), uso das bibliotecas(Pandas, matplotlib) dentre outras coisas!

## Calculadora

O primeiro exercício postado, tinha feito o primeiro modelo com vários 'Ifs' mas depois alterei para o match case para simplificar, usei o while para fazer a validação do operador e do divisor por 0. Acredito que tenha ficado simples e usável com as validações necessárias para o bom funcionamento.

## Números Primos

O meu segundo exercício, nele existem duas formas de identificar os números primos.

No primeiro ele verifica se o número digitado é primo apenas. 
EX: Digita 7 ele verifica se o 7 é primo

No segundo modo ele verifica quais os números são primos até aquele número e separa em duas listas de primos e não primos. 
EX: Digita 10 ele verifica de 1 a 10 quais desses números são primos ou não.

## Agência Bnacária

Meu terceiro exercício, esse particularmente eu gosto bastante, consigo trabalhar vários conceito de python nele, criação de classes, métodos, trabalhar com herança, polimorfismo, classes abstratas, usar condições if, else, while, tratar erros. Eu sempre consigo aprimorar ele cada vez que abro.

Nele tem a classe mãe que é a Conta, nela tem dois métodos o "sacar" e "depositar". O depositar seria padrão mas quis usar o polimorfismo na Conta salário para não permitir depósito, seria uma conta que só a empresa pode depositar. O método Sacar já é abstrato e cada tipo de Conta (Corrente e  Salário) tem suas características.

A Conta corrente possui um limite que pode ser utilizado junto com o saldo caso o valor do saque seja maior que o saldo.
Já a Conta salário não tem limite para ser usado e possui uma quantidade máxima de saques para realizar (3 saques).
