"""
Script para gerar o relatório unificado do projeto de
Predição de Resistência do Concreto.

Entrada : "Predição de Resistência do Concreto.ipynb" + "SG_Site.png"
Saída   : "Relatorio_Predicao_Concreto.ipynb"

Uso:
    python gerar_relatorio.py
"""
import json
import uuid

INPUT_FILE = "Predição de Resistência do Concreto.ipynb"
OUTPUT_FILE = "Relatorio_Predicao_Concreto.ipynb"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Outputs originais (da única célula que existia)
outputs = nb["cells"][0]["outputs"]
# Ordem dos outputs:
#  [0] print cabeçalho, [1] tabela df.head, [2] df.info()
#  [3] heatmap, [4] print métricas, [5] scatter, [6] importâncias

# ============================================================
# CONTEÚDO MARKDOWN
# ============================================================

MD_HEADER = """<div align="center">
<img src="SG_Site.png" alt="Cabeçalho Silvânio Góis" width="100%"/>
</div>

# Previsão da Resistência à Compressão do Concreto com Machine Learning
### Otimização de Dosagem, Redução de Custos e Controle de Qualidade em Obras

**Autor:** Silvânio Góis — *Gestor de Operações e Negócios Orientado a Dados*  
**Contatos:** [Website](https://www.silvaniogois.com.br) | [LinkedIn](https://www.linkedin.com/in/silvanio-gois) | [GitHub](https://github.com/SilvanioSG) | **E-mail:** sg@silvaniogois.com.br

---

## 1. Visão Geral do Projeto e Objetivo de Negócio

No setor da construção civil, o **concreto** é o insumo estrutural mais consumido. A verificação da sua **resistência à compressão (MPa)** tradicionalmente exige o rompimento de corpos de prova em laboratório aos **28 dias de cura**.

Aguardar 28 dias para validar um traço de concreto gera atrasos no cronograma, custos com desforma e riscos operacionais graves caso o lote não atinja a resistência projetada.

### Objetivo

Desenvolver um modelo preditivo baseado em **Machine Learning (Random Forest Regressor)** capaz de estimar a resistência do concreto em MPa a partir do seu traço (proporções dos insumos) e idade de cura, permitindo:

- **Redução no consumo de cimento** sem perder segurança estrutural.
- **Antecipação de tomadas de decisão** no canteiro de obras.
- **Minimização de desperdícios e emissões de CO₂** no processo construtivo.

---

## 2. Estrutura dos Dados e Atributos Técnicos

A base de dados utilizada provém de ensaios laboratoriais reais e contempla os seguintes componentes (em kg/m³):

| Atributo | Variável no Código | Descrição na Engenharia Civil |
| :--- | :--- | :--- |
| **Cimento** | `cimento` | Aglomerante principal (maior custo financeiro e ambiental) |
| **Escória de Alto Forno** | `escoria` | Subproduto industrial que melhora a durabilidade |
| **Cinza Volante** | `cinza_volante` | Pozolana que substitui parte do cimento e melhora a trabalhabilidade |
| **Água** | `agua` | Regula a reação de hidratação e a relação Água/Cimento (a/c) |
| **Superplastificante** | `superplastificante` | Aditivo químico que reduz a necessidade de água mantendo a fluidez |
| **Agregado Graúdo** | `agregado_graudo` | Brita / Pedra |
| **Agregado Miúdo** | `agregado_miudo` | Areia |
| **Idade** | `idade` | Tempo de cura do concreto (em dias) |
| **Resistência** | `resistencia_compressao` | **Variável Alvo (Target)** — Resistência final em MPa |

---

## 3. Carregamento e Padronização do Dataset

Abaixo são apresentados o carregamento dos dados brutos e a padronização dos nomes das colunas para o português, permitindo uma leitura direta alinhada à terminologia da engenharia civil brasileira.
"""

MD_EXPLORATORY = """---

## 4. Análise Exploratória: Matriz de Correlação

O heatmap abaixo mapeia o grau de associação linear entre cada componente do traço e a resistência final em MPa.
"""

MD_CORRELATION_EXPLAIN = """### Interpretação da Matriz de Correlação

**Utilidade para a Engenharia e Gestão:**

- Identifica rapidamente que o **cimento**, a **idade de cura** e o **superplastificante** possuem correlação positiva direta com a resistência.
- Evidencia o impacto negativo do excesso de **água** na resistência (princípio fundamental da relação água/cimento de Abrams).

**Benefício para a Construção Civil:**

- **Tomada de Decisão na Mistura:** Permite ao gestor de laboratório ou usina de concreto identificar quais aditivos priorizar para substituir o cimento mantendo o desempenho.
"""

