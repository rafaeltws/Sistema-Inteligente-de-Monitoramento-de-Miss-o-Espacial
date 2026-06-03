# ============================================================
# MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Missão Espacial
# GS2026.1 - Pensamento Computacional e Automação com Python
# ============================================================

# Matriz principal: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [22, 95, 91, 98, 93],   # Ciclo 1 - Início da missão
    [26, 83, 75, 95, 87],   # Ciclo 2 - Estabilização dos sistemas
    [32, 61, 54, 90, 68],   # Ciclo 3 - Aquecimento e queda de sinal
    [37, 40, 35, 85, 52],   # Ciclo 4 - Alerta de energia e temperatura
    [41, 25, 17, 76, 33],   # Ciclo 5 - Risco operacional crítico
    [35, 52, 30, 80, 48],   # Ciclo 6 - Tentativa de recuperação
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


# ─────────────────────────────────────────────
# FUNÇÕES DE ANÁLISE POR SENSOR
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# FUNÇÕES DE CLASSIFICAÇÃO E ANÁLISE
# ─────────────────────────────────────────────

def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(alertas):
    acoes = [
        "Verificar controle térmico da missão.",
        "Tentar restabelecer contato com a base.",
        "Ativar modo de economia de energia.",
        "Acionar protocolo de suporte à vida.",
        "Reduzir operações não essenciais.",
    ]

    recomendacoes = []
    for i in range(len(alertas)):
        if alertas[i] == "CRÍTICO":
            recomendacoes.append(acoes[i])

    if len(recomendacoes) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif len(recomendacoes) > 0:
        return " ".join(recomendacoes)
    else:
        return "Monitorar sistemas em atenção e preparar plano de contingência."


def analisar_tendencia(risco_primeiro, risco_ultimo):
    if risco_ultimo > risco_primeiro:
        return "A missão apresentou tendência de piora."
    elif risco_ultimo < risco_primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area):
    maior_indice = 0
    for i in range(len(pontos_por_area)):
        if pontos_por_area[i] > pontos_por_area[maior_indice]:
            maior_indice = i
    return areas_monitoradas[maior_indice]


# ─────────────────────────────────────────────
# COLETA DE DADOS DO USUÁRIO
# ─────────────────────────────────────────────

print("=" * 60)
print("  MISSION CONTROL AI — CADASTRO DA MISSÃO")
print("=" * 60)

nome_missao = input("Digite o nome da missão: ")
while nome_missao == "":
    print("O nome da missão não pode ser vazio.")
    nome_missao = input("Digite o nome da missão: ")

nome_equipe = input("Digite o nome da equipe: ")
while nome_equipe == "":
    print("O nome da equipe não pode ser vazio.")
    nome_equipe = input("Digite o nome da equipe: ")

integrantes = []
print("\nCadastre os integrantes (mínimo 1, máximo 3).")

for i in range(1, 4):
    nome_int = input("Nome do integrante " + str(i) + " (Enter para pular): ")
    if nome_int == "":
        break
    rm = input("RM de " + nome_int + ": ")
    integrantes.append(nome_int + " - RM: " + rm)

if len(integrantes) == 0:
    integrantes.append("Integrante 1 - RM: 000000")


# ─────────────────────────────────────────────
# INÍCIO DO MONITORAMENTO
# ─────────────────────────────────────────────

print()
print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão: " + nome_missao)
print("Equipe: " + nome_equipe)
print("Integrantes:")
for integrante in integrantes:
    print("  " + integrante)
print("Quantidade de ciclos analisados: " + str(len(dados_missao)))
print("=" * 60)

riscos_ciclos   = []
pontos_por_area = [0, 0, 0, 0, 0]
soma_temp       = 0
soma_com        = 0
soma_bat        = 0
soma_oxi        = 0
soma_est        = 0

