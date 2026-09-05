import json
import os

PASTA_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")
CAMINHO_USUARIOS = os.path.join(PASTA_DADOS, "usuarios.json")
CAMINHO_PERFIS = os.path.join(PASTA_DADOS, "perfis.json")


def _garantir_pasta():
    os.makedirs(PASTA_DADOS, exist_ok=True)


def _ler_json(caminho, padrao):
    if not os.path.exists(caminho):
        return padrao
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return padrao


def _escrever_json(caminho, dados):
    _garantir_pasta()
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


# ---------------------- Usuários ----------------------

def carregar_usuarios():
    return _ler_json(CAMINHO_USUARIOS, [])


def salvar_usuarios(usuarios):
    _escrever_json(CAMINHO_USUARIOS, usuarios)


def buscar_usuario_por_email(email):
    email = email.lower().strip()
    for usuario in carregar_usuarios():
        if usuario["email"].lower() == email:
            return usuario
    return None


def adicionar_usuario(usuario_dict):
    usuarios = carregar_usuarios()
    usuarios.append(usuario_dict)
    salvar_usuarios(usuarios)


# ---------------------- Perfis (Personal) ----------------------

def carregar_perfis():
    return _ler_json(CAMINHO_PERFIS, {})


def salvar_perfis(perfis):
    _escrever_json(CAMINHO_PERFIS, perfis)


def salvar_perfil(email, perfil_dict):
    perfis = carregar_perfis()
    perfis[email.lower().strip()] = perfil_dict
    salvar_perfis(perfis)


def buscar_perfil(email):
    return carregar_perfis().get(email.lower().strip())