MD_MODELING = """---

## 5. Preparação dos Dados e Treinamento do Modelo

Para a modelagem, os dados são divididos em **80% para treino** e **20% para teste**, garantindo que o modelo seja avaliado em amostras nunca vistas durante o aprendizado (validação honesta).

O algoritmo escolhido é o **Random Forest Regressor**, um modelo de ensemble baseado em múltiplas árvores de decisão que se destaca por:

- Robustez frente a relações não-lineares entre insumos e resistência.
- Resistência a *overfitting* (sobreajuste).
- Capacidade de fornecer a **importância relativa de cada variável**.
"""

MD_METRICS = """---

## 6. Métricas de Desempenho do Modelo (R² e RMSE)

Abaixo estão os resultados da avaliação do modelo na base de teste, comparando as previsões com os ensaios reais de laboratório.
"""

MD_METRICS_EXPLAIN = """### Interpretação das Métricas

- **R² = 0,8841:** Indica que o modelo explica **mais de 88% da variação** da resistência do concreto apenas com a proporção dos ingredientes e o tempo de cura.
- **RMSE ≈ 5,46 MPa:** Mostra que o erro médio das previsões é de aproximadamente 5,5 MPa, uma margem excelente para modelos de materiais heterogêneos.

**Benefício para a Construção Civil:**

- **Segurança Estrutural:** Fornece um indicador confiável para pré-dimensionamento de traços antes da mistura física, reduzindo a necessidade de testes exaustivos por tentativa e erro.
"""

MD_VALIDATION = """---

## 7. Validação Técnica: Resistência Real vs. Predição

O gráfico de dispersão abaixo relaciona a resistência real medida em laboratório (eixo X) com a resistência predita pelo modelo (eixo Y). A linha vermelha tracejada representa a **perfeição (y = x)**.
"""

MD_VALIDATION_EXPLAIN = """### Interpretação do Gráfico de Validação

- Pontos próximos à linha vermelha tracejada indicam alta precisão.
- Permite identificar se o modelo apresenta viés de subestimar ou superestimar a resistência em faixas específicas (ex: concretos de altíssimo desempenho > 60 MPa).

**Benefício para a Construção Civil:**

- **Redução de Riscos Operacionais:** Facilita a definição de um coeficiente de segurança preditivo no planejamento da desforma de lajes e pilares.
"""

MD_IMPORTANCE = """---

## 8. Importância das Variáveis (Feature Importance)

O gráfico abaixo classifica quais insumos e fatores exercem maior peso no resultado final da resistência do concreto, segundo o modelo treinado.
"""

MD_IMPORTANCE_EXPLAIN = """### Interpretação da Importância das Variáveis

**Utilidade para a Engenharia e Gestão:**

- Revela empiricamente que a **idade de cura** e a quantidade de **cimento** dominam a capacidade preditiva, seguidas da proporção de **água** e **superplastificantes**.

**Benefício para a Construção Civil:**

- **Otimização Financeira e ESG:** Direciona a equipe de suprimentos e P&D na negociação de aditivos superplastificantes e adições minerais (como cinzas e escória), reduzindo o custo por m³ sem comprometer a qualidade final.
"""

MD_IMPACT = """---

## 9. Impacto Estratégico e Retorno sobre o Investimento (ROI)

Ao aplicar esta solução de Data Science no controle de qualidade de usinas de concreto e construtoras, obtém-se:

1. **Aceleração de Cronograma:** Previsão do ganho de resistência em idades jovens (3 e 7 dias), antecipando a desforma segura e liberando escoramentos.
2. **Economia Financeira:** Otimização dos traços para evitar o consumo excessivo de cimento (superdimensionamento preventivo).
3. **Sustentabilidade (ESG):** Menor consumo de clínquer por metro cúbico, reduzindo diretamente a pegada de carbono da empresa.

---

## 10. Conclusão

O modelo desenvolvido demonstra que é possível **prever a resistência do concreto com alta confiabilidade** (R² ≈ 0,88) a partir apenas do traço e da idade de cura. Esta solução tem potencial para transformar a gestão de qualidade na construção civil, permitindo decisões mais rápidas, econômicas e sustentáveis.

---

<div align="center">

**Silvânio Góis**  
*Gestor de Operações e Negócios Orientado a Dados*

[Website](https://www.silvaniogois.com.br) | [LinkedIn](https://www.linkedin.com/in/silvanio-gois) | [GitHub](https://github.com/SilvanioSG) | sg@silvaniogois.com.br

</div>
"""

