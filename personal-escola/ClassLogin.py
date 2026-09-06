from ClassCadastro import hash_senha
# ^ herda hash_senha de ClassCadastro.
# ↓ herda buscar_usuario_por_email de database.
from database import buscar_usuario_por_email

class Login:
    def __init__(self):
        self.usuario_logado = None
#        ^ faz o usuario comecar sem login.
    
    def realizar_login(self, tentativas=3):
        for _ in range(tentativas):
            email = input("Email: ").strip()
            senha = input("Senha: ")
#               from ClassCadastro import hash_senha
# ^ herda hash_senha de ClassCadastro
# ↓ herda buscar_usuario_por_email de database
from database import buscar_usuario_por_email

class Login:
    def __init__(self):
        self.usuario_logado = None

    def realizar_login(self, tentativas=3):
        for _ in range(tentativas):
            email = input("Email: ").strip()
            senha = input("Senha: ")
#                          ↓ transformando usuario no email verificado no banco de dados
            usuario = buscar_usuario_por_email(email)
#                        ↓  verificando o usuario e a senha do usuario.
            if usuario and usuario["senha"] == hash_senha(senha):
                print(f"\nLogin concluído com sucesso! Bem-vindo(a), {usuario['nome']}!")
#                           ↓ altera o objeto da classe transformando o login de none para o usuario
                self.usuario_logado = usuario
#                   ↓ encerra o metodo da classe
                return usuario
#                ↓ caso o if seja ignorado ele vai dar erro
            print("Erro: dados incorretos.\n")
            
        print("Número máximo de tentativas excedido.")
        return None

    def logout(self):
        self.usuario_logado = None
#                ^ define o login do usuario como none.
        print("Logout concluído.")
