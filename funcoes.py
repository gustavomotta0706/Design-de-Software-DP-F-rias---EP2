
# 2.1
def transforma_base(questoes):
    base_por_nivel = {}

    for questao in questoes:
        nivel = questao['nivel']

        if nivel not in base_por_nivel:
            base_por_nivel[nivel] = []

        base_por_nivel[nivel].append(questao)

    return base_por_nivel

# 2.2   
def valida_questao(questao):
    erros = {}

    obrigatorias = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in obrigatorias:
        if chave not in questao:
            erros[chave] = 'nao_encontrado'

    if len(questao) != 4:
        erros['outro'] = 'numero_chaves_invalido'

    if 'titulo' in questao:
        if questao['titulo'].strip() == '':
            erros['titulo'] = 'vazio'

    if 'nivel' in questao:
        if questao['nivel'] not in ['facil', 'medio', 'dificil']:
            erros['nivel'] = 'valor_errado'

    if 'opcoes' in questao:
        opcoes = questao['opcoes']

        if len(opcoes) != 4:
            erros['opcoes'] = 'tamanho_invalido'
        else:
            if ('A' not in opcoes or
                'B' not in opcoes or
                'C' not in opcoes or
                'D' not in opcoes):
                erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                vazias = {}

                for letra in ['A', 'B', 'C', 'D']:
                    if opcoes[letra].strip() == '':
                        vazias[letra] = 'vazia'

                if vazias:
                    erros['opcoes'] = vazias

    if 'correta' in questao:
        if questao['correta'] not in ['A', 'B', 'C', 'D']:
            erros['correta'] = 'valor_errado'

    return erros


