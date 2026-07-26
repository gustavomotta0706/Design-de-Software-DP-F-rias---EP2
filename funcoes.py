
# 2.1
def transforma_base(questoes):
    base_por_nivel = {}

    for questao in questoes:
        nivel = questao['nivel']

        if nivel not in base_por_nivel:
            base_por_nivel[nivel] = []

        base_por_nivel[nivel].append(questao)

    return base_por_nivel


