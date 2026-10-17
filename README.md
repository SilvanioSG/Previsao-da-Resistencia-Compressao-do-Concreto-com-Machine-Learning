<div align="center">
  <img src="SG_Site.png" alt="Silvânio Góis" width="720"/>
</div>

<h1 align="center">Previsão da Resistência à Compressão do Concreto com Machine Learning</h1>
<h3 align="center">Otimização de dosagem, redução de custos e controle de qualidade em obras</h3>

<p align="center">
  <a href="https://silvaniogois.github.io/predicao-resistencia-concreto/"><img src="https://img.shields.io/badge/Apresentação-Ver%20slides-ff7b00?style=for-the-badge&logo=html5&logoColor=white" alt="Slides"></a>
  <a href="https://silvaniogois.github.io/predicao-resistencia-concreto/relatorio.html"><img src="https://img.shields.io/badge/Relatório-Completo-14375c?style=for-the-badge&logo=jupyter&logoColor=white" alt="Relatório"></a>
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="sklearn">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <b>Autor:</b> Silvânio Góis — <i>Gestor de Operações e Negócios Orientado a Dados</i><br>
  <a href="https://www.silvaniogois.com.br">Website</a> ·
  <a href="https://www.linkedin.com/in/silvanio-gois">LinkedIn</a> ·
  <a href="https://github.com/SilvanioSG">GitHub</a> ·
  <a href="mailto:sg@silvaniogois.com.br">E-mail</a>
</p>

---

## Índice

