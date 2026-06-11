competidores, quant_total, quant_per_competidor = map(int, input().split())
    #quant_total = competidores * quant_per_competidor + r
folhas_totais_gastas = competidores * quant_per_competidor

if quant_total >= folhas_totais_gastas:
    print('S')
else:
    print('N')
