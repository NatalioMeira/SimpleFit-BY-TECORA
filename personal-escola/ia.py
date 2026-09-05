import os
from dotenv import load_dotenv

load_dotenv()

CHAVE_API = os.getenv("GROQ_API_KEY") or os.getenv("gateway")

_cliente_ia = None
if CHAVE_API:
    from groq import Groq
    _cliente_ia = Groq(api_key=CHAVE_API)


def falar(mensagem, pessoa):
    if _cliente_ia is None:
        return (
            "Erro: nenhuma chave de API da Groq foi encontrada.\n"
            "Configure GROQ_API_KEY no arquivo .env (veja .env.example) "
            "para habilitar o chat com IA."
        )

    contexto = f"""
Nome: {pessoa.nome}
Idade: {pessoa.idade}
Altura: {pessoa.altura}
Peso: {pessoa.peso}
Objetivo: {pessoa.objetivo}
Academia: {pessoa.academia}
Dias de treino: {pessoa.diaTreino}
Horários de treino: {pessoa.horarios}
Escola: {pessoa.escola}
Trabalho: {pessoa.trabalho}
"""

    prompt = f"""
Você é um Personal Virtual.

Ajude a pessoa a organizar sua rotina,
treinos, descanso e alimentação equilibrada.

Informações da pessoa:

{contexto}

Não faça dietas restritivas ou recomendações
médicas.

Diga os treinos que a pessoa deve fazer e em que horario de que dia,
baseado no contexto dado.

Seja muito breve dizendo apenas o necessario.

Mensagem:
{mensagem}
"""

    try:
        resposta = _cliente_ia.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return resposta.choices[0].message.content

    except Exception as erro:
        return "Erro na IA: " + str(erro)


def dieta(pessoa):
    mensagem = """
Monte um plano de alimentação equilibrada
para minha rotina.

Separe em:

Café da manhã
Almoço
Lanche
Jantar

Considere meu peso, altura e objetivo, meus horários e minha rotina.
"""
    return falar(mensagem, pessoa)
