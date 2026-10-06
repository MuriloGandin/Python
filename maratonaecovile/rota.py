# https://judge.beecrowd.com/pt/problems/view/1123

# =========== Enunciado ============
# Descobrir a rota mais barata para a cidade de destino e exibir o custo de pedágio total considerando o desvio

# ============ Regras ================
# Arestas = rodovias
# Vértices = cidades
# Passar por rodovia > pagar pedágio
# C > Número de cidades que a rota de serviço faz (E C-1 o número de estradas)
# Rota de serviço não pode passar pela mesma cidade
# Veículo só pode trafegar na rota escolhida
# Se o veículo passar por qualquer cidade na rota de serviço, deve seguir a rota até o fim
# As cidades são identificadas por índices de 0 a N-1

# =========== Entrada, em ordem ===========
# Linha 1 infos gerais:
    # N entre 4 e 250 - Número de cidades no país 
    # M maior que 3 e menor que N×(N−1)/2 - Número de estradas
    # C - Número de cidades na rota de serviço
    # K - Cidade de origem considerando o desvio
# Linhas seguintes - rodovias (final 0 0 0 0 ):
    # U positivo - cidade origem de uma rodovia
    # V positivo diferente de U - cidade de destino de uma rodovia
    # P entre 0 e 250 - custo do pedágio da mesma rodovia

N, M, C, K = list(map(int, input().split()))

for _ in range(N):
    entrada = input()



if entrada == "0 0 0 0":
    exit(0)

    