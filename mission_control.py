NOME_MISSAO = "Nova Frontier X1"
NOME_EQUIPE  = "Equipe Vega"

dados_missao = [
    [22, 95, 91, 98, 93],
    [26, 83, 75, 95, 87],
    [32, 61, 54, 90, 68],
    [37, 40, 35, 85, 52],
    [41, 25, 17, 76, 33],
    [35, 52, 30, 80, 48],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados_ciclo, classificacao):
    criticos = [r[0] for r in resultados_ciclo if r[1] == "CRÍTICO"]

    if classificacao == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."

    if classificacao == "MISSÃO CRÍTICA" and len(criticos) >= 3:
        return ("Ativar modo de segurança e priorizar suporte à vida, "
                "energia e comunicação.")

    recomendacoes = []
    nomes = ["temperatura", "comunicação", "bateria", "oxigênio", "estabilidade"]
    acoes = [
        "Verificar controle térmico da missão.",
        "Tentar restabelecer contato com a base.",
        "Ativar modo de economia de energia.",
        "Acionar protocolo de suporte à vida.",
        "Reduzir operações não essenciais.",
    ]

    for i, resultado in enumerate(resultados_ciclo):
        if resultado[1] == "CRÍTICO":
            recomendacoes.append(acoes[i])

    if recomendacoes:
        return " ".join(recomendacoes)

    return "Monitorar sistemas em atenção e preparar plano de contingência."


def analisar_tendencia(riscos_ciclos):
    primeiro = riscos_ciclos[0]
    ultimo   = riscos_ciclos[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area):
    maior_indice = 0
    for i in range(1, len(pontos_por_area)):
        if pontos_por_area[i] > pontos_por_area[maior_indice]:
            maior_indice = i
    return areas_monitoradas[maior_indice]


def analisar_ciclo(ciclo):
    temp, com, bat, oxi, est = ciclo
    return [
        ("Temperatura",  *analisar_temperatura(temp)),
        ("Comunicação",  *analisar_comunicacao(com)),
        ("Bateria",      *analisar_bateria(bat)),
        ("Oxigênio",     *analisar_oxigenio(oxi)),
        ("Estabilidade", *analisar_estabilidade(est)),
    ]


def gerar_relatorio_final(riscos, pontos_area, medias):
    n = len(riscos)
    ciclo_critico  = riscos.index(max(riscos)) + 1
    risco_medio    = sum(riscos) / n
    qtd_criticos   = sum(1 for r in riscos if r >= 6)
    tendencia      = analisar_tendencia(riscos)
    area_afetada   = identificar_area_mais_afetada(pontos_area)
    class_final    = classificar_ciclo(round(risco_medio))

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"\nQuantidade de ciclos analisados: {n}")
    print(f"\nMédia de temperatura : {medias[0]:.2f} °C")
    print(f"Média de comunicação : {medias[1]:.2f}%")
    print(f"Média de bateria     : {medias[2]:.2f}%")
    print(f"Média de oxigênio    : {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
    print(f"\nCiclo mais crítico      : Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {max(riscos)}")
    print(f"Risco médio da missão   : {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")
    print(f"\nTendência da missão:\n{tendencia}")
    print("\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontos_area[i]} pontos")
    print(f"\nÁrea mais afetada:\n  {area_afetada}")
    print(f"\nClassificação final da missão:\n  {class_final}")

    print("\nConclusão:")
    if class_final == "MISSÃO ESTÁVEL":
        print("A missão transcorreu dentro dos parâmetros normais. "
              "Todos os sistemas operaram de forma satisfatória.")
    elif class_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou instabilidade relevante durante a operação. "
              "Apesar da tentativa de recuperação no último ciclo, ainda existem "
              "sistemas em atenção e a equipe deve manter o plano de contingência ativo.")
    else:
        print("A missão atingiu níveis críticos em múltiplos ciclos. "
              "Recomenda-se revisão completa dos sistemas antes de qualquer "
              "nova operação.")
    print("=" * 60)


def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos_ciclos  = []
    pontos_por_area = [0] * 5
    somas           = [0.0] * 5

    for numero_ciclo, ciclo in enumerate(dados_missao, start=1):
        print(f"\nCICLO {numero_ciclo}")
        print("-" * 60)

        resultados = analisar_ciclo(ciclo)
        labels     = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
        unidades   = ["°C", "%", "%", "%", "%"]

        pontuacao_ciclo = 0

        for i, (nome, classif, pontos, descricao) in enumerate(resultados):
            valor = ciclo[i]
            print(f"{labels[i]}: {valor} {unidades[i]} | {classif} | {descricao}")
            pontuacao_ciclo     += pontos
            pontos_por_area[i]  += pontos
            somas[i]            += valor

        classificacao = classificar_ciclo(pontuacao_ciclo)
        recomendacao  = gerar_recomendacao(
            [(r[0], r[1]) for r in resultados], classificacao
        )

        print(f"\nPontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

        riscos_ciclos.append(pontuacao_ciclo)

    n      = len(dados_missao)
    medias = [somas[i] / n for i in range(5)]

    print()
    gerar_relatorio_final(riscos_ciclos, pontos_por_area, medias)


if __name__ == "__main__":
    main()
