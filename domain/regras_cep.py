from services import consultacep, consultatempo


def analisar_cep(cep):
    if len(cep) == 8:
        local = consultacep.cidade_por_cep(cep)
    if len(local) > 0:
        (temperatura, clima) = consultatempo.tempo_por_cidade(local)

    return temperatura, clima, local