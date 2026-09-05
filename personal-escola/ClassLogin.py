from ClassCadastro import hash_senha
from database import buscar_usuario_por_email


class Login:
    def __init__(self):
        self.usuario_logado = None

    def realizar_login(self, tentativas=3):
        for _ in range(tentativas):
            email = input("Email: ").strip()
            senha = input("Senha: ")

            usuario = buscar_usuario_por_email(email)

            if usuario and usuario["senha"] == hash_senha(senha):
                print(f"\nLogin concluído com sucesso! Bem-vindo(a), {usuario['nome']}!")
                self.usuario_logado = usuario
                return usuario

            print("Erro: dados incorretos.\n")

        print("Número máximo de tentativas excedido.")
        return None

    def logout(self):
        self.usuario_logado = None
        print("Logout concluído.")
