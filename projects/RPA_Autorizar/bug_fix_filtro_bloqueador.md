# Bug Fix v2.5 - Filtro Bloqueando Guias Pre-autorizadas

## Data: 2026-09-03

## Sintoma
- RPA processou 126 guias mas portal ainda mostrava 309 pre-autorizadas
- 182 guias foram ignoradas pelo filtro _filter_pre_authorized
- Problema intercalado (nao era limite de server) - guias espalhadas por toda lista

## Root Cause: Banco como Bloqueador Incorreto
A funcao _filter_pre_authorized consultava tp_rpa_facial e pulava guias marcadas
como Reconhecimento Facial Finalizado no banco. Porem, o banco registrava Finalizado
mesmo quando a confirmacao falhava silenciosamente no portal (timeout, modal nao fechou,
erro de rede). Resultado: 182 guias ficavam bloqueadas no banco mas o portal ainda
as exibia como Pre-autorizado.

## Confirmacao pelo Banco
- 182 guias ausentes do RPA -> TODAS em tp_rpa_facial com status Finalizado
- Mas portal mostrava Pre-autorizado para TODAS elas
- Processadas entre 18/08 e 03/09 (execucoes anteriores com falha silenciosa)

## Correcao v2.5
O filtro nao usa mais o banco como bloqueador.
- Se portal diz Pre-autorizado -> SEMPRE processa (portal e a fonte da verdade)
- Banco continua sendo consultado MAS apenas para log diagnostico
- Status Autorizado/Negado no portal -> pula (confirmacao externa)
- Aviso especial no log quando banco diz Finalizado mas portal diz Pre-autorizado

## Impacto Esperado
Proxima execucao deve capturar todas as 309 guias restantes.

## Tabelas do Banco Relevantes
- tp_rpa_facial: order_number, status, data_solicitacao, data_processamento
- tb_rpa_facial: order_number, status, data_processamento (outra tabela - nao usada no filtro)
- tb_rpa_token_pendente: guias aguardando token
- tb_guias_sem_acao: guias sem acao possivel
