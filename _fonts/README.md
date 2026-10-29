# Fonts de les guies

GitHub Pages no publica les carpetes que comencen per `_`: aquesta carpeta és al repo, però no a la web.

## Què és cada cosa

| Adreça | Fitxer | Com es fa |
|---|---|---|
| `/` | `index.html` | La portada. S'edita directament. Si l'adreça porta `#N`, salta a `guia-1/#N` (enllaços vells). |
| `/guia-1/` | `guia-1/index.html` | La Guia 1. S'edita directament. És també l'esquelet de la guia per a docents. |
| `/guia-2/` | `guia-2/index.html` | La Guia 2. S'edita directament. |
| `/docents/` | `docents/index.html` | **No s'edita a mà**: es munta amb `_fonts/docents/munta.py`. |
| `/guia-2.html` | `guia-2.html` | Redirecció a `guia-2/` (l'adreça va estar publicada unes hores el 29/10/2026). |

## La guia per a docents

- `docents/diapositives.html`: el contingut (les pantalles).
- `docents/obres/*.jpg`: les captures de la galeria de la bola 6. La de Crisi energètica està retallada
  perquè no s'hi vegi el nom del centre: mira qualsevol captura nova abans de pujar-la.
- `docents/munta.py`: agafa l'estil, la navegació i l'animació de Shenron de `guia-1/index.html`, hi posa el
  contingut i les captures, i escriu `docents/index.html`.

Per refer-la: `python _fonts/docents/munta.py`. Si canvies la Guia 1 (estil, capçalera, Índex o Shenron),
torna-la a muntar perquè la guia per a docents també ho tingui.

## L'animació de Shenron

`shenron/shenron.html` és l'animació sola, per obrir-la i provar-la; `shenron.html?t=4.5` la congela en
aquell segon (així es van treure els fotogrames de `shenron/fotogrames.png`). A les guies hi va copiada
dins de `<template id="shenron-src">` (a `guia-1/index.html` i `guia-2/index.html`; la de docents l'agafa
de la Guia 1). Si la canvies, torna-la a copiar a totes dues i remunta la de docents.
`shenron/integracio.html` és un exemple de com incrustar-la en una altra pàgina.

Com és (29/10/2026): les boles es carreguen i el cel s'enfosqueix; un llampec i una columna de llum; un
cometa de llum surt del centre de l'anell i recorre el camí del cos (`#coil`), i el cos es fa darrere seu;
el cap neix d'un esclat i se li encenen els ulls; les boles es buiden. El cos del drac no és un dibuix fix:
el JS el genera a partir de `#coil` (amplada, panxa, escates, cresta i potes).
