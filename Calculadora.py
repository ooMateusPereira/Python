# Definição das funções de operações matemáticas
soma = lambda x, y: x + y
menos = lambda x, y: x - y
divi = lambda x, y: x / y
multi = lambda x, y: x * y

# Solicita ao usuário a operação desejada
operacao = input("Qual operação você deseja realizar (soma, menos, divi, multi)? ").strip().lower()

# Solicita ao usuário os números para a operação
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Dicionário para mapear as operações
operacoes = {
    'soma': soma,
    'menos': menos,
    'divi': divi,
    'multi': multi
}

# Verifica se a operação é válida e calcula o resultado
if operacao in operacoes:
    resultado = operacoes[operacao](x, y)
    print(f"O resultado da operação {operacao} é: {resultado}")
else:
    print("Operação inválida!")
