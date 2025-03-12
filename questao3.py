import json


def faturamentoMinMax(vetor):
    menor = min(val for val in vetor if val > 0.0)
    maior = max(vetor)
    
    return menor, maior

def diasMedia(vetor):
    media = 0
    for i in range(len(vetor)):
        if vetor[i] > 0.0: #ignora valores negativos
            media = media + vetor[i]
    
    
    media = media / len(vetor)  
          
    dias = 0
    for i in range(len(vetor)):
        if media > vetor[i]:
            dias = dias + 1
    
    return dias


with open('dados.json', 'r') as file:
    arquivo = json.load(file)


num_dias = max(item["dia"] for item in arquivo) #determinar quantos dias tem no arquivo json

vetor = [0.0] * num_dias #inicializar um vetor no mesmo tamanho da quantidades de dias

for item in arquivo:
    vetor[item["dia"] - 1] = item["valor"]
    
#print(vetor)


menor, maior = faturamentoMinMax(vetor)
dias = diasMedia(vetor)

print(f"O menor faturamento foi de {menor} R$.")
print(f"O maior faturamento foi de {maior} R$.")
print(f"Houve {dias} dias que o faturamento diário superou a média mensal.")