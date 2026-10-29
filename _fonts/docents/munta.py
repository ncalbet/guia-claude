"""Munta la guia per als docents a partir de l'esquelet de la Guia 1 (estil, navegació i Shenron)."""
import base64, re
from pathlib import Path

AQUI = Path(__file__).parent
ARREL = AQUI.parent.parent  # l'arrel del repo guia-claude
ORIGEN = ARREL / "guia-1" / "index.html"
DESTI = ARREL / "docents" / "index.html"

html = ORIGEN.read_text(encoding="utf-8")
noves = (AQUI / "diapositives.html").read_text(encoding="utf-8")

ini = html.index("<!-- ============ PORTADA ============ -->")
fi = html.index("  </main>")
html = html[:ini] + noves + "\n" + html[fi:]

CSS_NOU = """
/* Guia per a docents */
.targeta.vermell{border-top:10px solid var(--vermell)}
.tasques{gap:14px 20px}
.tasques .targeta p{margin:4px 0}
.tasques .que{color:var(--gris);font-style:italic}
.tasques .teu{border-top:2px dashed #e0d5bf;padding-top:5px}
.revises{margin:-2px 0 12px 4px;color:var(--gris)}
.revises b{color:var(--verd)}
ol.passos.tres>li{font-size:clamp(17px,1.9vw,22px);font-weight:800;margin:14px 0}

/* Obertura de cada prova: el camí del torneig */
.panel.obertura{background:none;border:0;box-shadow:none;color:#fff;text-align:center}
.obertura .kicker{color:var(--groc);font-size:clamp(18px,2.2vw,24px)}
.cami{position:relative;display:flex;justify-content:center;gap:clamp(4px,1.4vw,20px);margin:4px auto 0;max-width:980px}
.cami::before{content:"";position:absolute;left:7%;right:7%;top:50px;border-top:3px dashed rgba(255,255,255,.4)}
.fita{position:relative;display:flex;flex-direction:column;align-items:center;gap:4px;min-width:0}
.fita .b{height:100px;display:flex;align-items:center}
.fita .nom{font-family:var(--titol);letter-spacing:1px;font-size:clamp(12px,1.35vw,16px);color:#cfd8ee;white-space:nowrap}
.fita.guanyada .nom::after{content:" ✓";color:#9be37f}
.fita.falta svg{opacity:.3;filter:grayscale(1)}
.fita.falta .nom{opacity:.55}
.fita.enjoc .b{filter:drop-shadow(0 0 18px rgba(255,210,63,.9))}
.fita.enjoc .nom{color:var(--groc);font-size:clamp(15px,1.8vw,20px)}
.panel h2.titol-obertura{font-family:var(--titol);font-weight:400;font-size:clamp(32px,4.8vw,58px);line-height:1.05;color:var(--taronja);
  -webkit-text-stroke:2px var(--tinta);text-shadow:4px 4px 0 var(--tinta);letter-spacing:2px;margin:8px 0 16px}
.promesa{max-width:920px;margin:0 auto 12px;text-align:left;color:var(--tinta)}
.promesa .targeta p{font-size:clamp(15px,1.55vw,18px)}
@media (max-width:820px){
  .fita .b{height:64px}
  .cami::before{top:32px}
  .fita svg{width:30px;height:30px}
  .fita.enjoc svg{width:62px;height:62px}
  .fita .nom{display:none}
  .fita.enjoc .nom{display:block}
}
@media print{
  .panel.obertura,.fita .nom{color:var(--tinta)}
  .cami::before{border-color:#999}
}

/* Bola 6: nivells, galeria amb fitxes i idees */
.nivells{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:8px 0 6px}
.nivells .pw h3{font-family:var(--titol);font-weight:400;letter-spacing:1px;font-size:clamp(20px,2.2vw,26px);color:var(--blau)}
.nivells .que{font-weight:800;color:var(--taronja);margin:2px 0 4px}
.nivells .pw:nth-child(2){box-shadow:0 0 24px rgba(255,190,30,.95)}
.nivells .pw:nth-child(3){box-shadow:0 0 38px rgba(255,160,0,1);background:linear-gradient(180deg,#ffe27a,#fff 75%)}
.galeria{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin:6px 0 4px}
.obra{width:clamp(140px,16.5vw,196px);background:#fff;border:3px solid var(--tinta);border-radius:12px;padding:0;cursor:pointer;
  text-align:left;overflow:hidden;font:inherit;color:var(--tinta);box-shadow:4px 4px 0 var(--tinta);transition:transform .15s,box-shadow .15s}
.obra:hover,.obra:focus-visible{transform:translateY(-4px);box-shadow:6px 8px 0 var(--tinta)}
.obra img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top;border-bottom:3px solid var(--tinta)}
.obra b{display:block;padding:6px 10px 0;font-size:clamp(13.5px,1.3vw,15px);line-height:1.25}
.obra small{display:block;padding:1px 10px 8px;color:var(--gris);font-size:clamp(12px,1.1vw,13px)}
dialog.fitxa{width:min(760px,94vw);max-height:92vh;padding:0;border:4px solid var(--tinta);border-radius:14px;
  box-shadow:8px 8px 0 var(--tinta);background:var(--paper);color:var(--tinta)}
dialog.fitxa::backdrop{background:rgba(8,17,41,.85)}
.fitxa-in{position:relative;padding:clamp(16px,2.4vw,26px);text-align:left}
.fitxa-img{display:block;width:100%;height:clamp(130px,25vh,220px);object-fit:cover;object-position:top;border:3px solid var(--tinta);border-radius:10px;margin:0 0 10px}
.panel .fitxa h3{font-family:var(--titol);font-weight:400;letter-spacing:1px;font-size:clamp(24px,3vw,34px);color:var(--blau);margin:2px 0 6px}
.tanca-fitxa{position:absolute;top:8px;right:8px;z-index:1;width:38px;height:38px;border-radius:50%;border:3px solid var(--tinta);
  background:var(--groc);font-size:18px;font-weight:800;cursor:pointer;line-height:1}
.fitxa .enllac{font-weight:700}
.idees{gap:12px 16px}
.idees .targeta{padding:8px 14px}
.idees .targeta p{margin:3px 0;font-size:clamp(13.5px,1.3vw,15.5px)}
.idees .teu{border-top:2px dashed #e0d5bf;padding-top:4px;color:var(--gris)}
.rapids .cmd{margin:6px 0 10px}
.rapids .cmd code{font-size:clamp(12.5px,1.2vw,14px)}
.rapids h3{margin:8px 0 2px}
@media (max-width:820px){
  .nivells{grid-template-columns:1fr}
  .obra{width:calc(50% - 8px)}
}
@media print{
  .obra{box-shadow:none}
}
"""

