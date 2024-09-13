import json

with open("dados.json") as file:
    dados = json.load(file)

faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]

if faturamento:
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    acima_media = len([valor for valor in faturamento if valor > media_mensal])

    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da media mensal: {acima_media}")
else:
    print("Sem dados de faturamento para calcular.")
