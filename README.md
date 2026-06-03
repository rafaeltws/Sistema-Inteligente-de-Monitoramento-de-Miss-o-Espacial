# 🚀 Mission Control AI

**Sistema Inteligente de Monitoramento de Missão Espacial**  
GS2026.1 — Pensamento Computacional e Automação com Python — FIAP

---

## 📋 Descrição

O **Mission Control AI** simula o monitoramento de uma missão espacial experimental, analisando 6 ciclos de operação com base em 5 sensores: temperatura, comunicação, bateria, oxigênio e estabilidade. O sistema classifica cada ciclo, calcula o risco acumulado, identifica tendências e gera um relatório final automaticamente.

---

## 📁 Estrutura do repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## ▶️ Como executar

Basta ter Python 3 instalado. Nenhuma biblioteca externa é necessária.

```bash
python mission_control.py
```

---

## 🛰️ Dados da missão simulada

| Ciclo | Descrição                    | Temperatura | Comunicação | Bateria | Oxigênio | Estabilidade |
|-------|------------------------------|-------------|-------------|---------|----------|--------------|
| 1     | Início da missão             | 22 °C       | 95%         | 91%     | 98%      | 93%          |
| 2     | Estabilização dos sistemas   | 26 °C       | 83%         | 75%     | 95%      | 87%          |
| 3     | Aquecimento e queda de sinal | 32 °C       | 61%         | 54%     | 90%      | 68%          |
| 4     | Alerta de energia            | 37 °C       | 40%         | 35%     | 85%      | 52%          |
| 5     | Risco operacional crítico    | 41 °C       | 25%         | 17%     | 76%      | 33%          |
| 6     | Tentativa de recuperação     | 35 °C       | 52%         | 30%     | 80%      | 48%          |

---

## 📐 Regras de alerta

### Temperatura (°C)
| Condição           | Classificação |
|--------------------|---------------|
| < 18               | ATENÇÃO       |
| 18 a 30            | NORMAL        |
| > 30 até 35        | ATENÇÃO       |
| > 35               | CRÍTICO       |

### Comunicação (%)
| Condição     | Classificação |
|--------------|---------------|
| < 30         | CRÍTICO       |
| 30 a 59      | ATENÇÃO       |
| ≥ 60         | NORMAL        |

### Bateria (%)
| Condição     | Classificação |
|--------------|---------------|
| < 20         | CRÍTICO       |
| 20 a 49      | ATENÇÃO       |
| ≥ 50         | NORMAL        |

### Oxigênio (%)
| Condição     | Classificação |
|--------------|---------------|
| < 80         | CRÍTICO       |
| 80 a 89      | ATENÇÃO       |
| ≥ 90         | NORMAL        |

### Estabilidade (%)
| Condição     | Classificação |
|--------------|---------------|
| < 40         | CRÍTICO       |
| 40 a 69      | ATENÇÃO       |
| ≥ 70         | NORMAL        |

---

## 🔢 Pontuação de risco

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENÇÃO       | 1      |
| CRÍTICO       | 2      |

Pontuação máxima por ciclo: **10 pontos** (5 sensores × 2).

---

## 🏷️ Classificação do ciclo

| Pontuação | Classificação       |
|-----------|---------------------|
| 0 – 2     | MISSÃO ESTÁVEL      |
| 3 – 5     | MISSÃO EM ATENÇÃO   |
| 6 – 10    | MISSÃO CRÍTICA      |

---

## 🔧 Funções implementadas

| Função                         | Descrição                                              |
|--------------------------------|--------------------------------------------------------|
| `analisar_temperatura()`       | Classifica a temperatura e retorna pontuação           |
| `analisar_comunicacao()`       | Classifica o sinal de comunicação                      |
| `analisar_bateria()`           | Classifica o nível de bateria                          |
| `analisar_oxigenio()`          | Classifica o nível de oxigênio                         |
| `analisar_estabilidade()`      | Classifica a estabilidade operacional                  |
| `analisar_ciclo()`             | Agrega a análise dos 5 sensores de um ciclo            |
| `classificar_ciclo()`          | Determina a classificação do ciclo pela pontuação      |
| `gerar_recomendacao()`         | Gera recomendação automática com base nos alertas      |
| `analisar_tendencia()`         | Compara risco do 1º e último ciclo                     |
| `identificar_area_mais_afetada()` | Retorna a área com maior pontuação acumulada        |
| `gerar_relatorio_final()`      | Exibe o relatório consolidado no terminal              |

---

## 👥 Equipe

- **Rafael Sá** RM569223  
- **João Melo** RM571116
-  **Gabriel Souza** RM571583
