# Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a
# coluna) do maior valor
matriz = [
    [5, 8, 2, 1],
    [7, 3, 200, 4],
    [6, 0, 12, 10],
    [11, 14, 13, 15]
]

maior = matriz[0][0]
linha = 0
coluna = 0

i = 0

while i < 4:
    j = 0
    while j < 4:
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j
        j += 1
    i += 1

print("Maior valor:", maior)
print("Linha:", linha)
print("Coluna:", coluna)