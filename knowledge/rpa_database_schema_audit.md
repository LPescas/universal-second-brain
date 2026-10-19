# Auditoria de Schema de Banco de Dados: db_rpa

> Documentação gerada automaticamente para refletir o estado exato da arquitetura agnóstica.

## Estrutura de Tabelas

### paciente_documentos
| Coluna | Tipo |
|---|---|
| id | int |
| paciente_id | int |
| tipo | enum('LAUDO','RELATORIO') |
| nome_arquivo | varchar(255) |
| arquivo | longblob |
| data_upload | datetime |
| data_validade | date |
| status | enum('VALIDO','VENCIDO','PENDENTE') |


### tb_agenda_semanal
| Coluna | Tipo |
|---|---|
| id | int |
| paciente_id | int |
| terapia_code | varchar(20) |
| dia_semana | enum('SEG','TER','QUA','QUI','SEX') |
| quantidade | int |
| ativo | tinyint(1) |
| created_at | datetime |
| updated_at | datetime |
| profissional_id | int |


### tb_configuracoes_empresa
| Coluna | Tipo |
|---|---|
| id | int |
| chave | varchar(100) |
| valor | longtext |
| tipo | enum('cor','fonte','imagem','texto','json') |
| descricao | varchar(255) |
| updated_at | timestamp |


### tb_emissao_overrides
| Coluna | Tipo |
|---|---|
| id | int |
| paciente_id | int |
| terapia_code | varchar(20) |
| quantidade | int |
| dia_semana | varchar(3) |
| data_referencia | date |
| tipo_override | varchar(20) |
| criado_em | datetime |
| criado_por | varchar(100) |
| consumido | tinyint(1) |
| ativo | tinyint(1) |


### tb_evolutivo_historico_obs
| Coluna | Tipo |
|---|---|
| id | int |
| paciente_id | int |
| terapia_code | varchar(20) |
| observacao_id | int |
| data_uso | date |
| criado_em | datetime |


### tb_evolutivo_log
| Coluna | Tipo |
|---|---|
| id | int |
| data_execucao | date |
| dia_semana | varchar(3) |
| profissional_id | int |
| profissional_nome | varchar(200) |
| paciente_id | int |
| paciente_nome | varchar(200) |
| terapia_code | varchar(20) |
| observacao_id | int |
| status | varchar(20) |
| mensagem | text |
| criado_em | datetime |


### tb_guias_sem_acao
| Coluna | Tipo |
|---|---|
| id | int |
| data_solicitacao | date |
| paciente_nome | varchar(255) |
| guia_numero | varchar(100) |
| status | varchar(50) |
| data_registro | timestamp |


### tb_lista_de_pedidos
| Coluna | Tipo |
|---|---|
| order_number | varchar(255) |
| order_password | varchar(255) |
| request_date | date |
| status | varchar(255) |
| recipient | varchar(255) |
| authorization_date | date |
| treatment | varchar(50) |
| inserted_at | timestamp |
| record_status | varchar(255) |
| record_description | varchar(255) |
| record_date | timestamp |
| crm | varchar(100) |
| uf | varchar(100) |
| price | varchar(20) |


### tb_log_lancamentos
| Coluna | Tipo |
|---|---|
| id | int |
| paciente_id | int |
| terapia_code | varchar(20) |
| dia_semana | varchar(3) |
| data_lancamento | date |
| quantidade | int |
| status | enum('SUCESSO','ERRO','BLOQUEADO','DUPLICADO') |
| origem | varchar(50) |
| mensagem | text |
| id_registro_proc | int |
| created_at | datetime |


### tb_logs_atividade
| Coluna | Tipo |
|---|---|
| id | int |
| usuario_id | int |
| data_hora | datetime |
| rpa_nome | varchar(50) |
| pedido | text |
| resultado | text |
| tipo | varchar(20) |


### tb_observacoes_evolutivo
| Coluna | Tipo |
|---|---|
| id | int |
| terapia_code | varchar(20) |
| terapia_nome | varchar(200) |
| texto_observacao | text |
| ativo | tinyint(1) |
| criado_em | datetime |


### tb_pacientes
| Coluna | Tipo |
|---|---|
| ID | int |
| Nome | varchar(100) |
| numero_Beneficiario | varchar(20) |
| Conselho | varchar(10) |
| Uf_conselho | char(2) |
| Numero_Conselho | varchar(20) |
| CBOS | varchar(10) |
| Nome_Medico | varchar(100) |
| inserted_at | datetime |
| updated_at | datetime |
| ativo | tinyint(1) |
| Data_nascimento | date |


### tb_parametros_de_terapia
| Coluna | Tipo |
|---|---|
| code | varchar(50) |
| description | varchar(255) |
| price | varchar(20) |
| last_update | timestamp |


### tb_pesquisa_consolidacao
| Coluna | Tipo |
|---|---|
| id | int |
| num_pedido | varchar(30) |
| data_solicitacao | date |
| data_autorizacao | date |
| numero_Beneficiario | varchar(20) |
| Nome | varchar(255) |
| mes_referencia | varchar(7) |
| criado_em | timestamp |
| atualizado_em | timestamp |


