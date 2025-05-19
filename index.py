
def simulador_investimento(aporte_inicial, aporte_mensal, taxa_juros_anual, anos):
    saldo = aporte_inicial
    taxa_juros_mensal = (1 + taxa_juros_anual) ** (1 / 12) - 1
    saldo_historico = [saldo]
    
    for mes in range(anos * 12):
        saldo = saldo * (1 + taxa_juros_mensal) + aporte_mensal
        saldo_historico.append(saldo)
    
    return saldo_historico, saldo

aporte_inicial = 0
aporte_mensal = 10000
taxa_juros_anual = 0.12  
anos = 4

saldo_historico, saldo_final = simulador_investimento(aporte_inicial, aporte_mensal, taxa_juros_anual, anos)

print(f"Saldo final após {anos} anos: R$ {saldo_final:.2f}")
