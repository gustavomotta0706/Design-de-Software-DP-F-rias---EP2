import random
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

# 2.3
def valida_questoes(questoes):
    lista_erros = []
    for item in questoes:
        erro = valida_questao(item)
        lista_erros.append(erro)
    
    if len(lista_erros) == 0:
        return {}
    else:
        return lista_erros

# 2.4
def sorteia_questao(questoes, nivel):
    lista = questoes[nivel]
    indice = random.randint(0, len(lista) - 1)
    
    return lista[indice]

# 2.5
def sorteia_questao_inedita(dicionario, nivel, lista):
    questao = sorteia_questao(dicionario, nivel)

    while questao in lista:
        questao = sorteia_questao(dicionario, nivel)

    return questao

# 2.6
def questao_para_texto(questao, id):
    texto = "----------------------------------------\n"
    texto += f"QUESTAO {id}\n\n"
    texto += f"{questao['titulo']}\n\n"
    texto += "RESPOSTAS:\n"
    texto += f"A: {questao['opcoes']['A']}\n"
    texto += f"B: {questao['opcoes']['B']}\n"
    texto += f"C: {questao['opcoes']['C']}\n"
    texto += f"D: {questao['opcoes']['D']}"
    return texto

# 2.7
def gera_ajuda(questao):
    erradas = []

    for letra in questao["opcoes"]:
        if letra != questao["correta"]:
            erradas.append(questao["opcoes"][letra])

    quantidade = random.randint(1, 2)

    indice = random.randint(0, len(erradas) - 1)
    resposta = erradas[indice]
    erradas.pop(indice)

    if quantidade == 2:
        indice = random.randint(0, len(erradas) - 1)
        resposta += " | " + erradas[indice]

    texto = "DICA:\n"
    texto += "Opções certamente erradas: "
    texto += resposta

    return texto