#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_ai_guides.py -- Gerador de Manuais Universais AI_GUIDE.md para o Hub
=============================================================================
Gera arquivos AI_GUIDE.md completos, estruturados e em conformidade estrita com
a Seção 4 do plano de expansão do Second Brain, legíveis tanto por humanos quanto
por qualquer agente de IA (Claude, Gemini, Antigravity, Ollama, OpenAI, GLM).
"""
import sys
import io
from pathlib import Path

# Força UTF-8 no Windows
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")
REPOS_ROOT = SB_ROOT / "repos"

REPOS_META = {
    "VoiceStudio": {
        "rel_dir": "media_processing/VoiceStudio",
        "category": "media_processing",
        "tokens_efficiency": "Alto - Evita chamadas caras a APIs comerciais de síntese e clonagem de voz.",
        "triggers": ["voz", "áudio", "som", "tts", "clonagem vocal", "síntese de voz", "audiodescrição", "narração"],
        "summary": "Estúdio unificado de áudio e síntese vocal com múltiplos motores neurais de ponta (F5-TTS, CosyVoice, ChatTTS) e interface Gradio integrada.",
        "benefits": [
            "Geração de alertas sonoros e leitura automática de relatórios em pipelines de RPA.",
            "Gravação e dublagem automatizada para tutoriais e demonstrações do WRPE_Recorder.",
            "Execução 100% offline e local, garantindo sigilo absoluto de gravações e dados sensíveis."
        ],
        "usage_cli": "python launch.py  # ou scripts específicos de inferência tts",
        "usage_python": """from repos.media_processing.VoiceStudio import synthesize
# Exemplo conceitual de inferência local
synthesize(text="Execução da guia RPA finalizada com sucesso.", voice_preset="pt_br_female")""",
        "tokens_rules": "Consuma apenas os metadados do áudio gerado e os logs de conclusão; nunca leia arquivos binários de áudio diretamente no contexto do LLM."
    },
    "editonny": {
        "rel_dir": "media_processing/editonny",
        "category": "media_processing",
        "tokens_efficiency": "Alto - Substitui edição manual de mídia por pipelines declarativos e scripts automatizados.",
        "triggers": ["edição de vídeo", "cortar vídeo", "legendas automáticas", "transcodificar mídia", "gravar tela"],
        "summary": "Ferramenta de edição de vídeo e mídia potencializada por IA, gerando cortes inteligentes, sincronização labial, filtros e legendas automatizadas.",
        "benefits": [
            "Edição e corte automático das gravações de automações do WRPE_Recorder.",
            "Geração de evidências em vídeo enxutas para auditoria de falhas em execuções de robôs.",
            "Compressão e otimização de mídias antes do envio para clientes ou armazenamento em nuvem."
        ],
        "usage_cli": "python -m editonny --input video.mp4 --cut-silence --subtitle",
        "usage_python": """from repos.media_processing.editonny import VideoPipeline
pipe = VideoPipeline("gravacao_rpa.mp4")
pipe.remove_silence().generate_subtitles(lang="pt").export("evidencia_final.mp4")""",
        "tokens_rules": "Transfira apenas comandos de processamento e consulte o relatório de cortes; não injete streams de vídeo em base64."
    },
    "diagram-design": {
        "rel_dir": "media_processing/diagram-design",
        "category": "media_processing",
        "tokens_efficiency": "Máximo - Fornece padrões visuais estruturados (Mermaid/ASCII) que consomem pouquíssimos tokens.",
        "triggers": ["diagrama", "arquitetura visual", "fluxo", "flowchart", "mermaid", "blueprint visual"],
        "summary": "Guia de design, convenções e templates prontos para criação de diagramas técnicos legíveis, claros e padronizados.",
        "benefits": [
            "Documentação padronizada do banco de dados RPA e ligações relacionais.",
            "Mapeamento do fluxo de telas do WRPE_Recorder em fluxogramas compreensíveis.",
            "Ilustração de arquiteturas multi-agente sem sobrecarregar a memória de contexto."
        ],
        "usage_cli": "Consulte os templates em diagram-design/templates/ para reutilizar estruturas prontas.",
        "usage_python": """# Utilize os padrões de sintaxe Mermaid auditados para gerar documentações