### tb_procedimentos_pacientes
| Coluna | Tipo |
|---|---|
| id_registro | int |
| Data | date |
| Quantidade | int |
| id_procedimento | varchar(20) |
| situacao | varchar(15) |
| obs_erro | varchar(500) |
| ID | int |
| inserted_at | datetime |
| updated_at | datetime |


### tb_profissionais
| Coluna | Tipo |
|---|---|
| id | int |
| nome | varchar(255) |
| email | varchar(150) |
| conselho | varchar(50) |
| numero_conselho | varchar(100) |
| evolutivo_email | varchar(150) |
| evolutivo_senha | varchar(150) |
| ativo | tinyint(1) |
| created_at | datetime |
| updated_at | datetime |


### tb_profissional_especialidades
| Coluna | Tipo |
|---|---|
| id | int |
| profissional_id | int |
| terapia_code | varchar(20) |
| criado_em | datetime |


### tb_profissional_pacientes
| Coluna | Tipo |
|---|---|
| id | int |
| profissional_id | int |
| paciente_id | int |
| criado_em | datetime |


### tb_rpa_facial
| Coluna | Tipo |
|---|---|
| id | int |
| order_number | varchar(50) |
| status | varchar(100) |
| data_processamento | timestamp |


### tb_rpa_token_pendente
| Coluna | Tipo |
|---|---|
| id | int |
| order_number | varchar(50) |
| data_solicitacao | varchar(50) |
| token_value | varchar(20) |
| status | varchar(20) |
| data_processamento | timestamp |


### tb_usuarios
| Coluna | Tipo |
|---|---|
| id | int |
| nome | varchar(100) |
| email | varchar(100) |
| senha_hash | varchar(255) |
| is_admin | tinyint(1) |
| permissoes | json |
| status_conexao | tinyint(1) |
| ultimo_acesso | datetime |


### tp_rpa_facial
| Coluna | Tipo |
|---|---|
| id | int |
| order_number | varchar(50) |
| status | varchar(100) |
| data_solicitacao | varchar(50) |
| data_processamento | timestamp |


### 2026-08-16 Update: tb_rpa_token_pendente
Adicionadas colunas numero_beneficiario e nome_paciente para armazenar os dados do beneficiario logo durante a captura, evitando necessidade de JOIN.


## Atualização de CIDs e Procedimentos (2026-08-24)
- Criada a tabela tb_cids (id, cid_code)
- Criada a tabela tb_cid_procedimentos (cid_id, terapia_code)
- Removida a coluna CID de tb_pacientes
- Adicionada coluna sigla à tb_parametros_de_terapia


## Atualização 24/08/2026
- Nova tabela: 	b_medicos (id, nome_completo, conselho, uf_conselho, numero_conselho, cbos)
- Nova tabela: 	b_paciente_medicos (id_paciente, id_medico)
- Nova tabela: 	b_laudos (id, id_paciente, id_medico, cid, data_laudo, nome_arquivo)
- Alteração: Adicionada coluna id_laudo na tabela 	b_procedimentos_pacientes.
- Alteração: Adicionada coluna id_laudo na tabela 	b_agenda_semanal.


## Atualização 2026-08-24 21:50:08
Adicionadas colunas na tabela db_rpa.paciente_documentos:
- id_medico INT NULL (Para vínculos de laudos com médicos específicos)
- id_laudo INT NULL (Para vínculos de relatórios com laudos específicos)
- 	ipo_vinculo VARCHAR(50) NULL DEFAULT 'COMPLETO' (Para indicar o escopo de um documento, ex: COMPLETO, MEDICO, LAUDO)

## Atualizacao Automatica (Agente IA) - 05/10/2026

- **tb_reemissao_guias**: (Nova tabela) Armazena os metadados de pedidos de reemissao manual feitos no sistema.
  - Campos: id, id_registro (FK tb_procedimentos_pacientes), paciente_id, id_procedimento, numero_pedido_antigo, data_solicitacao_antiga, data_reemissao, criado_por, criado_em
  - Ligações: id_registro relaciona-se a tb_procedimentos_pacientes; paciente_id relaciona-se a tb_pacientes. A finalidade é guardar dados da reemissão (pedido cancelado anteriormente) que serão injetados pelo RPA de Emissão na aba Observações do portal, mantendo a emissão vinculada ao dia corrente (para evolutivos) mas informando que é uma guia antiga.
A l t e r a � � o :   A d i c i o n a d a   c o l u n a   ' o b s e r v a c a o '   ( T E X T )   n a   t a b e l a   t b _ r e e m i s s a o _ g u i a s   n o   d b _ r p a .  
 A l t e r a � � o :   A d i c i o n a d a   c o l u n a   ' n u m e r o _ g u i a '   ( V A R C H A R   5 0 )   n a   t a b e l a   t b _ p r o c e d i m e n t o s _ p a c i e n t e s   n o   d b _ r p a   p a r a   r e g i s t r a r   a   g u i a   g e r a d a   ( h i s t � r i c o   n o r m a l ) .  
 A l t e r a � � o :   A d i c i o n a d a   t a b e l a   t b _ c a p t a c a o _ c a n c e l a d a s   n o   d b _ r p a   p a r a   a r m a z e n a r   r e l a t � r i o s   d e   g u i a s   c a n c e l a d a s  
 