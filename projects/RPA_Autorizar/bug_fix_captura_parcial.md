# Bug Fix v2.4 - Captura Parcial de Guias Pre-autorizadas
Data: 2026-09-03

## Sintoma
- RPA rodou 14/08/2026 a 02/09/2026
- 361 guias Pre-autorizado no periodo (confirmado pelo Excel)
- RPA capturou apenas 187 (bug)

## Root Cause: 3 Bugs Combinados

### BUG 1 (CRITICO) - set_date_with_keys nao disparava eventos DOM
O campo data do portal ASP era preenchido sem disparar change/blur.
O datepicker ASP ignorava o valor e pesquisava SEM filtro de data,
retornando apenas os primeiros ~187 registros hardcoded no servidor.
CORRECAO: set_date_with_events dispara input+change+blur via JS.

### BUG 2 - Extracao prematura da tabela
Loop detectava 1 celula e extraia antes de todos os registros carregarem.
CORRECAO: aguarda tabela ESTABILIZAR (3 rounds sem crescimento = 6 segundos).

### BUG 3 - &nbsp; nao era removido do status  
Portal retorna U+00A0 antes dos valores. Filtro pre-autorizado podia falhar.
CORRECAO: cleanText() faz replace(U+00A0, espaco) em todos os campos.

## Licao Aprendida
Portais ASP legado com datepicker PRECISAM ter change+blur disparados via JS.
Apenas send_keys do Selenium nao e suficiente nesses portais.

## Status: Corrigido e validado sintaticamente em 2026-09-03
