"""
Gera apresentação HTML interativa e RESPONSIVA (Reveal.js)
com auto-fit por slide — nada é cortado em nenhum tamanho de tela.
"""
import json
import base64
import os

INPUT_NB  = "Predição de Resistência do Concreto.ipynb"
LOGO_FILE = "SG_Site.png"
OUTPUT    = "apresentacao_concreto.html"

with open(INPUT_NB, "r", encoding="utf-8") as f:
    nb = json.load(f)
outputs = nb["cells"][0]["outputs"]

img_heatmap = "data:image/png;base64," + outputs[3]["data"]["image/png"]
img_scatter = "data:image/png;base64," + outputs[5]["data"]["image/png"]
img_import  = "data:image/png;base64," + outputs[6]["data"]["image/png"]

with open(LOGO_FILE, "rb") as f:
    logo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode()

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Previsão de Resistência do Concreto | Silvânio Góis</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/theme/black.css" id="theme">
<style>
/* ================================================================
   VARIÁVEIS DE TEMA
   ================================================================ */
:root {{
    --azul-escuro:#0b1b2b; --azul-medio:#14375c;
    --laranja:#ff7b00; --cinza:#b8c4cf;
    --verde:#2ecc71; --vermelho:#e74c3c;
}}

/* ================================================================
   BASE — Fontes reduzidas para ganhar espaço vertical
   ================================================================ */
