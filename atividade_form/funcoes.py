import statistics

def calc_media(lista):
    return statistics.mean(lista)

def calc_mediana(lista):
    return statistics.median(lista)

def calc_moda(lista):
    moda = None
    maior_freq = 0

    for i in lista:
        freq = lista.count(i)
        if freq > maior_freq:
            maior_freq = freq
            moda = i

    if maior_freq == 1:
        return "Sem moda"
    else:
        return moda

def calc_amplitude(lista):
    return max(lista) - min(lista)

def calc_desvio_padrao(lista):
    return statistics.stdev(lista)

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def calc_varianca(lista):
    return statistics.variance(lista)