# ============================================================
# CONTEÚDO DAS CÉLULAS DE CÓDIGO (ficarão ocultas)
# ============================================================

CODE_LOAD = """# 1. Importação das Bibliotecas Necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Configuração visual dos gráficos
sns.set_theme(style="whitegrid")

# 2. Carregamento e Padronização do Dataset
url = "https://raw.githubusercontent.com/stedy/Machine-Learning-With-R-Datasets/master/concrete.csv"
df = pd.read_csv(url)

# Renomeando as colunas para o português
df.columns = [
    'cimento', 'escoria', 'cinza_volante', 'agua', 
    'superplastificante', 'agregado_graudo', 'agregado_miudo', 
    'idade', 'resistencia_compressao'
]

print("--- Primeiras 5 linhas do Dataset ---")
display(df.head())

print("\\n--- Informações Gerais do Dataset ---")
df.info()"""

CODE_HEATMAP = """# 3. Análise Exploratória: Matriz de Correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="Blues", fmt=".2f")
plt.title("Matriz de Correlação - Fatores x Resistência do Concreto (MPa)")
plt.show()"""

CODE_TRAIN = """# 4. Preparação dos Dados para o Machine Learning
X = df.drop(columns=['resistencia_compressao'])
y = df['resistencia_compressao']

# Divisão em bases de Treino (80%) e Teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Treinamento do Modelo (Random Forest Regressor)
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)"""

CODE_METRICS = """# 6. Previsão e Avaliação de Desempenho
y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\\n--- Resultados de Desempenho do Modelo ---")
print(f"• RMSE (Erro Quadrático Médio): {rmse:.2f} MPa")
print(f"• R² Score (Precisão do Modelo): {r2:.4f} ({r2*100:.1f}%)")"""

CODE_SCATTER = """# 7. Gráfico de Validação: Real vs. Predito
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='teal')
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r', linewidth=2)
plt.xlabel("Resistência Real em Laboratório (MPa)")
plt.ylabel("Resistência Predita pelo Modelo (MPa)")
plt.title("Validação Técnica: Resistência Real vs. Predição")
plt.show()"""

CODE_IMPORTANCE = """# 8. Gráfico de Importância das Variáveis (Feature Importance)
importancias = pd.Series(modelo.feature_importances_, index=X.columns).sort_values(ascending=False)

plt.figure(figsize=(10, 5))
importancias.plot(kind='bar', color='cornflowerblue')
plt.title("Grau de Importância dos Insumos na Resistência Final")
plt.ylabel("Peso Relativo no Modelo")
plt.show()"""

# ============================================================
# HELPERS
# ============================================================

def make_md(content):
    return {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": content,
    }

def make_code(content, outs=None, exec_count=None):
    return {
        "cell_type": "code",
        "execution_count": exec_count,
        "id": str(uuid.uuid4())[:8],
        "metadata": {
            "jupyter": {"source_hidden": True},
            "tags": ["hide-input"],
        },
        "outputs": outs if outs is not None else [],
        "source": content,
    }

# ============================================================
# MONTAGEM DO NOTEBOOK FINAL
# ============================================================

new_cells = [
    make_md(MD_HEADER),
    make_code(CODE_LOAD,     [outputs[0], outputs[1], outputs[2]], 1),
    make_md(MD_EXPLORATORY),
    make_code(CODE_HEATMAP,  [outputs[3]], 2),
    make_md(MD_CORRELATION_EXPLAIN),
    make_md(MD_MODELING),
    make_code(CODE_TRAIN,    [], 3),
    make_md(MD_METRICS),
    make_code(CODE_METRICS,  [outputs[4]], 4),
    make_md(MD_METRICS_EXPLAIN),
    make_md(MD_VALIDATION),
    make_code(CODE_SCATTER,  [outputs[5]], 5),
    make_md(MD_VALIDATION_EXPLAIN),
    make_md(MD_IMPORTANCE),
    make_code(CODE_IMPORTANCE, [outputs[6]], 6),
    make_md(MD_IMPORTANCE_EXPLAIN),
    make_md(MD_IMPACT),
]

nb["cells"] = new_cells

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"✅ Notebook gerado com sucesso: {OUTPUT_FILE}")
print(f"📊 Total de células: {len(new_cells)}")
print(f"🖼️  Outputs preservados: {sum(len(c.get('outputs', [])) for c in new_cells)}")