mermaid_code = \"\"\"graph TD
    A[Início RPA] --> B{Valida Certificado?}
    B -->|Sim| C[Acessa Portal]
    B -->|Não| D[Gera Alerta]\"\"\" """,
        "tokens_rules": "Gere blocos ```mermaid compactos seguindo a sintaxe do repositório, evitando prolixidade desnecessária."
    },
    "paperclip": {
        "rel_dir": "media_processing/paperclip",
        "category": "media_processing",
        "tokens_efficiency": "Alto - Converte layouts e capturas de tela diretamente em código limpo sem retrabalho manual.",
        "triggers": ["screenshot para código", "imagem para html", "converter tela", "extrair ui", "mock to code"],
        "summary": "Extrator visual e transpilador que converte imagens de interface, telas legadas e mockups diretamente em código frontend funcional.",
        "benefits": [
            "Conversão rápida de formulários de sistemas legados capturados pelo RPA em telas web modernas.",
            "Reconstrução ágil de componentes de interface para o dashboard do Second Brain.",
            "Economia de horas de desenvolvimento frontend na prototipagem."
        ],
        "usage_cli": "python paperclip.py --image tela_sistema.png --output-format html-tailwind",
        "usage_python": """from repos.media_processing.paperclip import ScreenParser
ui = ScreenParser.parse_image("tela_legado.png")
html = ui.to_clean_html()""",
        "tokens_rules": "Envie imagens apenas uma vez e consuma a árvore DOM/HTML estruturada retornada."
    },
    "rea": {
        "rel_dir": "dev_reverse_engineering/rea",
        "category": "dev_reverse_engineering",
        "tokens_efficiency": "Alto - Faz engenharia reversa sem depender de decompiladores comerciais complexos.",
        "triggers": ["engenharia reversa", "descompilar", "analisar dll", "binário", "protocolo legado", "exe", "disasm"],
        "summary": "Ambiente de engenharia reversa e análise de binários assistida por Inteligência Artificial, gerando descompilações compreensíveis e mapeamento de chamadas.",
        "benefits": [
            "Análise de telas e protocolos de comunicação de sistemas desktop antigos automatizados pelo RPA.",
            "Descoberta de parâmetros ocultos em DLLs e executáveis de terceiros.",
            "Inspeção de binários e segurança de dependências locais."
        ],
        "usage_cli": "python rea.py analyze --target app_antigo.exe --output relatorio_re.json",
        "usage_python": """from repos.dev_reverse_engineering.rea import BinaryAnalyzer
analyzer = BinaryAnalyzer("modulo_nativo.dll")
functions = analyzer.extract_exported_symbols()""",
        "tokens_rules": "Extraia somente assinaturas de funções e blocos de descompilação de interesse estrito para economizar contexto."
    },
    "ECC": {
        "rel_dir": "dev_reverse_engineering/ECC",
        "category": "dev_reverse_engineering",
        "tokens_efficiency": "Máximo - Elimina tentativas e erros fornecendo comandos exatos e flags de produtividade.",
        "triggers": ["claude code", "cli prompt", "flags claude", "comando avançado", "automação cli"],
        "summary": "Everything Claude Code (ECC): Coletânea de melhores práticas, prompts de sistema, flags CLI, scripts utilitários e automações para assistentes de terminal.",
        "benefits": [
            "Padronização de comandos para o ecossistema do Claude e Antigravity.",
            "Workflows comprovados para automação de tarefas repetitivas de desenvolvimento.",
            "Redução de chamadas desnecessárias através de atalhos e padrões de prompt."
        ],
        "usage_cli": "cat repos/dev_reverse_engineering/ECC/prompts/*.md",
        "usage_python": "# Consulte os templates de prompt e utilize diretamente nas instruções de sistema",
        "tokens_rules": "Leia seções pontuais dos guias do ECC sem despejar todos os manuais no prompt."
    },
    "vibe-coding-toolkit": {
        "rel_dir": "dev_reverse_engineering/vibe-coding-toolkit",
        "category": "dev_reverse_engineering",
        "tokens_efficiency": "Alto - Fornece scaffolds e snippets testados que evitam reinventar a roda.",
        "triggers": ["vibe coding", "protótipo rápido", "boilerplate ágil", "scaffold rápido", "mvp"],
        "summary": "Caixa de ferramentas para desenvolvimento ágil ('Vibe Coding'), com boilerplates, utilitários modulares e atalhos para implementação relâmpago de features.",
        "benefits": [
            "Criação ultrarrápida de scripts de suporte e ferramentas auxiliares.",
            "Boilerplates limpos para testes de novas ideias em minutos.",
            "Padronização de código moderno sem over-engineering."
        ],
        "usage_cli": "python -m vibe_coding scaffold --type script --name novo_modulo",
        "usage_python": """from repos.dev_reverse_engineering.vibe_coding_toolkit import quick_scaffold
quick_scaffold(template="fastapi_service", destination="./novo_microservico")""",
        "tokens_rules": "Copie apenas os módulos específicos necessários para a funcionalidade atual."
    },
    "andrej-karpathy-skills": {
        "rel_dir": "dev_reverse_engineering/andrej-karpathy-skills",
        "category": "dev_reverse_engineering",
        "tokens_efficiency": "Alto - Apresenta arquiteturas de aprendizado profundo limpas, sem abstrações pesadas de frameworks.",
        "triggers": ["karpathy", "deep learning raiz", "nanoGPT", "arquitetura transformer", "treino llm"],
        "summary": "Coleção de princípios didáticos e minimalistas de inteligência artificial de Andrej Karpathy (nanoGPT, micrograd, algoritmos de treinamento enxutos).",
        "benefits": [
            "Construção de pequenos classificadores de texto e seletores neurais locais ultraleves.",
            "Compreensão detalhada de como modelos de linguagem processam tokens e inferências.",
            "Implementação de lógica matemática de IA sem sobrecarga de bibliotecas pesadas."
        ],
        "usage_cli": "python model.py --data train.txt  # padrão nanoGPT",
        "usage_python": """# Exemplo de arquitetura enxuta baseada nos princípios de Karpathy
import torch
from repos.dev_reverse_engineering.andrej_karpathy_skills import NanoTransformer""",
        "tokens_rules": "Use para entender e codificar algoritmos de aprendizado compactos que não dependem de APIs externas pagas."
    },
    "superpowers": {
        "rel_dir": "dev_reverse_engineering/superpowers",
        "category": "dev_reverse_engineering",
        "tokens_efficiency": "Máximo - Reduz o tempo de depuração em até 80% através de metodologia sistemática.",
        "triggers": ["superpowers", "depuração rigorosa", "tdd estrito", "metodologia de testes", "blindagem"],
        "summary": "Conjunto de meta-habilidades e fluxos de excelência técnica para agentes de IA: TDD estrito, análise sistemática de bugs, depuração por evidências e blindagem de código.",
        "benefits": [
            "Depuração sem adivinhação nos fluxos críticos do RPA (emissão de guias, fechamentos).",
            "Criação automática de baterias de testes antes de aplicar alterações em código legado.",
            "Prevenção de quebra de regras e garantia de funcionamento empírico comprovado."
        ],
        "usage_cli": "Siga o fluxo RED-GREEN-REFACTOR documentado em superpowers/skills/tdd.md",
        "usage_python": "# Aplicação de testes automatizados com assertivas estritas antes de aprovar pull requests",
        "tokens_rules": "Siga as regras de diagnóstico antes de propor qualquer código, reduzindo iterações e desperdício de tokens."
    },
    "impeccable": {
        "rel_dir": "ui_ux_design/impeccable",
        "category": "ui_ux_design",
        "tokens_efficiency": "Alto - Entrega padrões de design sem necessidade de correções estéticas posteriores.",
        "triggers": ["design refinado", "uiux", "microinterações", "anti-slop", "front-end premium", "css moderno"],
        "summary": "Diretrizes e sistemas de design de classe mundial contra interfaces genéricas ('anti-slop'), com foco em micro-interações, tipografia, contraste e elegância visual.",
        "benefits": [
            "Elevação imediata do padrão visual do Dashboard do Second Brain.",
            "Criação de páginas e portais com acabamento premium e moderno.",
            "Eliminação de layouts pobres, garantindo excelente experiência do usuário."
        ],
        "usage_cli": "Consulte impeccable/guidelines.md para aplicar tokens de cor e espaçamentos adequados.",
        "usage_python": "# Incorpore os tokens CSS definidos no design system nos templates web",
        "tokens_rules": "Utilize a paleta de cores e tipografia pré-definida sem pedir para o LLM reinventar o design a cada tela."
    },
    "ruflo": {
        "rel_dir": "orchestration_governance/ruflo",
        "category": "orchestration_governance",
        "tokens_efficiency": "Alto - Barramento assíncrono que divide o trabalho entre agentes sem duplicar contextos.",
        "triggers": ["multiagente", "orquestrador assíncrono", "barramento de agentes", "ruflo", "enxame de agentes"],
        "summary": "Runtime e orquestrador de multi-agentes de alta performance, permitindo coordenação paralela, execução de pipelines e comunicação assíncrona entre IAs.",
        "benefits": [
            "Execução paralela de tarefas de auditoria, testes e codificação sem bloquear o chat principal.",
            "Separação clara de responsabilidades entre agentes especialistas.",
            "Monitoramento do ciclo de vida de tarefas em background."
        ],
        "usage_cli": "python -m ruflo run --pipeline pipeline_auditoria.yaml",
        "usage_python": """from repos.orchestration_governance.ruflo import MultiAgentSwarm
swarm = MultiAgentSwarm()
swarm.dispatch_parallel([task_a, task_b])""",
        "tokens_rules": "Delegue subtarefas independentes para agentes dedicados e consolide apenas o sumário executivo."
    },
    "agentville": {
        "rel_dir": "orchestration_governance/agentville",
        "category": "orchestration_governance",
        "tokens_efficiency": "Médio - Simula interações sociais e profissionais complexas entre agentes virtuais.",
        "triggers": ["simulação de agentes", "colaboração", "múltiplos papéis", "testes de agentes"],
        "summary": "Ambiente de simulação e colaboração de agentes autônomos com personas distintas, memórias locais e objetivos específicos.",
        "benefits": [
            "Teste de hipóteses de negócio e validação de estratégias antes de implementá-las.",
            "Simulação de usuários interagindo com o sistema RPA para prever gargalos.",
            "Laboratório para experimentar novos comportamentos de IA."
        ],
        "usage_cli": "python simulation.py --config config/cenario_empresa.yaml",
        "usage_python": """from repos.orchestration_governance.agentville import AgentCity
city = AgentCity.load("cenario.yaml")
city.run_ticks(10)""",
        "tokens_rules": "Monitore saídas estruturadas em JSON e encerre a simulação assim que o objetivo for alcançado."
    },
    "framework-5p": {
        "rel_dir": "orchestration_governance/framework-5p",
        "category": "orchestration_governance",
        "tokens_efficiency": "Máximo - Filtra demandas inviáveis antes de gastar recursos de desenvolvimento.",
        "triggers": ["5p", "governança de projeto", "metodologia de planejamento", "viabilidade", "arquitetura corporativa"],
        "summary": "Metodologia estruturada dos 5Ps (Propósito, Pessoas, Processo, Plataforma, Performance) para análise profunda, governança e viabilidade de projetos.",
        "benefits": [
            "Alinhamento estratégico rigoroso antes de iniciar qualquer desenvolvimento ou refatoração.",
            "Estruturação de documentações técnicas sólidas e fáceis de auditar.",
            "Garantia de que todo código gerado possui valor de negócio claro."
        ],
        "usage_cli": "Consulte framework-5p/templates/ para obter os roteiros de avaliação de projetos.",
        "usage_python": "# Preencha a matriz 5P no planejamento de novas funcionalidades",
        "tokens_rules": "Use as perguntas-chave do framework para definir o escopo de forma objetiva e sem rodeios."
    },
    "claude-plugins-official": {
        "rel_dir": "orchestration_governance/claude-plugins-official",
        "category": "orchestration_governance",
        "tokens_efficiency": "Alto - Padrão de conectores pré-definidos pronto para uso imediato.",
        "triggers": ["plugins oficiais", "especificação de plugin", "claude manifest", "extensões de ia"],
        "summary": "Repositório de referência contendo as especificações oficiais, schemas e manifestos para criação de plugins e ferramentas de IA da Anthropic.",
        "benefits": [
            "Padronização das ferramentas do Second Brain conforme o padrão da indústria.",
            "Facilidade de exportar skills locais como plugins universais.",
            "Interoperabilidade total com ferramentas que suportam manifests de IA."
        ],
        "usage_cli": "cat repos/orchestration_governance/claude-plugins-official/schemas/plugin.json",
        "usage_python": "# Valide manifestos locais contra os schemas oficiais fornecidos no repositório",
        "tokens_rules": "Valide contratos via JSON Schema para evitar erros de sintaxe e desperdício de chamadas."
    },
    "OmniRoute": {
        "rel_dir": "routing_gateways/OmniRoute",
        "category": "routing_gateways",
        "tokens_efficiency": "Máximo - Roteia chamadas de LLM para modelos gratuitos ou mais baratos, economizando até 90% em custos.",
        "triggers": ["roteamento llm", "economia de tokens", "gateway ai", "fallback de modelo", "modelo gratuito"],
        "summary": "Gateway inteligente de roteamento de chamadas de LLMs com balanceamento de carga, fallback dinâmico e seleção por custo/latência.",
        "benefits": [
            "Desvio automático de tarefas simples (resumos, triagens) para modelos gratuitos como Gemini Flash ou Groq.",
            "Fallback transparente quando uma API de modelo estiver sobrecarregada ou fora do ar.",
            "Redução substancial do consumo de créditos em APIs pagas."
        ],
        "usage_cli": "python omniroute_server.py --port 8080 --config config.yaml",
        "usage_python": """from repos.routing_gateways.OmniRoute import OmniClient
client = OmniClient(strategy="lowest_cost")
response = client.chat(messages=[{"role": "user", "content": "Classifique este texto"}])""",
        "tokens_rules": "Sempre escolha o menor modelo capaz de resolver a tarefa com base na tabela de complexidade do OmniRoute."
    },
    "freellmapi": {
        "rel_dir": "routing_gateways/freellmapi",
        "category": "routing_gateways",
        "tokens_efficiency": "Máximo - Custo zero de tokens utilizando múltiplos endpoints públicos gratuitos agregados.",
        "triggers": ["free llm", "api gratuita", "proxy de ia gratuito", "modelos sem custo"],
        "summary": "Agregador e provedor de APIs e proxies de modelos de inteligência artificial de acesso gratuito, mantendo alta disponibilidade por rotação.",
        "benefits": [
            "Execução de tarefas de segundo plano do Second Brain (auto-sincronização, resumos noturnos) a custo zero.",
            "Ambiente de teste e desenvolvimento sem risco de estourar limites financeiros.",
            "Acesso a múltiplos modelos abertos (Llama, Mistral, Qwen) sem instalação pesada local."
        ],
        "usage_cli": "python freellm_gateway.py --start",
        "usage_python": """from repos.routing_gateways.freellmapi import FreeLLM
llm = FreeLLM()
res = llm.complete("Gere um resumo deste log...")""",
        "tokens_rules": "Utilize para tarefas não críticas e rotinas de manutenção interna sem gastar orçamento."
    },
    "claude-mem": {
        "rel_dir": "memory_rag_graphs/claude-mem",
        "category": "memory_rag_graphs",
        "tokens_efficiency": "Máximo - Armazena histórico em banco vetorial/chave-valor, carregando apenas memórias pertinentes.",
        "triggers": ["memória contínua", "histórico persistente", "memória de longo prazo", "retenção de contexto"],
        "summary": "Sistema de memória episódica e semântica contínua que persiste fatos, correções e preferências do usuário entre diferentes sessões de IA.",
        "benefits": [
            "O agente lembra de erros corrigidos no passado e não repete os mesmos bugs.",
            "Redução drástica do prompt de inicialização: recupera apenas o que é relevante para a pergunta atual.",
            "Alinhamento automático com o estilo de código e preferências do desenvolvedor."
        ],
        "usage_cli": "python -m claude_mem query --text 'quais as regras de banco do rpa?'",
        "usage_python": """from repos.memory_rag_graphs.claude_mem import MemoryStore
mem = MemoryStore()
mem.remember("O campo data_vencimento no RPA não pode ser nulo.")
relevant = mem.recall("como tratar vencimento no RPA?")""",
        "tokens_rules": "Faça buscas semânticas pontuais em vez de injetar arquivos de memória inteiros no contexto."
    },
    "hindsight": {
        "rel_dir": "memory_rag_graphs/hindsight",
        "category": "memory_rag_graphs",
        "tokens_efficiency": "Alto - Evita alucinações e respostas erradas que demandariam múltiplos turnos de correção.",
        "triggers": ["avaliação rag", "reflexão", "auditoria de resposta", "melhoria de contexto", "auto-avaliação"],
        "summary": "Módulo reflexivo de auto-auditoria pós-execução, analisando se o contexto recuperado foi suficiente e preciso para a resposta gerada.",
        "benefits": [
            "Identificação imediata de alucinações antes de entregar o código ao usuário.",
            "Retroalimentação automática no Second Brain sobre lacunas de documentação encontradas.",
            "Melhoria contínua da qualidade das respostas dos agentes."
        ],
        "usage_cli": "python hindsight.py evaluate --query '...' --context '...' --response '...'",
        "usage_python": """from repos.memory_rag_graphs.hindsight import Evaluator
evaluator = Evaluator()
score = evaluator.audit(query=q, context=ctx, answer=ans)""",
        "tokens_rules": "Execute apenas quando houver incerteza ou complexidade crítica, gerando logs resumidos."
    },
    "graphify": {
        "rel_dir": "memory_rag_graphs/graphify",
        "category": "memory_rag_graphs",
        "tokens_efficiency": "Máximo - Substitui a leitura de dezenas de arquivos por consultas pontuais a nós do grafo de código.",
        "triggers": ["grafo de conhecimento", "dependências de código", "graphify", "análise estrutural de código"],
        "summary": "Ferramenta para extrair grafos de conhecimento estruturados a partir de código fonte, schemas de banco de dados e arquivos markdown.",
        "benefits": [
            "Visualização instantânea de quais arquivos são afetados ao alterar uma tabela do banco de dados RPA.",
            "Mapeamento completo da arquitetura de microsserviços e scripts sem ler centenas de linhas.",
            "Navegação relacional rápida por dependências de funções e classes."
        ],
        "usage_cli": "python graphify.py build --source C:/Projetos/RPA --output knowledge/rpa_graph.json",
        "usage_python": """from repos.memory_rag_graphs.graphify import CodeGraph
cg = CodeGraph.from_directory("C:/Projetos/RPA")
impacted = cg.get_blast_radius("app/models/guia.py")""",
        "tokens_rules": "Consulte o raio de impacto de um arquivo antes de editá-lo para alterar apenas o necessário."
    },
    "docling": {
        "rel_dir": "document_web_parsers/docling",
        "category": "document_web_parsers",
        "tokens_efficiency": "Máximo - Extrai apenas o texto e tabelas relevantes de documentos gigantescos com layout preservado.",
        "triggers": ["extrair pdf", "parser docx", "converter tabela pdf", "ocr estruturado", "leitura de documento complexo"],
        "summary": "Parser multimodal de ponta (IBM Research) especializado na extração e conversão estruturada de PDFs complexos, DOCX, tabelas mescladas e relatórios.",
        "benefits": [
            "Extração perfeita de tabelas de guias de recolhimento, DARFs e notas fiscais para o RPA.",
            "Leitura automatizada do arquivo C:/Projetos/Guia_Simplificado_Sistema_RPA.docx para sincronização.",
            "Transformação direta de documentos burocráticos em Markdown limpo pronto para processamento."
        ],
        "usage_cli": "docling converter.py --input guia.pdf --to markdown",
        "usage_python": """from docling.document_converter import DocumentConverter
converter = DocumentConverter()
result = converter.convert("documento.pdf")
markdown_text = result.document.export_to_markdown()""",
        "tokens_rules": "Extraia e passe para o LLM apenas as tabelas ou seções específicas necessárias para o fluxo."
    },
    "ponytail": {
        "rel_dir": "document_web_parsers/ponytail",
        "category": "document_web_parsers",
        "tokens_efficiency": "Alto - Remove HTML ruidoso, scripts e propagandas, entregando conteúdo puro em markdown.",
        "triggers": ["web scraper", "raspador rápido", "extrair conteúdo web", "baixar página sem anúncios"],
        "summary": "Scraper web headless ultrarrápido e leve, desenvolvido para extrair texto limpo e legível por LLMs diretamente de páginas da web.",
        "benefits": [
            "Coleta rápida de documentações de bibliotecas online sem overhead de navegador completo.",
            "Extração limpa de dados de portais governamentais e páginas de consulta do RPA.",
            "Redução em mais de 70% no tamanho do conteúdo web enviado para o agente."
        ],
        "usage_cli": "python ponytail.py fetch --url 'https://site.com/docs' --format markdown",
        "usage_python": """from repos.document_web_parsers.ponytail import FastScraper
scraper = FastScraper()
clean_md = scraper.scrape_to_markdown("https://exemplo.com/tabela")""",
        "tokens_rules": "Sempre converta para markdown antes de repassar o conteúdo de uma página web ao modelo."
    },
    "scientific-agent-skills": {
        "rel_dir": "document_web_parsers/scientific-agent-skills",
        "category": "document_web_parsers",
        "tokens_efficiency": "Alto - Ferramentas matemáticas e científicas dedicadas que realizam cálculos exatos sem alucinação.",
        "triggers": ["artigo científico", "arxiv", "cálculo avançado", "análise de dados estatísticos", "fórmulas"],
        "summary": "Habilidades especializadas para busca de artigos científicos (arXiv, PubMed), parsing de fórmulas matemáticas em LaTeX e cálculos numéricos.",
        "benefits": [
            "Cálculos financeiros e estatísticos exatos para validação de valores de fechamento no RPA.",
            "Pesquisa de algoritmos de ponta e técnicas avançadas de automação em papers científicos.",
            "Eliminação de erros de cálculo mental dos modelos de linguagem."
        ],
        "usage_cli": "python -m scientific_skills search --query 'machine learning automation' --source arxiv",
        "usage_python": """from repos.document_web_parsers.scientific_agent_skills import ArxivSearch, MathSolver
results = ArxivSearch.query("document layout analysis")""",
        "tokens_rules": "Delegue contas matemáticas e buscas bibliográficas diretamente para as ferramentas Python do repositório."
    },
    "security-audit-skill": {
        "rel_dir": "cloud_security_b2b/security-audit-skill",
        "category": "cloud_security_b2b",
        "tokens_efficiency": "Alto - Varreduras estáticas locais sem precisar submeter código a auditorias externas pagas.",
        "triggers": ["auditoria de segurança", "vulnerabilidade", "owasp", "segredos expostos", "pentest", "segurança de código"],
        "summary": "Skill de auditoria automatizada de segurança de código: detecção de senhas e tokens expostos, conformidade OWASP Top 10 e análise estática de vulnerabilidades.",
        "benefits": [
            "Proteção automática para impedir que credenciais e certificados do RPA sejam commitados por engano.",
            "Auditoria de falhas de injeção SQL ou XSS em endpoints de automação.",
            "Garantia de segurança máxima exigida pelo protocolo Zero Trust do usuário."
        ],
        "usage_cli": "python audit_scanner.py --target C:/Projetos/RPA --rules owasp2025",
        "usage_python": """from repos.cloud_security_b2b.security_audit_skill import SecurityAuditor
auditor = SecurityAuditor()
vulnerabilities = auditor.scan_directory("C:/Projetos/RPA")""",
        "tokens_rules": "Emita relatórios apenas com as vulnerabilidades encontradas e suas linhas específicas."
    },
    "Octop": {
        "rel_dir": "cloud_security_b2b/Octop",
        "category": "cloud_security_b2b",
        "tokens_efficiency": "Alto - Automação declarativa de recursos de nuvem que economiza chamadas iterativas de API.",
        "triggers": ["nuvem", "multi-cloud", "infraestrutura como código", "automação cloud", "servidores"],
        "summary": "Plataforma de gestão e orquestração de infraestrutura multi-cloud da Tencent, permitindo gerenciar máquinas virtuais, storage e redes de forma unificada.",
        "benefits": [
            "Provisionamento automático de ambientes para hospedar workers de robôs RPA na nuvem.",
            "Gerenciamento centralizado de backups do Second Brain em storage seguro na nuvem.",
            "Automação de escalabilidade de instâncias conforme a demanda de processamento."
        ],
        "usage_cli": "octop-cli deploy --config cloud_deploy.yaml",
        "usage_python": """from repos.cloud_security_b2b.Octop import CloudManager
cm = CloudManager(provider="tencent")
cm.ensure_instance_running("rpa-worker-01")""",
        "tokens_rules": "Utilize arquivos de configuração declarativos (YAML) em vez de comandos manuais repetidos."
    },
    "nango": {
        "rel_dir": "cloud_security_b2b/nango",
        "category": "cloud_security_b2b",
        "tokens_efficiency": "Máximo - Resolve todo o fluxo complexo de autenticação OAuth e sincronização de 250+ APIs SaaS.",
        "triggers": ["oauth", "integração saas", "conectores api", "sincronização de crm", "nango"],
        "summary": "Plataforma open-source unificada de integração com centenas de APIs SaaS populares (Google, Slack, Notion, Salesforce, GitHub), gerenciando autenticação OAuth e webhooks.",
        "benefits": [
            "Conexão do Second Brain e do RPA com qualquer serviço em nuvem sem escrever código de autenticação do zero.",
            "Renovação automática e silenciosa de tokens OAuth vencidos.",
            "Sincronização bidirecional de dados entre ferramentas internas e provedores SaaS."
        ],
        "usage_cli": "nango sync trigger --connection-id conn_123 --sync-name leads",
        "usage_python": """from repos.cloud_security_b2b.nango import NangoClient
nango = NangoClient(secret_key="...")
data = nango.list_records(connection_id="google-sheets-1", model="row")""",
        "tokens_rules": "Consulte o catálogo de conectores do Nango antes de implementar integrações manuais com APIs externas."
    }
}


