def valor_taxa(quantia):
    taxa = quantia * 0.25
    total = quantia * 1.25
    return taxa, total

preco = valor_taxa(100)
print(preco)