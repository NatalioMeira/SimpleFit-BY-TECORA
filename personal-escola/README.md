# Personal Virtual

Sistema de linha de comando que faz login/cadastro, monta a rotina
semanal da pessoa (escola, trabalho, academia), mostra o calendário
e conversa com você via IA (Groq) para dieta e dicas de treino.

## ⚠️ Antes de qualquer coisa

O arquivo `.env` que veio no zip original tinha uma chave de API da Groq
exposta em texto puro. **Revogue essa chave** em
https://console.groq.com/keys e gere uma nova — nunca reaproveite uma
chave que já circulou em um arquivo compartilhado.

## O que foi mudado em relação ao projeto original

- `ClassCadastro.py` e `ClassLogin.py` agora são usados de verdade pelo
  `main.py` (antes ficavam soltos e o login rodava sozinho ao importar
  o arquivo).
- Senhas são guardadas como hash SHA-256, nunca em texto puro.
- `personal.py` ganhou métodos para configurar escola, trabalho e
  academia — antes esses dados nunca eram preenchidos e o calendário
  sempre aparecia "Dia livre" o tempo todo.
- Tudo é salvo em `dados/usuarios.json` e `dados/perfis.json` (criados
  automaticamente), então você não precisa recadastrar ou reconfigurar
  sua rotina toda vez que abrir o programa.
- `ia.py` não quebra mais o programa se faltar a chave de API — só
  avisa que o chat/dieta estão desativados até você configurar.
- `requirements.txt` corrigido (`python` e `Groq` não eram nomes de
  pacote válidos no PyPI).

## Como rodar

```bash
# 1. Crie um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure sua chave da Groq
cp .env.example .env
# edite o .env e cole sua chave em GROQ_API_KEY

# 4. Rode o programa
python3 main.py
```

## Estrutura

| Arquivo             | Função                                                       |
|----------------------|---------------------------------------------------------------|
| `main.py`            | Ponto de entrada — liga login/cadastro, perfil, dieta e chat |
| `ClassCadastro.py`   | Cadastro de usuário (nome, email, senha com hash, etc.)      |
| `ClassLogin.py`      | Login de usuário já cadastrado                               |
| `personal.py`        | Classes `Pessoa`/`Personal`, rotina semanal e calendário     |
| `ia.py`               | Integração com a Groq (dieta sugerida e chat)                |
| `database.py`        | Persistência simples em JSON (`dados/usuarios.json`, `dados/perfis.json`) |
| `.env.example`       | Modelo do arquivo de variáveis de ambiente                   |

## Fluxo de uso

1. Ao abrir, escolha **Cadastrar** (primeira vez) ou **Login**.
2. Na primeira vez, você configura altura, peso, objetivo e sua rotina
   semanal (escola, trabalho, academia — dias e horários).
3. O programa salva tudo, mostra seu calendário da semana e sugere uma
   dieta com base no seu perfil.
4. Depois entra em modo chat, onde você pode pedir dicas ao seu
   Personal Virtual. Digite `sair` para encerrar.
5. Da próxima vez que fizer login, pode reaproveitar o perfil e a
   rotina já salvos, sem precisar configurar tudo de novo.