JS_NOU = """
  // Obertura de cada prova: el camí del torneig, amb les boles guanyades i la que està en joc
  document.querySelectorAll('[data-cami]').forEach(function(el){
    var n = +el.dataset.cami, h = '';
    for (var k = 1; k <= 7; k++){
      var estat = k < n ? 'guanyada' : (k === n ? 'enjoc' : 'falta');
      h += '<div class="fita ' + estat + '"><span class="b' + (k === n ? ' sura' : '') + '">' + bola(k, k === n ? 96 : 50) +
           '</span><span class="nom">' + SAGUES[k].curt + '</span></div>';
    }
    el.innerHTML = h;
  });
  document.querySelectorAll('[data-pantalles]').forEach(function(el){
    var s = el.dataset.pantalles, n = 0;
    slides.forEach(function(sl){ if (sl.dataset.saga === s && !sl.dataset.trobada && !sl.dataset.obertura) n++; });
    el.textContent = n + (n === 1 ? ' pantalla' : ' pantalles') + ' i la bola és teva ▶';
  });
  // Galeria de la bola 6: cada captura obre la seva fitxa
  document.querySelectorAll('[data-fitxa]').forEach(function(b){
    b.addEventListener('click', function(){
      var d = document.getElementById(b.dataset.fitxa);
      if (!d || !d.showModal) return;
      var im = d.querySelector('.fitxa-img');
      if (im && !im.getAttribute('src')) im.src = b.querySelector('img').src;
      d.showModal();
    });
  });
  document.querySelectorAll('dialog.fitxa').forEach(function(d){
    d.addEventListener('click', function(e){ if (e.target === d || e.target.closest('.tanca-fitxa')) d.close(); });
  });
"""
OBERTA = "document.querySelector('dialog.fitxa[open]')"
ANCORA_JS = """    for (var k = 1; k <= 7; k++) h += bola(k, 46, k <= n ? '' : 'falta');
    el.innerHTML = h;
  });
"""

