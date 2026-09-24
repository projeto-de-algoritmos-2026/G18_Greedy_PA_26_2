def calc_troco_guloso(moedas:list,valor:int) -> dict:
    resultado = {}
    for moeda in moedas:
        if valor >= moeda:
            qnt = valor // moeda
            resultado[moeda] = qnt
            valor %= moeda
        else:
            resultado[moeda] = 0
    return resultado
