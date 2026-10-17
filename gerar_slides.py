"""
Gera apresentação HTML interativa e RESPONSIVA (Reveal.js).
- Desktop: canvas 1280x720 + auto-fit.
- Mobile portrait: viewport nativo + scroll vertical.
- Mobile landscape (tela baixa): viewport nativo + 2 colunas compactas.
- Setas de navegação por toque no rodapé (mobile).
- Links da documentação no GitHub.
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

DOC_URL = "https://github.com/SilvanioSG/Previsao-da-Resistencia-Compressao-do-Concreto-com-Machine-Learning"

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#0b1b2b">
<title>Previsão de Resistência do Concreto | Silvânio Góis</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/theme/black.css" id="theme">
<style>
:root {{
    --azul-escuro:#0b1b2b; --azul-medio:#14375c;
    --laranja:#ff7b00; --cinza:#b8c4cf;
    --verde:#2ecc71; --vermelho:#e74c3c;
}}

/* ============ BASE — DESKTOP ============ */
.reveal {{ font-family:'Inter','Segoe UI',sans-serif; font-size:30px; }}
.reveal h1, .reveal h2, .reveal h3 {{
    font-family:'Inter','Segoe UI',sans-serif;
    text-transform:none; letter-spacing:-0.5px; margin:0.15em 0;
}}
.reveal h1 {{ font-size:1.6em; color:#fff; }}
.reveal h2 {{ font-size:1.15em; color:var(--laranja); margin-bottom:0.4em; }}
.reveal h3 {{ font-size:0.8em;  color:var(--cinza);   margin-bottom:0.3em; }}
.reveal p, .reveal li {{ font-size:0.62em; line-height:1.4; margin:0.2em 0; color:#e0e6ed; }}

/* ============ LAYOUT ============ */
.reveal .slides section {{ height:100% !important; padding:0 !important; text-align:left; overflow:hidden; }}
.slide-content {{
    height:100%; box-sizing:border-box;
    padding:25px 45px;
    display:flex; flex-direction:column; justify-content:center;
    transform-origin:center center; will-change:transform;
}}
.slide-content > * {{ flex-shrink:0; }}

/* ============ COMPONENTES ============ */
.highlight-box {{
    background:linear-gradient(135deg,var(--azul-medio),var(--azul-escuro));
    border-left:5px solid var(--laranja);
    padding:14px 22px; border-radius:10px; margin:0.6em 0;
}}
.highlight-box p {{ margin:0; }}

/* ==== RESET DE MARCADOR — mata o disc branco do tema ==== */
.reveal .slides ul.icon-list,
.reveal .slides section ul.icon-list,
.reveal ul.icon-list {{
    list-style: none !important;
    list-style-type: none !important;
    margin: 0.4em 0 !important;
    padding: 0 !important;
    display: block !important;
}}
.reveal .slides ul.icon-list > li,
.reveal .slides section ul.icon-list > li,
.reveal ul.icon-list > li {{
    list-style: none !important;
    list-style-type: none !important;
    padding: 0.3em 0 0.3em 1.6em !important;
    position: relative;
    margin: 0 !important;
}}
.reveal .slides ul.icon-list > li::marker,
.reveal .slides section ul.icon-list > li::marker {{
    content: '' !important;
    color: transparent !important;
    display: none !important;
}}
.reveal .slides ul.icon-list > li::before {{
    content: '▸';
    color: var(--laranja);
    font-size: 1.2em;
    position: absolute;
    left: 6px;
    top: 0.26em;
    line-height: 1;
}}

.metric-grid {{ display:flex; gap:20px; justify-content:center; margin:0.8em 0; flex-wrap:wrap; }}
.metric-card {{
    background:linear-gradient(135deg,#1a2f4a,#0b1b2b);
    border:2px solid var(--laranja); border-radius:14px;
    padding:18px 24px; text-align:center; min-width:190px;
    box-shadow:0 8px 24px rgba(255,123,0,0.15);
}}
.metric-card .value {{ font-size:2em; font-weight:800; color:var(--laranja); }}
.metric-card .label {{ font-size:0.6em; color:var(--cinza); margin-top:6px; text-transform:uppercase; letter-spacing:1px; }}

.two-col {{ display:grid; grid-template-columns:1fr 1fr; gap:25px; align-items:center; width:100%; }}
.two-col > div {{ min-height:0; display:flex; flex-direction:column; justify-content:center; }}
.two-col img {{
    width:100%; max-height:400px; height:auto;
    object-fit:contain; border-radius:10px;
    box-shadow:0 6px 20px rgba(0,0,0,0.5); display:block;
}}

.reveal table {{ font-size:0.55em; width:100%; border-collapse:collapse; margin:0.4em 0; }}
.reveal table th {{ background:var(--azul-medio); color:var(--laranja); padding:0.35em 0.6em; text-align:left; }}
.reveal table td {{ padding:0.3em 0.6em; border-bottom:1px solid #2c4257; }}

.slide-capa .slide-content {{ text-align:center; align-items:center; }}
.slide-capa img {{ max-height:130px; border-radius:12px; margin-bottom:12px; }}
.slide-capa h1 {{ margin:10px 0; }}
.slide-capa .subtitle {{ color:var(--cinza); font-size:0.7em; margin:6px 0; }}
.slide-capa .author {{ color:var(--laranja); font-size:0.65em; font-weight:600; }}

.footer {{
    position:absolute; bottom:10px; left:0; right:0;
    text-align:center; font-size:0.4em; color:#5a6b7a;
    letter-spacing:1px; pointer-events:none;
}}
.reveal .slide-number {{
    background:rgba(255,123,0,0.85); color:#000;
    font-weight:700; font-size:0.55em;
}}

.accent {{ color:var(--laranja); font-weight:700; }}
.green  {{ color:var(--verde);   font-weight:700; }}
.red    {{ color:var(--vermelho);font-weight:700; }}
.center {{ text-align:center; }}
.big    {{ font-size:1.15em; }}
.small  {{ font-size:0.6em; color:var(--cinza); }}

/* ==== LINK INLINE DE DOCUMENTAÇÃO ==== */
.doc-reference {{
    margin-top:0.6em;
    padding-top:0.5em;
    border-top:1px solid rgba(255,123,0,0.25);
    display:flex; flex-wrap:wrap; gap:4px 8px;
    align-items:center;
}}
.doc-label {{ color:var(--cinza); font-size:0.85em; }}
.reveal .doc-link, a.doc-link {{
    color:var(--laranja) !important;
    font-weight:600; font-size:0.9em;
    text-decoration:none;
    border-bottom:1px dashed var(--laranja);
    padding-bottom:1px; transition:0.2s;
}}
.reveal .doc-link:hover {{
    color:#fff !important;
    background:rgba(255,123,0,0.15);
    border-bottom-style:solid;
}}

.contact-grid {{ display:flex; gap:12px; justify-content:center; margin-top:20px; flex-wrap:wrap; }}
.contact-btn {{
    background:var(--azul-medio); color:#fff !important;
    padding:10px 20px; border-radius:26px;
    text-decoration:none; font-size:0.65em;
    border:2px solid var(--laranja); transition:0.3s;
}}
.contact-btn:hover {{ background:var(--laranja); color:#000 !important; }}

.mobile-only {{ display:none; }}
.desktop-only {{ display:inline; }}

/* ================================================================
   NAVEGAÇÃO POR TOQUE — visível só em mobile/landscape
   ================================================================ */
.mobile-nav {{ display: none; }}

/* ================================================================
   MOBILE — largura estreita OU altura baixa (landscape)
   ================================================================ */
@media (max-width: 900px), (max-height: 500px) {{
    html, body {{ height:100%; overflow:hidden; }}
    .reveal {{ font-size:17px; }}
    .reveal h1 {{ font-size:1.5em;  line-height:1.2; }}
    .reveal h2 {{ font-size:1.35em; line-height:1.2; margin-bottom:0.5em; }}
    .reveal h3 {{ font-size:1em;    line-height:1.25; }}
    .reveal p, .reveal li {{ font-size:0.95em; line-height:1.5; margin:0.3em 0; }}

    .reveal .slides {{ height:100% !important; }}
    .reveal .slides section {{ height:100% !important; }}

    /* padding-top maior para não colidir com slide-number (top-right)
       padding-bottom reserva espaço para os botões de navegação */
    .slide-content {{
        padding:30px 16px 56px;
        justify-content:flex-start;
        overflow-y:auto;
        overflow-x:hidden;
        -webkit-overflow-scrolling:touch;
        touch-action:pan-y;
        overscroll-behavior:contain;
    }}

    .two-col {{ grid-template-columns:1fr; gap:14px; align-items:stretch; }}
    .two-col > div {{ justify-content:flex-start; }}
    .two-col img {{ width:100%; max-height:42vh; object-fit:contain; margin:0 auto; }}

    .highlight-box {{ padding:12px 14px; margin:0.5em 0; border-left-width:4px; }}
    .icon-list > li {{ padding:0.3em 0 0.3em 1.4em !important; }}
    .icon-list > li::before {{ top:0.3em !important; }}

    .metric-grid {{ gap:12px; margin:0.6em 0; }}
    .metric-card {{ min-width:130px; padding:12px 16px; border-radius:10px; }}
    .metric-card .value {{ font-size:1.7em; }}
    .metric-card .label {{ font-size:0.75em; letter-spacing:0.5px; }}

    .reveal table {{ font-size:0.85em; }}
    .reveal table th, .reveal table td {{ padding:0.45em 0.55em; }}

    .slide-capa img {{ max-height:100px; margin-bottom:8px; }}
    .slide-capa h1 {{ font-size:1.4em; margin:8px 0; }}
    .slide-capa .subtitle {{ font-size:0.9em; }}
    .slide-capa .author   {{ font-size:0.85em; }}

    .contact-grid {{ gap:8px; margin-top:14px; }}
    .contact-btn {{ padding:9px 16px; font-size:0.85em; border-radius:22px; }}

    /* Rodapé estreitado — os botões laterais ocupam ~52px de cada lado */
    .footer {{ font-size:0.7em; bottom:4px; left:60px; right:60px; letter-spacing:0.4px; }}

    /* Slide-number vai para o canto superior direito (libera o rodapé) */
    .reveal .slide-number {{
        font-size:0.7em; padding:4px 8px;
        top:8px; bottom:auto; right:8px;
    }}

    .small {{ font-size:0.82em; }}
    .big   {{ font-size:1em; }}
    .mobile-only  {{ display:inline; }}
    .desktop-only {{ display:none; }}
    .reveal .controls {{ display:none !important; }}

    .doc-reference {{ margin-top:0.5em; padding-top:0.4em; }}
    .doc-label, .reveal .doc-link, a.doc-link {{ font-size:0.95em; }}

    /* ==== BOTÕES DE NAVEGAÇÃO POR TOQUE ==== */
    .mobile-nav {{
        display: flex;
        position: fixed;
        bottom: calc(6px + env(safe-area-inset-bottom, 0px));
        left: 0; right: 0;
        justify-content: space-between;
        padding: 0 8px;
        pointer-events: none;
        z-index: 100;
    }}
    .mobile-nav-btn {{
        pointer-events: auto;
        box-sizing: border-box;
        width: 44px; height: 44px;
        border-radius: 50%;
        border: 2px solid var(--laranja);
        background: rgba(11,27,43,0.88);
        color: var(--laranja);
        font-size: 26px; font-weight: 700; line-height: 1;
        padding: 0 0 3px 0;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        -webkit-tap-highlight-color: transparent;
        box-shadow: 0 2px 12px rgba(0,0,0,0.45);
        transition: transform 0.12s ease, background 0.12s ease;
        user-select: none;
        font-family: inherit;
    }}
    .mobile-nav-btn:active:not(:disabled) {{
        background: var(--laranja);
        color: #000;
        transform: scale(0.92);
    }}
    .mobile-nav-btn:disabled {{
        opacity: 0.22;
        cursor: default;
        pointer-events: none;
    }}
}}

/* ============ TELAS MUITO PEQUENAS (≤ 480px) ============ */
@media (max-width: 480px) {{
    .reveal {{ font-size:15px; }}
    .reveal h1 {{ font-size:1.4em; }}
    .reveal h2 {{ font-size:1.25em; }}
    .reveal p, .reveal li {{ font-size:1em; line-height:1.5; }}
    .slide-content {{ padding:28px 12px 52px; }}
    .two-col img {{ max-height:38vh; }}
    .metric-card {{ min-width:110px; padding:10px 12px; flex:1 1 40%; }}
    .metric-card .value {{ font-size:1.5em; }}
    .metric-card .label {{ font-size:0.72em; }}
    .contact-btn {{ font-size:0.8em; padding:8px 12px; }}
    .reveal table {{ font-size:0.8em; }}
    .reveal table th, .reveal table td {{ padding:0.4em 0.45em; }}
    .footer {{ font-size:0.72em; left:56px; right:56px; }}
}}

/* ================================================================
   LANDSCAPE COMPACTO — celular deitado (altura baixa)
   ================================================================ */
@media (orientation: landscape) and (max-height: 500px) {{
    .reveal {{ font-size:14px; }}
    .reveal h2 {{ font-size:1.25em; margin-bottom:0.3em; }}
    .reveal h3 {{ font-size:0.95em; }}
    .reveal p, .reveal li {{ font-size:0.92em; line-height:1.4; margin:0.2em 0; }}

    .slide-content {{ padding:28px 20px 52px; }}

    .two-col {{ grid-template-columns:1fr 1fr; gap:15px; }}
    .two-col img {{ max-height:56vh; }}

    .highlight-box {{ padding:8px 14px; margin:0.3em 0; }}
    .icon-list > li {{ padding:0.22em 0 0.22em 1.35em !important; }}

    .metric-grid {{ gap:10px; margin:0.4em 0; }}
    .metric-card {{ padding:8px 14px; min-width:120px; }}
    .metric-card .value {{ font-size:1.4em; }}
    .metric-card .label {{ font-size:0.7em; }}

    .slide-capa img {{ max-height:70px; }}
    .contact-btn {{ font-size:0.85em; padding:8px 14px; }}
    .footer {{ display:none; }}
    .reveal .slide-number {{ font-size:0.72em; top:8px; bottom:auto; right:8px; }}
}}
</style>
</head>
<body>
<div class="reveal">
<div class="slides">

    <!-- 1: CAPA -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)" class="slide-capa">
        <div class="slide-content">
            <img src="{logo_b64}" alt="Silvânio Góis">
            <h1>Previsão da Resistência à Compressão do Concreto</h1>
            <p class="subtitle">Otimização de Dosagem, Redução de Custos e Controle de Qualidade com Machine Learning</p>
            <p class="author">Silvânio Góis — Gestor de Operações e Negócios Orientado a Dados</p>
        </div>
        <div class="footer">
            <span class="desktop-only">Use as setas ← → para navegar · F para tela cheia · ESC para visão geral</span>
            <span class="mobile-only">Toque nas setas ou deslize para navegar</span>
        </div>
    </section>

    <!-- 2: PROBLEMA -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>O Problema</h2>
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

    <!-- 3: SOLUÇÃO -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>A Solução Proposta</h2>
            <div class="highlight-box">
                <p class="big">Modelo preditivo de <span class="accent">Machine Learning (Random Forest)</span> que estima a resistência em MPa a partir do traço e idade de cura.</p>
            </div>
            <ul class="icon-list">
                <li><span class="accent">Redução no consumo de cimento</span> sem perda de segurança estrutural</li>
                <li><span class="accent">Antecipação de decisões</span> no canteiro de obras</li>
                <li><span class="accent">Minimização de desperdícios</span> e emissões de CO₂</li>
                <li><span class="accent">Previsão em segundos</span> vs. 28 dias de espera</li>
            </ul>
        </div>
        <div class="footer">Dos dados do laboratório ao canteiro, em tempo real</div>
    </section>

    <!-- 4: DADOS -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>Os Dados de Entrada</h2>
            <p class="small">1.030 ensaios laboratoriais reais · 9 atributos · Componentes em kg/m³</p>
            <table>
                <thead><tr><th>Atributo</th><th>Descrição na Engenharia Civil</th></tr></thead>
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

    <!-- 5: METODOLOGIA -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>Metodologia</h2>
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
            <div class="doc-reference">
                <span class="doc-label">Código-fonte, dataset e metodologia detalhada:</span>
                <a class="doc-link" href="{DOC_URL}" target="_blank" rel="noopener">Documentação do Estudo →</a>
            </div>
        </div>
    </section>

    <!-- 6: HEATMAP -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>Matriz de Correlação</h2>
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

    <!-- 7: MÉTRICAS -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content center">
            <h2>Desempenho do Modelo</h2>
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

    <!-- 8: VALIDAÇÃO -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>Validação: Real vs. Predito</h2>
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

    <!-- 9: FEATURE IMPORTANCE -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>Importância das Variáveis</h2>
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

    <!-- 10: IMPACTO -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)">
        <div class="slide-content">
            <h2>Impacto Estratégico e ROI</h2>
            <div class="highlight-box">
                <h3 style="margin-top:0;">Aceleração de Cronograma</h3>
                <p>Previsão do ganho de resistência em idades jovens (3 e 7 dias), antecipando a desforma segura e liberando escoramentos.</p>
            </div>
            <div class="highlight-box">
                <h3 style="margin-top:0;">Economia Financeira</h3>
                <p>Otimização dos traços para evitar superdimensionamento preventivo do cimento.</p>
            </div>
            <div class="highlight-box">
                <h3 style="margin-top:0;">Sustentabilidade (ESG)</h3>
                <p>Menor consumo de clínquer por m³, reduzindo a pegada de carbono — indicador estratégico para relatórios de sustentabilidade.</p>
            </div>
        </div>
    </section>

    <!-- 11: CONCLUSÃO -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)" class="slide-capa">
        <div class="slide-content">
            <h2>Conclusão</h2>
            <div class="highlight-box" style="max-width:900px;margin:20px auto;">
                <p class="big">É possível prever a resistência do concreto com <span class="accent">alta confiabilidade</span> (R² ≈ 0,88) a partir do traço e da idade de cura.</p>
            </div>
            <p style="margin-top:15px;">Esta solução tem potencial para <b>transformar a gestão de qualidade</b> na construção civil:</p>
            <div style="display:flex;gap:25px;justify-content:center;margin-top:15px;font-size:1.1em;flex-wrap:wrap;">
                <span>Mais rápido</span><span>Mais barato</span><span>Mais sustentável</span>
            </div>
        </div>
    </section>

    <!-- 12: CONTATO -->
    <section data-background-gradient="linear-gradient(135deg,#0b1b2b,#14375c)" class="slide-capa">
        <div class="slide-content">
            <img src="{logo_b64}" alt="Silvânio Góis">
            <h2>Da estratégia à operação, conectando processos, pessoas e resultados</h2>
            <p class="subtitle">Gestão de Operações &amp; Análise de Dados aplicados à Engenharia Civil</p>
            <p class="author">Silvânio Góis</p>
            <div class="contact-grid">
                <a class="contact-btn" href="{DOC_URL}" target="_blank" rel="noopener">Documentação do Estudo</a>
                <a class="contact-btn" href="https://www.silvaniogois.com.br" target="_blank">Website</a>
                <a class="contact-btn" href="https://www.linkedin.com/in/silvanio-gois" target="_blank">LinkedIn</a>
                <a class="contact-btn" href="https://github.com/SilvanioSG" target="_blank">GitHub</a>
                <a class="contact-btn" href="mailto:sg@silvaniogois.com.br">E-mail</a>
            </div>
        </div>
    </section>

</div>
</div>

<!-- ============ BOTÕES DE NAVEGAÇÃO POR TOQUE (mobile) ============ -->
<div class="mobile-nav" aria-hidden="false">
    <button class="mobile-nav-btn" id="prevBtn" type="button" aria-label="Slide anterior" title="Slide anterior">‹</button>
    <button class="mobile-nav-btn" id="nextBtn" type="button" aria-label="Próximo slide" title="Próximo slide">›</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.js"></script>
<script>
/* ============================================================
   Detecção mobile: largura estreita OU altura baixa (landscape)
   ============================================================ */
function isMobileViewport() {{
    return window.matchMedia('(max-width: 900px)').matches
        || window.matchMedia('(max-height: 500px)').matches;
}}

const isMobile = isMobileViewport();

const config = {{
    hash: true,
    slideNumber: 'c/t',
    transition: 'slide',
    transitionSpeed: 'default',
    backgroundTransition: 'fade',
    progress: true,
    center: false,
    keyboard: true,
    overview: !isMobile,
    touch: true,
    loop: false,
    controls: !isMobile,
}};

if (isMobile) {{
    config.width  = Math.max(320, Math.round(document.documentElement.clientWidth));
    config.height = Math.max(320, Math.round(window.innerHeight));
    config.margin = 0;
    config.minScale = 0.5;
    config.maxScale = 1.2;
}} else {{
    config.width  = 1280;
    config.height = 720;
    config.margin = 0.02;
    config.minScale = 0.2;
    config.maxScale = 1.6;
}}

Reveal.initialize(config);

/* ============================================================
   AUTO-FIT — apenas desktop (mobile usa scroll nativo)
   ============================================================ */
function autoFitSlides() {{
    if (isMobileViewport()) {{
        document.querySelectorAll('.reveal .slides section .slide-content')
            .forEach(el => {{ el.style.transform = ''; }});
        return;
    }}
    document.querySelectorAll('.reveal .slides section').forEach(section => {{
        const content = section.querySelector('.slide-content');
        if (!content) return;
        content.style.transform = '';
        content.style.width = '';
        void content.offsetHeight;
        const availH = section.clientHeight;
        const needH  = content.scrollHeight;
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

window.addEventListener('orientationchange', () => {{
    if (isMobileViewport()) location.reload();
}});

/* ============================================================
   BOTÕES DE NAVEGAÇÃO POR TOQUE
   - Chamam a API pública do Reveal (prev/next)
   - Estado desabilitado reflete availableRoutes()
   ============================================================ */
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

if (prevBtn) prevBtn.addEventListener('click', () => Reveal.prev());
if (nextBtn) nextBtn.addEventListener('click', () => Reveal.next());

function updateMobileNav() {{
    if (!prevBtn || !nextBtn) return;
    const routes = Reveal.availableRoutes();
    prevBtn.disabled = !(routes.left || routes.up);
    nextBtn.disabled = !(routes.right || routes.down);
}}

Reveal.on('ready', updateMobileNav);
Reveal.on('slidechanged', updateMobileNav);
</script>
</body>
</html>
"""

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"Apresentação gerada: {OUTPUT}")
print(f"Tamanho: {os.path.getsize(OUTPUT)/1024:.1f} KB")
print("Setas por toque · botão doc consistente · landscape corrigido")