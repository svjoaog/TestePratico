def inverte(palavra):
    n = len(palavra) - 1
    
    invertido = "" #string vazia
    
    while n >= 0:
        invertido += palavra[n]
        n -= 1
        
    return invertido


palavra = input("Digite a palavra: ")

print(f"Palavra invertida: {inverte(palavra)}")    