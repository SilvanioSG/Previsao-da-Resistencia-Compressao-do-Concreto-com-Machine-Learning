 <div align="center">
  <img src="SG_Site.png" alt="Silvânio Góis — Gestão de Operações e Negócios Orientada a Dados" width="40%"/>
</div>

# Previsão da Resistência à Compressão do Concreto com Machine Learning

### Otimização de Dosagem, Redução de Custos e Controle de Qualidade em Obras

**Autor:** Silvânio Góis — Gestor de Operações e Negócios Orientado a Dados

**Contatos:** [Website](https://www.silvaniogois.com.br) · [LinkedIn](https://www.linkedin.com/in/silvanio-gois) · [GitHub](https://github.com/SilvanioSG) · [E-mail](mailto:sg@silvaniogois.com.br)

---

## Acesso Rápido

| Recurso | Link |
| :--- | :--- |
| Relatório online (GitHub Pages) | [Acessar relatório](https://silvaniosg.github.io/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning/) |
| Repositório no GitHub | [Acessar repositório](https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning) |
| Relatório em PDF | [`Relatorio_Predicao_Concreto.pdf`](https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning/blob/main/Relatorio_Predicao_Concreto.pdf) |
| Notebook executado | [`Relatorio_Predicao_Concreto.ipynb`](https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning/blob/main/Relatorio_Predicao_Concreto.ipynb) |
| Script gerador do notebook | [`gerar_relatorio.py`](https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning/blob/main/gerar_relatorio.py) |

---

## 1. Contexto de Negócio

No setor da construção civil, o concreto é um dos principais insumos estruturais. A verificação de sua resistência à compressão, expressa em megapascals (MPa), tradicionalmente envolve ensaios laboratoriais com corpos de prova em diferentes idades de cura, frequentemente aos 28 dias. Esse processo pode aumentar o tempo de tomada de decisão, gerar custos operacionais e dificultar o planejamento de atividades dependentes da resistência do material.

Este projeto aplica técnicas de Machine Learning para estimar a resistência à compressão do concreto com base nas proporções dos materiais utilizados na mistura e na idade de cura. A proposta é substituir parte da análise baseada exclusivamente em experimentação por uma abordagem orientada a dados, capaz de apoiar decisões de engenharia, planejamento e controle de qualidade.

### Inteligência Aplicada ao Negócio

- **Aceleração do cronograma:** estimativa da evolução da resistência em idades iniciais, como 3 e 7 dias, para apoiar o planejamento de desforma e escoramento, sempre condicionada à validação técnica e às normas aplicáveis.
- **Eficiência financeira:** análise de dosagens para investigar oportunidades de redução do consumo de cimento e evitar formulações excessivamente conservadoras.
- **Sustentabilidade (ESG):** avaliação de alternativas com menor consumo de materiais cimentícios e potencial redução das emissões associadas à produção do concreto.
- **Controle de qualidade preditivo:** utilização de modelos estatísticos para estimar a resistência e apoiar a identificação de misturas com desempenho potencialmente inadequado.

---

## 2. Origem dos Dados

A base utilizada provém do UCI Machine Learning Repository e corresponde ao conjunto de dados *Concrete Compressive Strength Dataset*, disponibilizado publicamente por I-Cheng Yeh, do Department of Information Management da Chung-Hua University.

O conjunto foi apresentado originalmente no artigo científico:

> YEH, I-Cheng. *Modeling of strength of high-performance concrete using artificial neural networks.* Cement and Concrete Research, v. 28, n. 12, p. 1797–1808, 1998.

**Características da base:**

- **Acesso aos dados:** "https://raw.githubusercontent.com/stedy/Machine-Learning-With-R-Datasets/master/concrete.csv"
- **Volume:** 1.030 amostras de ensaios laboratoriais.
- **Variáveis de entrada:** cimento, escória de alto-forno, cinza volante, água, superplastificante, agregado graúdo, agregado miúdo e idade de cura.
- **Unidades:** os componentes da mistura são expressos em kg/m³ e a idade em dias.
- **Variável-alvo:** resistência à compressão, expressa em MPa.

A utilização de uma base pública permite reproduzir os experimentos e comparar os resultados obtidos com outras abordagens de modelagem.

---

## 3. Engenharia de Features

Além dos oito atributos originais, foram construídas oito variáveis derivadas para representar relações entre os componentes da mistura e características relevantes para a resistência do concreto.

Essa etapa, conhecida como *Feature Engineering*, incorpora conhecimento do domínio ao processo de modelagem e permite investigar relações que não estão explicitamente representadas nas variáveis originais.

| Feature derivada | Fórmula | Justificativa técnica |
| :--- | :--- | :--- |
| `relacao_ac` | Água / cimento | Representa a relação água/cimento, associada à resistência do concreto conforme a Lei de Abrams. |
| `total_ligante` | Cimento + escória + cinza volante | Representa a quantidade total dos materiais cimentícios considerados. |
| `relacao_agua_ligante` | Água / total_ligante | Expressa a relação entre água e materiais cimentícios totais. |
| `total_agregado` | Agregado graúdo + agregado miúdo | Representa a massa total de agregados na mistura. |
| `prop_escoria` | Escória / total_ligante | Expressa a participação da escória na composição dos materiais cimentícios. |
| `prop_cinza` | Cinza volante / total_ligante | Expressa a participação da cinza volante na composição dos materiais cimentícios. |
| `sp_por_ligante` | Superplastificante / total_ligante | Representa a dosagem relativa do aditivo em relação aos materiais cimentícios. |
| `log_idade` | ln(1 + idade) | Transforma a idade de cura para representar possíveis relações não lineares com a resistência. |

As variáveis derivadas ampliam a representação dos dados e ajudam os algoritmos a identificar padrões relevantes para a previsão. Sua contribuição efetiva deve ser avaliada por meio dos resultados experimentais, e não presumida apenas pela justificativa técnica.

---

## 4. Metodologia — Como o Teste Foi Realizado

O desenvolvimento seguiu um pipeline de Machine Learning estruturado para avaliar o desempenho preditivo, comparar algoritmos e reduzir a dependência de uma única divisão dos dados.

### Etapas do pipeline

1. **Divisão entre treino e teste (80/20):** separação dos dados para treinamento e avaliação final em amostras não utilizadas no ajuste dos modelos.
2. **Validação cruzada K-Fold (5 folds):** avaliação do comportamento dos algoritmos em diferentes partições dos dados, permitindo analisar a estabilidade dos resultados.
3. **Otimização de hiperparâmetros:** utilização do `RandomizedSearchCV` para pesquisar combinações de parâmetros, com 30 combinações avaliadas e validação cruzada de cinco folds.
4. **Comparação de algoritmos:** avaliação de modelos baseados em árvores e métodos de boosting, considerando suas métricas de desempenho.
5. **Ensemble por Stacking:** combinação das previsões de modelos-base por meio de um modelo de nível superior, utilizando regressão Ridge como meta-modelo.

### Modelos Avaliados

- **Random Forest Regressor:** modelo de referência e versão com hiperparâmetros otimizados.
- **Gradient Boosting Regressor:** algoritmo de boosting baseado em árvores de decisão.
- **HistGradientBoosting Regressor:** implementação de boosting com histogramas, voltada à eficiência computacional.
- **XGBoost e LightGBM:** algoritmos opcionais de boosting, quando disponíveis no ambiente.
- **StackingRegressor:** abordagem de ensemble que combina modelos-base para gerar uma previsão final.

A comparação entre os algoritmos permite identificar qual abordagem apresenta melhor equilíbrio entre precisão e capacidade de generalização para o conjunto de dados utilizado.

---

## 5. Resultados

Os resultados abaixo representam as métricas registradas na avaliação dos modelos. O conjunto de teste corresponde a 20% dos dados separados antes do treinamento.

O coeficiente de determinação (R²) mede a proporção da variabilidade da variável-alvo explicada pelo modelo. O RMSE (*Root Mean Squared Error*) representa a raiz do erro quadrático médio e é expresso na mesma unidade da variável prevista, neste caso, MPa.

### Comparação de desempenho

| Modelo | R² Teste | RMSE (MPa) | R² CV (média) | R² CV (desvio-padrão) |
| :--- | :---: | :---: | :---: | :---: |
| **Stacking (Ensemble)** | **0,9270** | **4,34** | — | — |
| HistGradientBoosting | 0,9252 | 4,39 | 0,9257 | 0,0130 |
| GradientBoosting | 0,9188 | 4,57 | 0,9218 | 0,0095 |
| Random Forest — Baseline | 0,9104 | 4,81 | 0,9004 | 0,0131 |
| Random Forest — Otimizado | 0,9080 | 4,87 | 0,9129 | 0,0100 |

### Interpretação dos resultados

O modelo **Stacking (Ensemble)** apresentou o melhor resultado na avaliação de teste, com R² de 0,9270 e RMSE de 4,34 MPa.

O HistGradientBoosting apresentou desempenho próximo, com R² de 0,9252 e RMSE de 4,39 MPa, além de resultados de validação cruzada com média de R² igual a 0,9257.

Os resultados indicam que os modelos conseguem representar uma parcela expressiva da variabilidade da resistência à compressão presente na base analisada. Entretanto, o erro de previsão permanece relevante e deve ser considerado antes de qualquer aplicação operacional.

A utilização desses modelos pode apoiar estudos preliminares de dosagem, análises comparativas e planejamento de ensaios. A adoção em decisões estruturais exige validação experimental, avaliação das condições de aplicação e atendimento às normas técnicas pertinentes.

**Nota metodológica:** os valores apresentados correspondem aos resultados registrados neste projeto. Para assegurar a reprodutibilidade, recomenda-se confirmar as métricas diretamente no notebook executado e verificar se o Stacking foi avaliado com o mesmo protocolo de separação e validação aplicado aos demais modelos.

---

## 6. Importância das Variáveis e Análise dos Resultados

A análise de correlação, a importância das variáveis (*Feature Importance*) e a importância por permutação (*Permutation Importance*) são utilizadas para investigar quais atributos apresentam maior contribuição para as previsões dos modelos.

Entre as variáveis de interesse estão a relação água/cimento (`relacao_ac`), a idade de cura (`log_idade`) e a quantidade de cimento. Essas características possuem justificativa técnica no comportamento do concreto e permitem relacionar os padrões identificados pelo algoritmo ao conhecimento de engenharia de materiais.

A interpretação dessas análises pode apoiar diferentes decisões de negócio:

- **Suprimentos e planejamento:** identificação dos insumos associados a mudanças relevantes na resistência estimada.
- **Pesquisa e desenvolvimento:** avaliação comparativa de formulações e investigação da influência das adições minerais.
- **Eficiência operacional:** estudo de alternativas de dosagem com foco na relação entre desempenho técnico e consumo de materiais.
- **Sustentabilidade:** análise de possibilidades de substituição parcial do cimento, sujeita à confirmação experimental e ao atendimento dos requisitos de desempenho.
- **Controle de qualidade:** identificação de variáveis que merecem acompanhamento prioritário na caracterização das misturas.

A importância preditiva de uma variável não demonstra, isoladamente, uma relação causal. Além disso, os resultados de importância dependem dos dados, das correlações entre os atributos e do algoritmo utilizado.

Por esse motivo, as conclusões devem ser interpretadas em conjunto com os fundamentos técnicos, os resultados experimentais e as limitações da base de dados.

---

## 7. Estrutura do Repositório

A organização do repositório foi planejada para facilitar a consulta aos resultados, a reprodução dos experimentos e a compreensão do processo de desenvolvimento.

```text
Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning/
├── SG_Site.png
├── Relatorio_Predicao_Concreto.ipynb
├── Relatorio_Predicao_Concreto.pdf
├── Relatorio_Predicao_Concreto.html
├── gerar_relatorio.py
└── README.md
```

### Descrição dos arquivos

- **`SG_Site.png`:** imagem institucional utilizada no cabeçalho do README.
- **`Relatorio_Predicao_Concreto.ipynb`:** notebook Jupyter com células de código, análises, tabelas, gráficos e resultados registrados.
- **`Relatorio_Predicao_Concreto.pdf`:** relatório estático para consulta e apresentação dos resultados.
- **`Relatorio_Predicao_Concreto.html`:** versão navegável do relatório, adequada para visualização em navegadores compatíveis.
- **`gerar_relatorio.py`:** script utilizado para construir, executar e exportar o notebook por meio das ferramentas Python e Jupyter.
- **`README.md`:** documentação principal do projeto, com contexto, metodologia, resultados e instruções de reprodução.

O script de geração utiliza ferramentas do ecossistema Jupyter, incluindo `nbformat` e `nbclient`. Em ambientes Windows, pode ser necessário ajustar a configuração do event loop para compatibilidade com bibliotecas utilizadas pelo Jupyter e pelo ZeroMQ.

---

## 8. Como Reproduzir

Para reproduzir o projeto, é necessário ter Python instalado e acesso ao terminal. Recomenda-se utilizar um ambiente virtual para isolar as dependências.

### Etapa 1 — Clonar o repositório

```bash
git clone https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning.git

cd Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning
```

### Etapa 2 — Criar e ativar um ambiente virtual

No Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Etapa 3 — Instalar as dependências

```bash
python -m pip install --upgrade pip

pip install jupyter nbformat nbclient pandas numpy matplotlib seaborn scikit-learn
```

Para habilitar os algoritmos opcionais XGBoost e LightGBM, execute:

```bash
pip install xgboost lightgbm
```

A disponibilidade desses pacotes pode alterar os modelos avaliados e os resultados obtidos. Para reproduzir os números do relatório, é importante manter as versões das bibliotecas e a configuração experimental compatíveis com as utilizadas na execução original.

### Etapa 4 — Gerar e executar o notebook

Execute o script a partir da pasta do repositório:

```bash
python gerar_relatorio.py
```

O script é responsável pela geração e execução automatizada do notebook, conforme a implementação existente no repositório.

### Alternativa — Executar manualmente

Também é possível abrir o arquivo `Relatorio_Predicao_Concreto.ipynb` no Jupyter Notebook ou no Visual Studio Code e executar as células na sequência apresentada.

**Tempo estimado de execução:** de 8 a 15 minutos, conforme o hardware disponível, as dependências instaladas e a configuração da busca de hiperparâmetros.

**Observação:** a reprodução integral depende da disponibilidade dos arquivos referenciados pelo script, do acesso à base de dados e da compatibilidade das versões das bibliotecas. O tempo informado é estimativo, não uma garantia de duração.

---

## 9. Próximos Passos Recomendados

O projeto pode evoluir de um estudo experimental para uma ferramenta de apoio à decisão por meio das seguintes melhorias:

1. **Ampliação da base de dados:** incorporar resultados de ensaios em idades iniciais, como 1, 3 e 7 dias, e buscar dados adicionais de diferentes composições, condições de cura e origens de materiais.
2. **Quantificação da incerteza:** implementar intervalos de previsão utilizando técnicas como *Quantile Regression Forests* ou *Conformal Prediction*, permitindo avaliar a dispersão esperada das estimativas.
3. **Validação externa:** testar os modelos com dados de obras, centrais dosadoras ou laboratórios não utilizados no treinamento, avaliando sua capacidade de generalização.
4. **Deploy por API REST:** disponibilizar o modelo por meio de uma API para integração com sistemas de dosagem, plataformas de controle de qualidade e aplicações operacionais.
5. **Monitoramento de desempenho e drift:** acompanhar mudanças na distribuição dos dados e na qualidade das previsões, definindo critérios objetivos para reavaliação e retreinamento.
6. **Otimização de dosagem com restrições técnicas:** desenvolver análises que considerem resistência-alvo, custo dos materiais, trabalhabilidade, durabilidade e requisitos normativos.
7. **Monitoramento de indicadores de negócio:** mensurar, em ambiente controlado, os efeitos da aplicação sobre custos, consumo de cimento, tempo de decisão e frequência de ensaios complementares.
8. **Documentação da reprodutibilidade:** registrar versões das bibliotecas, parâmetros dos experimentos, sementes aleatórias, critérios de seleção e métricas de cada execução.

Essas melhorias podem ampliar a utilidade do projeto e aproximar a modelagem preditiva de aplicações práticas na construção civil, preservando a validação técnica como requisito para decisões relacionadas à segurança e ao desempenho estrutural.

---

## Considerações Finais

Este projeto demonstra a aplicação de Machine Learning à previsão da resistência à compressão do concreto, integrando engenharia de atributos, comparação de algoritmos, otimização de hiperparâmetros e combinação de modelos.

Além do exercício técnico, a iniciativa evidencia como dados e modelos preditivos podem apoiar análises de eficiência operacional, controle de qualidade, planejamento de materiais e avaliação de oportunidades de redução de custos.

Os resultados apresentados são referentes ao conjunto de dados utilizado e não substituem ensaios laboratoriais, especificações de projeto, normas técnicas ou a responsabilidade dos profissionais habilitados.

O objetivo é demonstrar uma abordagem analítica reproduzível, com potencial de evolução para soluções de apoio à decisão orientadas a dados no setor da construção civil.

---

## Autor

**Silvânio Góis**

Gestor de Operações e Negócios Orientado a Dados, com interesse na aplicação de análise de dados, indicadores de desempenho e Machine Learning à melhoria de processos e à tomada de decisão.

- Website: https://www.silvaniogois.com.br
- LinkedIn: https://www.linkedin.com/in/silvanio-gois
- GitHub: https://github.com/SilvanioSG
- E-mail: sg@silvaniogois.com.br

---

## Licença e Uso

Os dados utilizados são provenientes de uma fonte pública, identificada na seção de origem dos dados. A reutilização do conjunto deve respeitar as condições de atribuição e os termos aplicáveis à fonte original.

O código, a documentação e os resultados deste repositório devem ser utilizados considerando suas limitações metodológicas e a necessidade de validação independente antes de qualquer aplicação em contexto real.

Para fins acadêmicos, profissionais ou de pesquisa, recomenda-se citar a fonte original dos dados e identificar este repositório como referência para a implementação apresentada.
