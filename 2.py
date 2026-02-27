nomes = ["Ana", "Beatriz", "Caio", "Daniela", "Edu"]

curto = lambda nome: len(nome) == 3

teste = list(filter(curto, nomes))

print(teste)