- [Visão Geral](#-visão-geral)
- [O Problema](#-o-problema)
- [A Solução](#-a-solução)
- [Origem e Dicionário dos Dados](#-origem-e-dicionário-dos-dados)
- [Metodologia](#-metodologia)
- [Resultados](#-resultados)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Reproduzir](#-como-reproduzir)
- [Perguntas Frequentes (Q&A)](#-perguntas-frequentes-qa)
- [Impacto Estratégico](#-impacto-estratégico)
- [Licença e Citação](#-licença-e-citação)

---

## Visão Geral

Este projeto aplica **Machine Learning** para prever a resistência à compressão do concreto (em MPa) a partir apenas do seu traço e tempo de cura — permitindo que construtoras e usinas **antecipem decisões críticas em segundos**, em vez dos tradicionais 28 dias de rompimento laboratorial.

**Resultado alcançado:** modelo Random Forest com **R² = 0,8841** e **RMSE = 5,46 MPa**, demonstrando que é possível prever a resistência com alta confiabilidade apenas com dados de composição.

---

## O Problema

Na construção civil, validar um traço de concreto exige **28 dias de cura** até o rompimento do corpo de prova. Este atraso gera:

| Dor | Consequência |
|-----|--------------|
| Atraso na desforma | Cronograma travado, escoramentos ocupados |
| Custos com retrabalho | Se o lote não atinge a resistência projetada |
| Riscos operacionais | Estruturas liberadas antes do tempo seguro |
| Desperdício de cimento | Superdimensionamento preventivo por incerteza |

---

## A Solução

Modelo preditivo de **Random Forest Regressor** que estima a resistência em MPa a partir de 8 features (componentes do traço + idade de cura), com as seguintes entregas:

- **Redução no consumo de cimento** sem perda de segurança estrutural
- **Antecipação de decisões** no canteiro de obras
- **Minimização de desperdícios** e emissões de CO₂
- **Previsão em segundos** vs. 28 dias de espera

---

## Origem e Dicionário dos Dados

### Fonte oficial

- **Dataset:** *Concrete Compressive Strength*
- **Autor original:** I-Cheng Yeh (1998) — *Cement and Concrete Research*, 28(12), 1797-1808
- **Repositório primário:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)
- **DOI:** [10.24432/C5PK67](https://doi.org/10.24432/C5PK67)
- **Mirror usado no código:** [stedy/Machine-Learning-With-R-Datasets](https://raw.githubusercontent.com/stedy/Machine-Learning-With-R-Datasets/master/concrete.csv)
- **Volume:** 1.030 amostras · 9 atributos · **sem valores nulos**

### Dicionário de atributos (em kg/m³, exceto onde indicado)

| Atributo | Variável no código | Faixa típica | Descrição na Engenharia Civil |
|----------|-------------------|--------------|-------------------------------|
| Cimento | `cimento` | 102–540 | Aglomerante principal (maior custo) |
| Escória de Alto Forno | `escoria` | 0–360 | Subproduto que melhora durabilidade |
| Cinza Volante | `cinza_volante` | 0–200 | Pozolana que substitui parte do cimento |
| Água | `agua` | 121–247 | Regula a relação a/c (Abrams) |
| Superplastificante | `superplastificante` | 0–32 | Aditivo que reduz a necessidade de água |
| Agregado Graúdo | `agregado_graudo` | 801–1145 | Brita / pedra |
| Agregado Miúdo | `agregado_miudo` | 594–992 | Areia |
| Idade | `idade` (dias) | 1–365 | Tempo de cura |
| **Resistência** | `resistencia_compressao` (MPa) | 2,3–82,6 | **Variável-alvo (target)** |

---

## Metodologia

```
┌─────────────────────┐
│  1. Carregamento    │  concrete.csv (UCI)
│     e padronização  │  Colunas em PT-BR
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  2. Análise         │  Heatmap de correlação
│     Exploratória    │  Identificação de padrões
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  3. Split 80/20     │  Validação honesta
│     Treino/Teste    │  random_state=42
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  4. Random Forest   │  n_estimators=100
│     Regressor       │  Robustez a não-linearidades
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  5. Avaliação       │  R², RMSE
│     e Interpretação │  Feature Importance
└─────────────────────┘
```

**Por que Random Forest?**
- Robusto a relações não-lineares entre insumos e resistência
- Resistente a *overfitting* (múltiplas árvores)
- Fornece **importância das variáveis** (interpretabilidade)
- Excelente para materiais heterogêneos como o concreto

---

## Resultados

### Métricas na base de teste (206 amostras não vistas)

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **R² Score** | **0,8841** | Explica 88,4% da variação da resistência |
| **RMSE** | **5,46 MPa** | Erro médio de ~5,5 MPa por previsão |
| **MSE** | 29,8 MPa² | Erro quadrático médio |

### Principais insights

- **Cimento** e **idade de cura** são as variáveis dominantes no modelo
- **Água** apresenta correlação negativa com a resistência (princípio de Abrams)
- **Superplastificante** tem efeito positivo moderado
- **Escória e cinza volante** atuam como substitutos parciais do cimento

### Visualizações

- Matriz de correlação (heatmap)
- Validação real vs. predito (scatter)
- Importância das variáveis (bar chart)

> A visualização está disponível na [apresentação]([https://silvaniogois.github.io/predicao-resistencia-concreto/](https://silvaniosg.github.io/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning/)).

---

## Estrutura do Repositório

```
predicao-resistencia-concreto/
├── README.md                              # este arquivo
├── LICENSE                                # MIT
├── requirements.txt                       # dependências Python
├── .gitignore
│
├── SG_Site.png                            # logo do autor
│
├── Predição de Resistência do Concreto.ipynb    # notebook original (com código)
├── Relatorio_Predicao_Concreto.ipynb            # notebook unificado (código oculto)
│
├── apresentacao_concreto.html             # slides Reveal.js
├── relatorio_concreto.html                # relatório HTML (nbconvert --no-input)
│
├── gerar_relatorio.py                     # gera o notebook unificado
├── gerar_slides.py                        # gera a apresentação HTML
│
├── data/
│   └── concrete.csv                       # https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set
│
└── docs/                                  # GitHub Pages
    ├── index.html                         # apresentação (raiz do Pages)
    └── relatorio.html                     # relatório completo
```

---

## Como Reproduzir

### 1. Clonar o repositório

```bash
git clone https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning.git
cd Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning
```

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
# ou .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

### 3. Executar o notebook

```bash
jupyter notebook "Predição de Resistência do Concreto.ipynb"
```

### 4. Regerar os artefatos de apresentação (opcional)

```bash
# Gera o notebook unificado com markdown + código oculto
python gerar_relatorio.py

# Gera a apresentação Reveal.js auto-contida
python gerar_slides.py

# Exporta o relatório para HTML limpo (sem código)
jupyter nbconvert --to html --no-input Relatorio_Predicao_Concreto.ipynb \
    --output-dir docs --output relatorio.html
```

### 5. Visualizar a apresentação

Abra `apresentacao_concreto.html` no navegador, **ou** publique com GitHub Pages (ver abaixo).

---

## Deploy no GitHub Pages

1. Vá em **Settings → Pages**
2. Em **Source**, selecione: `Deploy from a branch`
3. **Branch:** `main` · **Folder:** `/docs`
4. Salve — aguarde ~1 minuto
5. URL final: `Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning`

---

## Perguntas Frequentes (Q&A)

### Técnicas

<details>
<summary><b>1. Por que Random Forest e não Redes Neurais?</b></summary>

Random Forest foi escolhido por três razões práticas: **(a)** funciona bem com datasets pequenos (1.030 amostras — pouco para redes neurais), **(b)** é robusto a overfitting sem necessidade de tuning extensivo, e **(c)** fornece `feature_importance` nativa — crucial para o valor de negócio (entender o que pesa na resistência). Redes Neurais só se justificariam com muito mais dados ou séries temporais complexas.
</details>

<details>
<summary><b>2. Por que R² e RMSE como métricas principais?</b></summary>

- **R²** responde a pergunta de negócio: *"quanto da variação da resistência o modelo explica?"* — 88,4% é excelente para material heterogêneo.
- **RMSE** responde a pergunta de engenharia: *"qual o erro médio em MPa?"* — 5,46 MPa está na mesma unidade da variável-alvo, permitindo dimensionar coeficientes de segurança.

Um terceiro indicador (MAE) poderia complementar, mas os dois acima cobrem bem tanto a perspectiva estatística quanto a técnica.
</details>

<details>
<summary><b>3. O modelo pode extrapolar para traços fora do dataset?</b></summary>

**Não com segurança.** Random Forest **não extrapola** — ele interpola entre os padrões vistos no treino. Se você fornecer um traço com valores muito fora das faixas do dataset original (ex: cimento acima de 540 kg/m³), a previsão tende a ser imprecisa ou enviesada para o valor mais próximo visto. Para traços inéditos, recomenda-se retreinar com amostras adicionais.
</details>

<details>
<summary><b>4. Por que split 80/20 e não validação cruzada?</b></summary>

O split 80/20 foi escolhido por **simplicidade e reprodutibilidade** (`random_state=42` garante resultado idêntico). Cross-validation (k-fold) daria estimativa mais robusta do desempenho geral, mas para um projeto de portfólio com dataset pequeno, 80/20 já é suficiente para demonstrar capacidade preditiva. Como evolução futura, recomenda-se `cross_val_score` com k=5.
</details>

<details>
<summary><b>5. Como atualizar o modelo com novos dados de obra?</b></summary>

O modelo pode ser retreinado adicionando as novas amostras ao `concrete.csv` e rodando novamente o notebook. Como o Random Forest é não-paramétrico, cada retreino incorpora os novos padrões automaticamente. Para produção contínua, o ideal seria uma pipeline MLOps (ex: retreino mensal com validação automática) — mas isso está fora do escopo deste case.
</details>

### De Engenharia Civil

<details>
<summary><b>6. O modelo substitui o ensaio de rompimento em laboratório?</b></summary>

**Não.** O modelo é uma **ferramenta de pré-dimensionamento e antecipação de decisão**, não um substituto do controle tecnológico normativo (NBR 5739). Ele permite: prever resistência antes da concretagem, otimizar traços antes de produzi-los, e antecipar ganhos em idades jovens (3 e 7 dias) para planejar desforma. A validação por corpo de prova continua sendo obrigatória por norma.
</details>

<details>
<summary><b>7. Qual é a margem de segurança recomendada ao usar as previsões?</b></summary>

Com RMSE = 5,46 MPa, recomenda-se aplicar um **coeficiente de segurança preditivo** entre 5 e 8 MPa sobre a resistência de projeto (fk), dependendo do nível de responsabilidade estrutural. Para estruturas críticas, o ideal é trabalhar com o **intervalo de confiança inferior** da previsão — o que exigiria uma versão aprimorada do modelo com quantile regression ou bootstrap de resíduos.
</details>

<details>
<summary><b>8. Por que 28 dias é referência?</b></summary>

28 dias é o tempo convencional estabelecido por normas internacionais (ASTM C39, NBR 5739) porque, em condições normais de cura, o concreto atinge cerca de **99% da resistência final** nesse período. Nos primeiros 7 dias, a resistência já chega a ~70%, o que permite desforma controlada — e é exatamente aí que o modelo agrega mais valor.
</details>

<details>
<summary><b>9. O modelo funciona para concretos de alto desempenho (>60 MPa)?</b></summary>

Parcialmente. O dataset original contém alguns exemplos nessa faixa, mas a **dispersão do erro aumenta** para valores extremos (visível no gráfico real vs. predito). Para concretos de altíssimo desempenho (fck > 60 MPa), recomenda-se retreinar com uma base específica (ex: HPC datasets) ou aplicar coeficientes de segurança maiores.
</details>

<details>
<summary><b>10. Quais os principais benefícios ESG que o modelo habilita?</b></summary>

O cimento responde por ~7% das emissões globais de CO₂. Otimizar traços com substituição parcial por escória e cinza volante (subprodutos industriais) reduz o consumo de clínquer por m³. O modelo permite **testar virtualmente dezenas de combinações** antes de produzir fisicamente — economizando tanto cimento quanto o custo energético dos ensaios laboratoriais.
</details>

### De Negócio

<details>
<summary><b>11. Como medir o ROI desta solução numa construtora?</b></summary>

Três alavancas mensuráveis:
1. **Economia de cimento:** cada 10 kg/m³ economizados representam R$ 5–10/m³ de concreto.
2. **Redução de dias de escoramento:** antecipar desforma em 2–3 dias por laje impacta diretamente o cronograma.
3. **Redução de retrabalho:** evitar lotes fora de especificação (custo médio de R$ 20–50 mil por evento).

Em uma obra de médio porte (5.000 m³), a economia conservadora estimada fica entre **R$ 150 mil e R$ 400 mil** ao longo do projeto.
</details>

<details>
<summary><b>12. Por que não usar apenas uma planilha Excel em vez de ML?</b></summary>

Excel funciona para **fórmulas conhecidas** (ex: relação a/c de Abrams). Mas a resistência do concreto depende de **8 variáveis com interações não-lineares** — impossível de modelar em fórmulas simples. O ML captura essas interações automaticamente. Além disso, uma planilha não fornece *feature importance*, não se atualiza com novos dados, e não escala para múltiplos traços simultâneos.
</details>

---

## Impacto Estratégico

| Alavanca | Benefício |
|----------|-----------|
| **Cronograma** | Previsão em idades jovens → desforma segura antecipada |
| **Financeiro** | Otimização de traços → economia de cimento por m³ |
| **ESG** | Menor consumo de clínquer → pegada de carbono reduzida |
| **Qualidade** | Pré-dimensionamento confiável → menos retrabalho |

---

## Citação

Se você usar este projeto em pesquisa ou trabalho derivado, cite o dataset original:

```bibtex
@misc{yeh_concrete_1998,
  author    = {Yeh, I-Cheng},
  title     = {Concrete Compressive Strength},
  year      = {1998},
  publisher = {UCI Machine Learning Repository},
  doi       = {10.24432/C5PK67},
  url       = {https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength}
}
```

---

## Licença

Este projeto está licenciado sob a **MIT License** — veja [LICENSE](LICENSE) para detalhes. O dataset original segue a licença **CC BY 4.0** do UCI Machine Learning Repository.

---

<div align="center">

**Silvânio Góis**  
*Gestor de Operações e Negócios Orientado a Dados*

[Website](https://www.silvaniogois.com.br) · [LinkedIn](https://www.linkedin.com/in/silvanio-gois) · [GitHub](https://github.com/SilvanioSG) · sg@silvaniogois.com.br

</div>