.reveal {{
    font-family:'Inter','Segoe UI',sans-serif;
    font-size:30px;               /* antes: 40px → 25% de economia */
}}
.reveal h1, .reveal h2, .reveal h3 {{
    font-family:'Inter','Segoe UI',sans-serif;
    text-transform:none;
    letter-spacing:-0.5px;
    margin:0.15em 0;
}}
.reveal h1 {{ font-size:1.6em; color:#fff; }}
.reveal h2 {{ font-size:1.15em; color:var(--laranja); margin-bottom:0.4em; }}
.reveal h3 {{ font-size:0.8em; color:var(--cinza); margin-bottom:0.3em; }}
.reveal p, .reveal li {{
    font-size:0.62em; line-height:1.4; margin:0.2em 0; color:#e0e6ed;
}}

/* ================================================================
   LAYOUT DO SLIDE — Flexbox com centralização vertical
   ================================================================ */
.reveal .slides section {{
    height:100% !important;
    padding:0 !important;
    text-align:left;
    overflow:hidden;              /* clip extra residual */
}}

.slide-content {{
    height:100%;
    box-sizing:border-box;
    padding:25px 45px;
    display:flex;
    flex-direction:column;
    justify-content:center;        /* centraliza verticalmente */
    transform-origin:center center;
    will-change:transform;
}}
.slide-content > * {{
    flex-shrink:0;                 /* impede compressão */
}}

/* ================================================================
   COMPONENTES
   ================================================================ */
/* Caixa de destaque */
.highlight-box {{
    background:linear-gradient(135deg,var(--azul-medio),var(--azul-escuro));
    border-left:5px solid var(--laranja);
    padding:14px 22px;
    border-radius:10px;
    margin:0.6em 0;
}}
.highlight-box p {{ margin:0; }}

/* Listas com ícone */
.icon-list {{ list-style:none; padding:0; margin:0.4em 0; }}
.icon-list li {{
    padding:0.3em 0 0.3em 1.6em;
    position:relative;
}}
.icon-list li::before {{
    content:'▸'; color:var(--laranja); font-size:1.2em;
    position:absolute; left:6px; top:0.28em;
}}

/* Grid de métricas */
.metric-grid {{
    display:flex; gap:20px; justify-content:center;
    margin:0.8em 0; flex-wrap:wrap;
}}
.metric-card {{
    background:linear-gradient(135deg,#1a2f4a,#0b1b2b);
    border:2px solid var(--laranja);
    border-radius:14px;
    padding:18px 24px;
    text-align:center;
    min-width:190px;
    box-shadow:0 8px 24px rgba(255,123,0,0.15);
}}
.metric-card .value {{ font-size:2em; font-weight:800; color:var(--laranja); }}
.metric-card .label {{
    font-size:0.6em; color:var(--cinza); margin-top:6px;
    text-transform:uppercase; letter-spacing:1px;
}}

/* Duas colunas — imagem + texto */
.two-col {{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:25px;
    align-items:center;
    width:100%;
}}
.two-col > div {{
    min-height:0;
    display:flex;
    flex-direction:column;
    justify-content:center;
}}
.two-col img {{
    width:100%;
    max-height:400px;              /* CAP explícito — evita estouro */
    height:auto;
    object-fit:contain;
    border-radius:10px;
    box-shadow:0 6px 20px rgba(0,0,0,0.5);
    display:block;
}}

/* Tabela compacta */
.reveal table {{
    font-size:0.55em;
    width:100%;
    border-collapse:collapse;
    margin:0.4em 0;
}}
.reveal table th {{
    background:var(--azul-medio);
    color:var(--laranja);
    padding:0.35em 0.6em;
    text-align:left;
}}
.reveal table td {{
    padding:0.3em 0.6em;
    border-bottom:1px solid #2c4257;
}}

/* Capa e slide de contato */
.slide-capa .slide-content {{
    text-align:center;
    align-items:center;
}}
.slide-capa img {{
    max-height:130px;
    border-radius:12px;
    margin-bottom:12px;
}}
.slide-capa h1 {{ margin:10px 0; }}
.slide-capa .subtitle {{ color:var(--cinza); font-size:0.7em; margin:6px 0; }}
.slide-capa .author {{ color:var(--laranja); font-size:0.65em; font-weight:600; }}

/* Rodapé fixo (fora do slide-content para não escalar) */
.footer {{
    position:absolute;
    bottom:10px; left:0; right:0;
    text-align:center;
    font-size:0.4em;
    color:#5a6b7a;
    letter-spacing:1px;
    pointer-events:none;
}}

/* Numeração */
.reveal .slide-number {{
    background:rgba(255,123,0,0.85); color:#000;
    font-weight:700; font-size:0.55em;
}}

/* Utilitários */
.accent {{ color:var(--laranja); font-weight:700; }}
.green  {{ color:var(--verde); font-weight:700; }}
.red    {{ color:var(--vermelho); font-weight:700; }}
.center {{ text-align:center; }}
.big    {{ font-size:1.15em; }}
.small  {{ font-size:0.6em; color:var(--cinza); }}

/* Botões contato */
.contact-grid {{
    display:flex; gap:12px; justify-content:center;
    margin-top:20px; flex-wrap:wrap;
}}
.contact-btn {{
    background:var(--azul-medio); color:#fff !important;
    padding:10px 20px; border-radius:26px;
    text-decoration:none; font-size:0.65em;
    border:2px solid var(--laranja);
    transition:0.3s;
}}
.contact-btn:hover {{ background:var(--laranja); color:#000 !important; }}

/* ================================================================
   RESPONSIVIDADE EXTRA (telas muito pequenas)
   ================================================================ */
@media (max-width:900px) {{
    .two-col {{ grid-template-columns:1fr; gap:15px; }}
    .two-col img {{ max-height:280px; }}
    .metric-card {{ min-width:150px; padding:14px 18px; }}
    .reveal table {{ font-size:0.5em; }}
}}
</style>
</head>
<body>
<div class="reveal">
<div class="slides">

    <!-- ============ SLIDE 1: CAPA ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)" class="slide-capa">
        <div class="slide-content">
            <img src="{logo_b64}" alt="Silvânio Góis">
            <h1>Previsão da Resistência à Compressão do Concreto</h1>
            <p class="subtitle">Otimização de Dosagem, Redução de Custos e Controle de Qualidade com Machine Learning</p>
            <p class="author">Silvânio Góis — Gestor de Operações e Negócios Orientado a Dados</p>
        </div>
        <div class="footer">Use as setas ← → para navegar · F para tela cheia · ESC para visão geral</div>
    </section>

    <!-- ============ SLIDE 2: PROBLEMA ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> O Problema</h2>
            <div class="highlight-box">
                <p class="big">Validar um traço de concreto exige <span class="accent">28 dias de cura</span> até o rompimento do corpo de prova.</p>
            </div>
            <ul class="icon-list">
                <li><span class="red">Atrasos no cronograma</span> — desforma e liberação de escoramentos dependem do resultado</li>
                <li><span class="red">Custos com retrabalho</span> — se o lote não atinge a resistência projetada</li>
                <li><span class="red">Riscos operacionais</span> — estruturas liberadas antes do tempo seguro</li>
                <li><span class="red">Desperdício de cimento</span> — superdimensionamento preventivo por incerteza</li>
            </ul>
        </div>
        <div class="footer">O custo da incerteza em obras é medido em dias e em reais</div>
    </section>

    <!-- ============ SLIDE 3: SOLUÇÃO ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> A Solução Proposta</h2>
            <div class="highlight-box">
                <p class="big">Modelo preditivo de <span class="accent">Machine Learning (Random Forest)</span> que estima a resistência em MPa a partir do traço e idade de cura.</p>
            </div>
            <ul class="icon-list">
                <li> <span class="accent">Redução no consumo de cimento</span> sem perda de segurança estrutural</li>
                <li> <span class="accent">Antecipação de decisões</span> no canteiro de obras</li>
                <li> <span class="accent">Minimização de desperdícios</span> e emissões de CO₂</li>
                <li> <span class="accent">Previsão em segundos</span> vs. 28 dias de espera</li>
            </ul>
        </div>
        <div class="footer">Dos dados do laboratório ao canteiro, em tempo real</div>
    </section>

    <!-- ============ SLIDE 4: DADOS ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> Os Dados de Entrada</h2>
            <p class="small">1.030 ensaios laboratoriais reais · 9 atributos · Componentes em kg/m³</p>
            <table>
                <thead>
                    <tr><th>Atributo</th><th>Descrição na Engenharia Civil</th></tr>
                </thead>
                <tbody>
                    <tr><td><b>Cimento</b></td><td>Aglomerante principal (maior custo)</td></tr>
                    <tr><td><b>Escória de Alto Forno</b></td><td>Subproduto que melhora durabilidade</td></tr>
                    <tr><td><b>Cinza Volante</b></td><td>Pozolana que substitui parte do cimento</td></tr>
                    <tr><td><b>Água</b></td><td>Regula a relação água/cimento (a/c)</td></tr>
                    <tr><td><b>Superplastificante</b></td><td>Aditivo que reduz a necessidade de água</td></tr>
                    <tr><td><b>Agregado Graúdo / Miúdo</b></td><td>Brita e areia</td></tr>
                    <tr><td><b>Idade</b></td><td>Tempo de cura (dias)</td></tr>
                    <tr><td><b>Resistência</b></td><td><span class="accent">Variável alvo</span> em MPa</td></tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- ============ SLIDE 5: METODOLOGIA ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> Metodologia</h2>
            <div class="two-col">
                <div>
                    <h3>Pipeline do projeto</h3>
                    <ul class="icon-list">
                        <li><b>Pré-processamento</b> — Padronização e limpeza</li>
                        <li><b>Split 80/20</b> — Treino e teste (validação honesta)</li>
                        <li><b>Random Forest</b> — 100 árvores de decisão</li>
                        <li><b>Avaliação</b> — R² e RMSE na base de teste</li>
                        <li><b>Interpretação</b> — Feature Importance</li>
                    </ul>
                </div>
                <div>
                    <div class="highlight-box">
                        <p><b>Por que Random Forest?</b></p>
                        <p class="small">Robusto a não-linearidades · Resistente a overfitting · Fornece importância das variáveis · Excelente para materiais heterogêneos</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ SLIDE 6: HEATMAP ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> Matriz de Correlação</h2>
            <div class="two-col">
                <div><img src="{img_heatmap}" alt="Heatmap"></div>
                <div>
                    <h3>O que o gráfico revela</h3>
                    <ul class="icon-list">
                        <li><b>Cimento</b> e <b>idade de cura</b> — correlação positiva forte</li>
                        <li><b>Superplastificante</b> — correlação positiva moderada</li>
                        <li><b>Água</b> — correlação <span class="red">negativa</span> (princípio de Abrams)</li>
                    </ul>
                    <p class="small" style="margin-top:10px;"><b>Benefício:</b> identifica quais aditivos priorizar para substituir o cimento.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ SLIDE 7: MÉTRICAS ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content center">
            <h2> Desempenho do Modelo</h2>
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="value">0,8841</div>
                    <div class="label">R² Score</div>
                    <div class="small" style="margin-top:6px;">Explica 88,4% da variação</div>
                </div>
                <div class="metric-card">
                    <div class="value">5,46 MPa</div>
                    <div class="label">RMSE</div>
                    <div class="small" style="margin-top:6px;">Erro médio das previsões</div>
                </div>
            </div>
            <div class="highlight-box" style="max-width:800px;margin:15px auto 0;">
                <p>O modelo explica <span class="accent">mais de 88% da variação</span> da resistência apenas com o traço e a idade. Erro médio de <span class="accent">5,5 MPa</span> — excelente para materiais heterogêneos.</p>
            </div>
        </div>
        <div class="footer">Fonte: avaliação na base de teste (206 amostras não vistas no treino)</div>
    </section>

    <!-- ============ SLIDE 8: VALIDAÇÃO ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> Validação: Real vs. Predito</h2>
            <div class="two-col">
                <div><img src="{img_scatter}" alt="Scatter"></div>
                <div>
                    <h3>Como interpretar</h3>
                    <ul class="icon-list">
                        <li>Pontos próximos à linha tracejada indicam <span class="green">alta precisão</span></li>
                        <li>Dispersão maior em concretos de altíssimo desempenho (&gt;60 MPa)</li>
                        <li>Sem viés sistemático de sub ou superestimação</li>
                    </ul>
                    <p class="small" style="margin-top:10px;"><b>Benefício:</b> permite definir coeficiente de segurança preditivo para desforma de lajes e pilares.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ SLIDE 9: FEATURE IMPORTANCE ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> Importância das Variáveis</h2>
            <div class="two-col">
                <div><img src="{img_import}" alt="Feature Importance"></div>
                <div>
                    <h3>Quem manda no resultado</h3>
                    <ul class="icon-list">
                        <li><b>Idade de cura</b> — dominante no modelo</li>
                        <li><b>Cimento</b> — segundo maior peso</li>
                        <li><b>Água</b> e <b>superplastificantes</b> — influência significativa</li>
                    </ul>
                    <p class="small" style="margin-top:10px;"><b>Benefício ESG:</b> direciona P&amp;D e suprimentos na negociação de aditivos e adições minerais, reduzindo custo/m³ sem perda de qualidade.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ SLIDE 10: IMPACTO ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2> Impacto Estratégico e ROI</h2>
            <div class="highlight-box">
                <h3 style="margin-top:0;"> Aceleração de Cronograma</h3>
                <p>Previsão do ganho de resistência em idades jovens (3 e 7 dias), antecipando a desforma segura e liberando escoramentos.</p>
            </div>
            <div class="highlight-box">
                <h3 style="margin-top:0;"> Economia Financeira</h3>
                <p>Otimização dos traços para evitar superdimensionamento preventivo do cimento.</p>
            </div>
            <div class="highlight-box">
                <h3 style="margin-top:0;"> Sustentabilidade (ESG)</h3>
                <p>Menor consumo de clínquer por m³, reduzindo a pegada de carbono — indicador estratégico para relatórios de sustentabilidade.</p>
            </div>
        </div>
    </section>

    <!-- ============ SLIDE 11: CONCLUSÃO ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)" class="slide-capa">
        <div class="slide-content">
            <h2> Conclusão</h2>
            <div class="highlight-box" style="max-width:900px;margin:20px auto;">
                <p class="big">É possível prever a resistência do concreto com <span class="accent">alta confiabilidade</span> (R² ≈ 0,88) a partir do traço e da idade de cura.</p>
            </div>
            <p style="margin-top:15px;">Esta solução tem potencial para <b>transformar a gestão de qualidade</b> na construção civil:</p>
            <div style="display:flex;gap:25px;justify-content:center;margin-top:15px;font-size:1.1em;flex-wrap:wrap;">
                <span> Mais rápido</span>
                <span> Mais barato</span>
                <span> Mais sustentável</span>
            </div>
        </div>
    </section>

    <!-- ============ SLIDE 12: CONTATO ============ -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)" class="slide-capa">
        <div class="slide-content">
            <img src="{logo_b64}" alt="Silvânio Góis">
            <h2>Da estratégia à operação, conectando, processos, pessoas e resultados</h2>
            <p class="subtitle">Gestão de Operações & Análise de Dados aplicados à Engenharia Civil</p>
            <p class="author">Silvânio Góis</p>
            <div class="contact-grid">
                <a class="contact-btn" href="https://www.silvaniogois.com.br" target="_blank"> Website</a>
                <a class="contact-btn" href="https://www.linkedin.com/in/silvanio-gois" target="_blank"> LinkedIn</a>
                <a class="contact-btn" href="https://github.com/SilvanioSG" target="_blank"> GitHub</a>
                <a class="contact-btn" href="mailto:sg@silvaniogois.com.br"> E-mail</a>
            </div>
        </div>
    </section>

</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.js"></script>
<script>
Reveal.initialize({{
    hash: true,
    slideNumber: 'c/t',
    transition: 'slide',
    transitionSpeed: 'default',
    backgroundTransition: 'fade',
    controls: true,
    progress: true,
    center: false,
    width: 1280,
    height: 720,
    margin: 0.02,
    minScale: 0.2,
    maxScale: 1.6,
    keyboard: true,
    overview: true,
    touch: true,
    loop: false,
}});

/* ============================================================
   AUTO-FIT: mede cada slide e aplica scale() se estourar.
   É um "cinto de segurança" — com o CSS corrigido acima,
   raramente será acionado, mas garante 0% de corte.
   ============================================================ */
function autoFitSlides() {{
    document.querySelectorAll('.reveal .slides section').forEach(section => {{
        const content = section.querySelector('.slide-content');
        if (!content) return;

        // Reset transform anterior
        content.style.transform = '';
        content.style.width = '';

        // Força reflow para medir corretamente
        void content.offsetHeight;

        const availH = section.clientHeight;
        const needH  = content.scrollHeight;

        // Se estourar (com tolerância de 4px), escala para caber
        if (needH > availH + 4) {{
            const scale = (availH - 4) / needH;
            content.style.transform = `scale(${{scale}})`;
            content.style.transformOrigin = 'center center';
        }}
    }});
}}

Reveal.on('ready', autoFitSlides);
Reveal.on('slidechanged', autoFitSlides);

let resizeTimer;
window.addEventListener('resize', () => {{
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(autoFitSlides, 150);
}});
</script>
</body>
</html>
"""

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f" Apresentação gerada: {OUTPUT}")
print(f" Tamanho: {os.path.getsize(OUTPUT) / 1024:.1f} KB")
print(f" 12 slides · responsivo · auto-fit ativo")