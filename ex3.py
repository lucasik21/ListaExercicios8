# Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as
# seguintes informações sobre alunos de uma disciplina, sendo todas as
# informações do tipo inteiro:
# a. Primeira coluna: número de matrícula (use um inteiro)
# b. Segunda coluna: media das provas
# c. Terceira coluna: media dos trabalhos
# d. Quarta coluna: nota final
# Elabore um programa que:
# a. Leia as três primeiras informações de cada aluno;
# b. Calcule a nota final como sendo a soma da média das provas e da
# média dos trabalhos;
# c. Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe
# uma maior nota).
matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
linha = 0
while linha < 5:
    print("ALuno", linha + 1)

    matriz[linha][0] = int(input("Número da Matrícula: "))
    matriz[linha][1] = int(input("Média das provas: "))
    matriz[linha][2] = int(input("Média dos trabalhos: "))
    matriz[linha][3] = matriz[linha][1] + matriz[linha][2]
    linha += 1

maiorNota = matriz[0][3]
matriculaMaior = matriz[0][0]

linha = 1

while linha < 5:
    if matriz[linha][3] > maiorNota:
        maiorNota = matriz[linha][3]
        matriculaMaior = matriz[linha][0]
    
    linha += 1

print("Matrícula do aluno com maior nota final:", matriculaMaior)