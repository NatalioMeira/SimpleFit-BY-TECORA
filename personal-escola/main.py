import sys

from ClassCadastro import Usuario
from ClassLogin import Login
from personal import Personal
from ia import dieta, falar
from database import buscar_perfil, salvar_perfil


def menu_inicial():
    while True:
        print("\n===== PERSONAL VIRTUAL =====")
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            login = Login()
            usuario = login.realizar_login()
            if usuario:
                return usuario

        elif escolha == "2":
            Usuario().cadastro()
            print("Agora faça login para continuar.")

        elif escolha == "3":
            print("Até logo!")
            sys.exit(0)

        else:
            print("Opção inválida.")


def carregar_ou_criar_perfil(usuario):
    dados_perfil = buscar_perfil(usuario["email"])

    if dados_perfil:
        print(f"\nBem-vindo de volta, {usuario['nome']}!")
        usar_existente = input("Deseja usar seu perfil e rotina salvos? (sim/nao): ").strip().lower()
        if usar_existente.startswith("s"):
            return Personal.from_dict(dados_perfil)

    print("\n===== VAMOS CONHECER VOCÊ =====")
    altura = input("Altura (ex: 1.75m): ").strip()
    peso = input("Peso (ex: 70kg): ").strip()
    objetivo = input("Qual seu objetivo? ").strip()

    perfil = Personal(usuario["nome"], usuario.get("idade"), altura, peso, objetivo)
    perfil.configurar_rotina_completa()

    salvar_perfil(usuario["email"], perfil.to_dict())
    print("\nPerfil salvo! Da próxima vez você pode reaproveitá-lo.")

    return perfil


def loop_chat(perfil):
    print("\n===== CHAT COM SEU PERSONAL VIRTUAL =====")
    print("Digite 'sair' para encerrar.")

    while True:
        mensagem = input("\nVocê: ").strip()

        if mensagem.lower() == "sair":
            print("\nAté a próxima!")
            break

        if not mensagem:
            continue

        resposta = falar(mensagem, perfil)
        print("\nPersonal:", resposta)


def main():
    usuario = menu_inicial()
    perfil = carregar_ou_criar_perfil(usuario)

    perfil.calendario()

    print("\n===== SUA DIETA E ROTINA DE TREINO =====")
    print(dieta(perfil))

    loop_chat(perfil)


if __name__ == "__main__":
    main()
