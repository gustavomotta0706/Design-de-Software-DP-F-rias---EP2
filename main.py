import random

from base import questoes
from funcoes import (
    transforma_base,
    valida_questoes,
    questao_para_texto,
    gera_ajuda,
)

VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
ROXO = "\033[95m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

PREMIOS = [
    1000,
    5000,
    10000,
    30000,
    50000,
    100000,
    300000,
    500000,
    1000000,
]


def mostrar_manual():
    print(f"\n{ROXO}{NEGRITO}" + "=" * 40 + RESET)
    print(f"{ROXO}{NEGRITO}FORTUNA DESSOFT{RESET}")
    print(f"{ROXO}{NEGRITO}" + "=" * 40 + RESET)
    print(f"{AZUL}Regras:{RESET}")
    print(f"{AZUL}- Responda com A, B, C ou D.{RESET}")
    print(f"{AZUL}- Digite 'pula' para trocar a pergunta.{RESET}")
    print(f"{AZUL}- Digite 'ajuda' para eliminar respostas erradas.{RESET}")
    print(f"{AZUL}- Se errar, perde o jogo.{RESET}")
    print(f"{AZUL}- Após acertar, pode continuar ou parar.{RESET}")
    print(f"{ROXO}{NEGRITO}" + "=" * 40 + RESET)


def mostrar_estado(nome, premio, pulos, ajudas, nivel):
    print(f"\n{AZUL}" + "-" * 40 + RESET)
    print(f"{AZUL}Jogador:{RESET} {NEGRITO}{nome}{RESET}")
    print(f"{AZUL}Prêmio:{RESET} {VERDE}{NEGRITO}R$ {premio}{RESET}")
    print(f"{AZUL}Pulos:{RESET} {AMARELO}{pulos}{RESET}")
    print(f"{AZUL}Ajudas:{RESET} {AMARELO}{ajudas}{RESET}")
    print(f"{AZUL}Nível atual:{RESET} {ROXO}{nivel}{RESET}")
    print(f"{AZUL}" + "-" * 40 + RESET)


def escolher_questao_do_nivel(base_por_nivel, nivel, questoes_jogadas):
    disponiveis = []

    for questao in base_por_nivel[nivel]:
        if questao not in questoes_jogadas:
            disponiveis.append(questao)

    if len(disponiveis) == 0:
        return None

    return random.choice(disponiveis)


def proximo_nivel(nivel_atual):
    if nivel_atual == "facil":
        return "medio"
    if nivel_atual == "medio":
        return "dificil"
    return "dificil"


def joga_partida(questoes):
    erros = valida_questoes(questoes)

    if any(erro != {} for erro in erros):
        print(f"{VERMELHO}{NEGRITO}Base inválida!{RESET}")
        print()

        for i, erro in enumerate(erros):
            if erro != {}:
                print(f"{VERMELHO}Questão {i + 1}: {erro}{RESET}")

        return

    base = transforma_base(questoes)

    nome = input(f"{CIANO}Digite seu nome: {RESET}")

    mostrar_manual()

    questoes_jogadas = []

    premio = 0
    indice_premio = 0

    pulos = 3
    ajudas = 2

    nivel_atual = "facil"
    acertos_no_nivel = 0

    while True:
        if indice_premio >= len(PREMIOS):
            print(f"\n{VERDE}{NEGRITO}PARABÉNS!{RESET}")
            print(f"{VERDE}Você ganhou R$ 1.000.000!{RESET}")
            return

        questao = escolher_questao_do_nivel(base, nivel_atual, questoes_jogadas)

        if questao is None:
            print(f"{AZUL}Não há mais perguntas no nível {nivel_atual}.{RESET}")
            print(f"{AZUL}Você saiu com {VERDE}R$ {premio}{RESET}{AZUL}.{RESET}")
            return

        questoes_jogadas.append(questao)
        ajuda_usada = False

        while True:
            mostrar_estado(nome, premio, pulos, ajudas, nivel_atual)

            print(f"{CIANO}")
            print(questao_para_texto(questao, len(questoes_jogadas)))
            print(RESET)

            resposta = input(
                f"{CIANO}Resposta (A/B/C/D/pula/ajuda): {RESET}"
            ).strip().lower()

            if resposta in ["a", "b", "c", "d"]:
                if resposta.upper() == questao["correta"]:
                    premio = PREMIOS[indice_premio]
                    indice_premio += 1
                    acertos_no_nivel += 1

                    print(f"\n{VERDE}{NEGRITO}Resposta correta!{RESET}")
                    print(f"{VERDE}Prêmio atual: R$ {premio}{RESET}")

                    if nivel_atual == "facil" and acertos_no_nivel == 3:
                        nivel_atual = proximo_nivel(nivel_atual)
                        acertos_no_nivel = 0
                        print(f"{ROXO}Você passou para o nível médio!{RESET}")

                    elif nivel_atual == "medio" and acertos_no_nivel == 3:
                        nivel_atual = proximo_nivel(nivel_atual)
                        acertos_no_nivel = 0
                        print(f"{ROXO}Você passou para o nível difícil!{RESET}")

                    if indice_premio == len(PREMIOS):
                        print(f"\n{VERDE}{NEGRITO}VOCÊ VENCEU O JOGO!{RESET}")
                        print(f"{VERDE}Você ganhou R$ 1.000.000!{RESET}")
                        return

                    continuar = input(
                        f"{CIANO}Deseja continuar? (s/n): {RESET}"
                    ).strip().lower()

                    while continuar not in ["s", "n"]:
                        continuar = input(
                            f"{CIANO}Digite s ou n: {RESET}"
                        ).strip().lower()

                    if continuar == "n":
                        print(
                            f"{AZUL}Você saiu com {VERDE}R$ {premio}{RESET}{AZUL}.{RESET}"
                        )
                        return

                    break

                else:
                    print(f"\n{VERMELHO}{NEGRITO}Resposta errada!{RESET}")
                    print(f"{VERMELHO}Você perdeu o jogo.{RESET}")
                    return

            elif resposta == "pula":
                if pulos > 0:
                    pulos -= 1
                    print(f"{AMARELO}Pergunta pulada.{RESET}")
                    break
                else:
                    print(f"{VERMELHO}Você não possui mais pulos.{RESET}")

            elif resposta == "ajuda":
                if ajudas == 0:
                    print(f"{VERMELHO}Você não possui mais ajudas.{RESET}")

                elif ajuda_usada:
                    print(f"{VERMELHO}Você já usou ajuda nesta pergunta.{RESET}")

                else:
                    print()
                    print(f"{AMARELO}{gera_ajuda(questao)}{RESET}")
                    ajudas -= 1
                    ajuda_usada = True

            else:
                print(f"{VERMELHO}Opção inválida.{RESET}")


def main():
    while True:
        joga_partida(questoes)

        jogar = input(
            f"\n{CIANO}Deseja jogar novamente? (s/n): {RESET}"
        ).strip().lower()

        while jogar not in ["s", "n"]:
            jogar = input(
                f"{CIANO}Digite s ou n: {RESET}"
            ).strip().lower()

        if jogar == "n":
            print(f"{AZUL}Até a próxima!{RESET}")
            break


if __name__ == "__main__":
    main()