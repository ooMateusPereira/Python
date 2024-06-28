#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite outro número: '))
#n3 = n1 + n2
#print('A soma de:', n1, '+', n2, 'deu:', n3)
#print('A soma de {} e {} vale {}'.format(n1, n2, n3))

n = input('Digite algo: ')
print('O tipo primitivo é: ', type(n))
print('Tem espaço? ', n.isspace())
print('É número? ', n.isnumeric())
print('É letra? ', n.isalpha())
print('É maiúsculo: ', n.isupper())