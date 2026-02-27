def calcular_reajuste(valor):
    return valor * 1.3

nome_lambda = lambda nome : nome.upper()

print(nome_lambda('Juca'))

lista = ['ana', 'maria', 'carlos', 'pedro']

print(*list(map(lambda nome : nome.upper(), lista)))