def generate_guide(repo_name: str, meta: dict) -> str:
    triggers_str = ", ".join(meta["triggers"])
    benefits_str = "\n".join(f"- {b}" for b in meta["benefits"])
    
    content = f"""---
name: {repo_name}
category: {meta["category"]}
universal_compatibility: [claude, gemini, glm, ollama, antigravity, openai, cursor]
tokens_efficiency: {meta["tokens_efficiency"]}
triggers: [{triggers_str}]
---

# 📖 Guia Universal de Uso: {repo_name}

> **Repositório Local:** `C:\\Users\\USER\\.second_brain\\repos\\{meta["rel_dir"]}`  
> **Categoria:** `{meta["category"]}`  
> **Status:** 🔒 Persistido Localmente (Protegido por Cold Snapshot)

---

## 1. O que é e para que serve
{meta["summary"]}

---

## 2. Como isso ajuda nos seus projetos (Benefícios Práticos)
{benefits_str}

---

## 3. Como o Agente de IA deve Executar (Qualquer Modelo)

### Modo Linha de Comando (CLI / Terminal):
```bash
# Executado a partir da pasta C:\\Users\\USER\\.second_brain\\repos\\{meta["rel_dir"]}
{meta["usage_cli"]}
```

### Modo Integração Python / Wrapper:
```python
{meta["usage_python"]}
```

---

## 4. Diretrizes de Economia de Tokens e Retroalimentação
- **Regra de Consumo:** {meta["tokens_rules"]}
- **Retroalimentação:** Registre no `learning_log.md` do Second Brain qualquer erro encontrado, padrão de dados descoberto ou comando novo testado com sucesso.
- **Consulta Prévia Mandatória:** Antes de codificar soluções repetitivas do zero, consulte este guia e utilize as funções nativas desta biblioteca.
"""
    return content


def main():
    print("=" * 60)
    print("  GERADOR DE MANUAIS UNIVERSAIS AI_GUIDE.md")
    print("=" * 60)
    
    created = 0
    skipped = 0
    
    for repo_name, meta in REPOS_META.items():
        repo_dir = REPOS_ROOT / meta["rel_dir"]
        guide_file = repo_dir / "AI_GUIDE.md"
        
        # Garante que a pasta existe (mesmo se ainda não clonou)
        repo_dir.mkdir(parents=True, exist_ok=True)
        
        guide_content = generate_guide(repo_name, meta)
        guide_file.write_text(guide_content, encoding="utf-8")
        print(f"  [OK] AI_GUIDE.md -> {meta['rel_dir']}")
        created += 1

    print("\n" + "=" * 60)
    print(f"  Total de AI_GUIDE.md gerados com sucesso: {created}")
    print("=" * 60)


if __name__ == "__main__":
    main()
