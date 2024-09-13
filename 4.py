estados = ["SP", "RJ", "MG", "ES", "Outros"]
faturamentos = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

total_mensal = sum(faturamentos)

for i in range(len(estados)):
    percentual = (faturamentos[i] / total_mensal) * 100
    print(f"{estados[i]}: {percentual:.2f}%")