for numero_ciclo in range(len(dados_missao)):
    ciclo = dados_missao[numero_ciclo]

    temperatura  = ciclo[0]
    comunicacao  = ciclo[1]
    bateria      = ciclo[2]
    oxigenio     = ciclo[3]
    estabilidade = ciclo[4]

    class_temp, pont_temp, desc_temp = analisar_temperatura(temperatura)
    class_com,  pont_com,  desc_com  = analisar_comunicacao(comunicacao)
    class_bat,  pont_bat,  desc_bat  = analisar_bateria(bateria)
    class_oxi,  pont_oxi,  desc_oxi  = analisar_oxigenio(oxigenio)
    class_est,  pont_est,  desc_est  = analisar_estabilidade(estabilidade)

    pontuacao_ciclo = pont_temp + pont_com + pont_bat + pont_oxi + pont_est

    pontos_por_area[0] = pontos_por_area[0] + pont_temp
    pontos_por_area[1] = pontos_por_area[1] + pont_com
    pontos_por_area[2] = pontos_por_area[2] + pont_bat
    pontos_por_area[3] = pontos_por_area[3] + pont_oxi
    pontos_por_area[4] = pontos_por_area[4] + pont_est

    soma_temp = soma_temp + temperatura
    soma_com  = soma_com  + comunicacao
    soma_bat  = soma_bat  + bateria
    soma_oxi  = soma_oxi  + oxigenio
    soma_est  = soma_est  + estabilidade

    classificacao = classificar_ciclo(pontuacao_ciclo)
    alertas = [class_temp, class_com, class_bat, class_oxi, class_est]

    if classificacao == "MISSÃO ESTÁVEL":
        recomendacao = "Manter operação normal e continuar monitoramento."
    else:
        recomendacao = gerar_recomendacao(alertas)

    print()
    print("CICLO " + str(numero_ciclo + 1))
    print("-" * 60)
    print("Temperatura : " + str(temperatura) + " °C | " + class_temp + " | " + desc_temp)
    print("Comunicação : " + str(comunicacao) + "% | "  + class_com  + " | " + desc_com)
    print("Bateria     : " + str(bateria)      + "% | "  + class_bat  + " | " + desc_bat)
    print("Oxigênio    : " + str(oxigenio)     + "% | "  + class_oxi  + " | " + desc_oxi)
    print("Estabilidade: " + str(estabilidade) + "% | "  + class_est  + " | " + desc_est)
    print()
    print("Pontuação de risco do ciclo: " + str(pontuacao_ciclo))
    print("Classificação do ciclo: " + classificacao)
    print("Recomendação: " + recomendacao)

    riscos_ciclos.append(pontuacao_ciclo)


# ─────────────────────────────────────────────
# RELATÓRIO FINAL
# ─────────────────────────────────────────────

total_ciclos = len(dados_missao)

media_temp = soma_temp / total_ciclos
media_com  = soma_com  / total_ciclos
media_bat  = soma_bat  / total_ciclos
media_oxi  = soma_oxi  / total_ciclos
media_est  = soma_est  / total_ciclos

maior_risco    = riscos_ciclos[0]
ciclo_critico  = 1
for i in range(len(riscos_ciclos)):
    if riscos_ciclos[i] > maior_risco:
        maior_risco   = riscos_ciclos[i]
        ciclo_critico = i + 1

soma_riscos = 0
for risco in riscos_ciclos:
    soma_riscos = soma_riscos + risco
risco_medio = soma_riscos / total_ciclos

qtd_criticos = 0
for risco in riscos_ciclos:
    if risco >= 6:
        qtd_criticos = qtd_criticos + 1

tendencia    = analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1])
area_afetada = identificar_area_mais_afetada(pontos_por_area)
class_final  = classificar_ciclo(round(risco_medio))

print()
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)
print("Missão: " + nome_missao)
print("Equipe: " + nome_equipe)
print("Integrantes:")
for integrante in integrantes:
    print("  " + integrante)
print()
print("Quantidade de ciclos analisados: " + str(total_ciclos))
print()
print("Média de temperatura : " + str(round(media_temp, 2)) + " °C")
print("Média de comunicação : " + str(round(media_com,  2)) + "%")
print("Média de bateria     : " + str(round(media_bat,  2)) + "%")
print("Média de oxigênio    : " + str(round(media_oxi,  2)) + "%")
print("Média de estabilidade: " + str(round(media_est,  2)) + "%")
print()
print("Ciclo mais crítico      : Ciclo " + str(ciclo_critico))
print("Maior pontuação de risco: " + str(maior_risco))
print("Risco médio da missão   : " + str(round(risco_medio, 2)))
print("Quantidade de ciclos críticos: " + str(qtd_criticos))
print()
print("Tendência da missão:")
print(tendencia)
print()
print("Pontuação acumulada por área:")
for i in range(len(areas_monitoradas)):
    print("  " + areas_monitoradas[i] + ": " + str(pontos_por_area[i]) + " pontos")
print()
print("Área mais afetada:")
print("  " + area_afetada)
print()
print("Classificação final da missão:")
print("  " + class_final)
print()
print("Conclusão:")
if class_final == "MISSÃO ESTÁVEL":
    print("A missão transcorreu dentro dos parâmetros normais.")
    print("Todos os sistemas operaram de forma satisfatória.")
elif class_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidade durante a operação.")
    print("Ainda existem sistemas em atenção.")
    print("A equipe deve manter o plano de contingência ativo.")
else:
    print("A missão atingiu níveis críticos em múltiplos ciclos.")
    print("Recomenda-se revisão completa dos sistemas antes de nova operação.")
print("=" * 60)