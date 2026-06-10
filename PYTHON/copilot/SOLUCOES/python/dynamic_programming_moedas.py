# Solução: DP - Problema das Moedas

entrada = list(map(int, input().split()))
n = entrada[0]
m = entrada[1]
moedas = list(map(int, input().split()))

# DP[i] = número mínimo de moedas para formar o valor i
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for moeda in moedas:
        if moeda <= i:
            dp[i] = min(dp[i], dp[i - moeda] + 1)

if dp[n] == float('inf'):
    print(-1)
else:
    print(dp[n])
