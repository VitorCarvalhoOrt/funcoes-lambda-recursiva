produtos = [("Teclado", 150), ("Mouse", 80), ("Monitor", 900)]

ordenado_por_preco = sorted(produtos, key=lambda item: item[1])

print(ordenado_por_preco)