CANVIS = [
    ("<title>Guia Claude Code</title>", "<title>IA per a docents</title>"),
    ("🏆 Torneig de les Arts Marcials", "🏆 Torneig de les Arts Docents"),
    ("</style>\n</head>", CSS_NOU + "</style>\n</head>"),
    ("""    1:{nom:"Inscripció al torneig", curt:"Inscripció"},
    2:{nom:"Preparació: la instal·lació", curt:"Instal·lació"},
    3:{nom:"Entrenament amb el Follet Tortuga", curt:"Entrenament"},
    4:{nom:"La tècnica secreta: el mètode", curt:"El mètode"},
    5:{nom:"Super Guerrer: millores", curt:"Super Guerrer"},
    6:{nom:"Mongetes màgiques: problemes", curt:"Problemes"},
    7:{nom:"El radar del drac: xuleta", curt:"Xuleta"}""",
     """    1:{nom:"Inscripció: les quatre tasques", curt:"El mapa"},
    2:{nom:"Preparació: l'aplicació", curt:"L'aplicació"},
    3:{nom:"Entrenament: la carpeta de feina", curt:"La carpeta"},
    4:{nom:"El reglament: les instruccions fixes", curt:"Instruccions"},
    5:{nom:"La tècnica secreta: com encarregar", curt:"Com demanar"},
    6:{nom:"Super Guerrer: de l'encàrrec al projecte", curt:"Projectes"},
    7:{nom:"Mongetes màgiques: revisar i resoldre", curt:"Revisar"}"""),
    ("""if (sg === 0) return "Guia d'iniciació a Claude Code";""",
     """if (sg === 0) return "Guia pràctica per a docents";"""),
    ("return 'Extra · Com recorda Claude';", "return 'Extra';"),
    (ANCORA_JS, ANCORA_JS + JS_NOU),
    # amb una fitxa oberta, les tecles i el dit no passen pantalla
    ("    if (index.classList.contains('oberta')){ if (e.key === 'Escape') tancaIndex(); return; }",
     "    if (" + OBERTA + ") return;\n"
     "    if (index.classList.contains('oberta')){ if (e.key === 'Escape') tancaIndex(); return; }"),
    ("    if (tx === null) return;",
     "    if (tx === null) return;\n"
     "    if (" + OBERTA + "){ tx = ty = null; return; }"),
]
for vell, nou in CANVIS:
    n = html.count(vell)
    assert n == 1, f"{n} aparicions de: {vell[:60]}"
    html = html.replace(vell, nou)

# Captures de la galeria, dins del fitxer
html = re.sub(r'src="obra:([a-z]+)"',
              lambda m: 'src="data:image/jpeg;base64,' +
              base64.b64encode((AQUI / "obres" / (m.group(1) + ".jpg")).read_bytes()).decode() + '"', html)
assert 'src="obra:' not in html

DESTI.write_text(html, encoding="utf-8")
print("fet:", DESTI, len(html), "caràcters")
