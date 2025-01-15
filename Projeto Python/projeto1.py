# print ("hello world")
# Crie um programa que recebe um número e imprime o seu fatorial

'''
Quais são os dados de entrada necessário?
número
O que devo fazer com esses dados?
eu devo calcular  o fatorial do número que for p assado para o meu programa e o exibir na tela
Quais são as restrições do problema?
o número deve ser um número valor positivo
o número deve ser um valor inteiro
Qual resultado esperado?
o resultado esperado é que o fatorial do número providenciado seja exibido
Qual a sequência de pasasos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial)
''' 
numero = int(input('digite um número'))
if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
        fatorial = fatorial * item
    print(fatorial)