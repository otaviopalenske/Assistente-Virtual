import os
import pandas as pd
from google import genai
from google.genai import types

# 1. Configuração do Cliente API (Insira sua chave aqui ou configure no ambiente)
# os.environ["GEMINI_API_KEY"] = "SUA_API_KEY_AQUI"
client = genai.Client()

# 2. Etapa 2: Base de Conhecimento (Simulando dados de transações do usuário)
dados_gastos = {
    'Data': ['2026-05-15', '2026-05-16', '2026-05-17', '2026-05-18', '2026-05-19'],
    'Categoria': ['Alimentação', 'Transporte', 'Lazer', 'Alimentação', 'Assinaturas'],
    'Descricao': ['Supermercado', 'Combustível', 'Cinema', 'Restaurante', 'Streaming'],
    'Valor': [250.00, 120.00, 60.00, 85.00, 42.90]
}
df_gastos = pd.DataFrame(dados_gastos)

# Regras de bolso financeiras que o agente deve saber (Base de Conhecimento de texto)
REGRAS_FINANCEIRAS = """
- Regra 50/30/20: 50% para necessidades, 30% para desejos, 20% para poupança/investimentos.
- Reserva de Emergência: Deve cobrir de 3 a 6 meses de custos fixos.
- Meta do usuário atual: Reduzir gastos com 'Alimentação fora de casa' e 'Lazer' neste mês.
"""

# 3. Etapa 1 e 3: Persona e Engenharia de Prompts (System Instruction)
PROMPT_SISTEMA = f"""
Você é o "FinancAI", um assistente virtual especializado em finanças pessoais.
Seu tom de voz deve ser direto, prático, encorajador e focado em soluções.

Você tem acesso ao histórico atual de gastos do usuário:
{df_gastos.to_string(index=False)}

E deve seguir estas diretrizes de conhecimento:
{REGRAS_FINANCEIRAS}

Responda às dúvidas do usuário de forma concisa, utilizando os dados fornecidos sempre que ele perguntar sobre o histórico dele ou pedir conselhos baseados na realidade dele.
"""

# 4. Etapa 4: Aplicação Funcional (Função de Chat)
def enviar_mensagem(pergunta_usuario):
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=PROMPT_SISTEMA,
            temperature=0.3, # Temperatura baixa para o assistente não inventar dados financeiros
        )
    )
    
    resposta = chat.send_message(pergunta_usuario)
    return resposta.text

# --- Exemplo de Uso/Testes (Etapa 4 - Testes) ---
if __name__ == "__main__":
    print("--- Assistente Financeiro Iniciado ---")
    
    # Teste 1: Consultando a base de dados via IA
    pergunta_1 = "Quanto eu gastei no total com alimentação segundo o meu histórico?"
    print(f"\nUsuário: {pergunta_1}")
    print(f"FinancAI:\n{enviar_mensagem(pergunta_1)}")
    
    print("-" * 40)
    
    # Teste 2: Pedindo conselho com base nas regras de negócio
    pergunta_2 = "Estou gastando muito com lazer, o que você me recomenda com base na minha meta?"
    print(f"\nUsuário: {pergunta_2}")
    print(f"FinancAI:\n{enviar_mensagem(pergunta_2)}")