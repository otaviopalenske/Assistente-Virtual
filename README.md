# FinancAI - Assistente Virtual de Finanças Pessoais com Inteligência Artificial

Este projeto consiste no desenvolvimento de um assistente virtual inteligente especializado em finanças pessoais, criado como desafio prático para a plataforma DIO. O agente utiliza Inteligência Artificial generativa integrada com análise de dados para fornecer insights financeiros personalizados.

---

## 🛠️ Desenvolvimento do Agente (Etapa por Etapa)

### 📋 Etapa 1: Documentação e Persona do Agente
O agente foi batizado de **FinancAI**. Sua persona foi desenhada para agir como um consultor financeiro direto, prático e focado em soluções de economia. Ele opera sob restrições estritas para não sugerir investimentos de alto risco e manter o foco na organização do orçamento.

### 📚 Etapa 2: Base de Conhecimento (RAG Simulado)
Para evitar respostas genéricas, o assistente foi alimentado com duas fontes de conhecimento:
1. **Dados Estruturados (Pandas):** Uma tabela contendo o histórico real de transações recentes do usuário (colunas de Data, Categoria, Descrição e Valor).
2. **Regras de Negócio:** Diretrizes financeiras clássicas como a regra orçamentária 50/30/20 e metas de redução de custos fixos.

### 🧠 Etapa 3: Engenharia de Prompts
Foi desenvolvido um *System Instruction* detalhado que força o modelo a cruzar as perguntas do usuário diretamente com a base de conhecimento fornecida, garantindo precisão e baixíssima taxa de alucinação (temperatura configurada em 0.3).

### 💻 Etapa 4: Aplicação Funcional e Testes
A aplicação foi desenvolvida em **Python**, utilizando o SDK oficial do Google Gemini (`google-genai`). O script cria um canal de chat estruturado que processa as entradas do usuário, consulta o DataFrame do Pandas e retorna a melhor estratégia financeira.

---

## 🚀 Como Executar o Projeto

1. Instale as dependências necessárias:
   ```bash
   pip install google-genai pandas
