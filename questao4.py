faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_estado.values())

for estado, faturamento in faturamento_estado.items():
    percentual = (faturamento / total) * 100
    print(f"{estado}: {percentual:.2f}%")