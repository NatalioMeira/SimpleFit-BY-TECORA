import hashlib
import re

from database import adicionar_usuario, buscar_usuario_por_email

REGEX_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


class Usuario:
    def __init__(self, nome=None, contato=None, email=None, idade=None, senha=None):
        self.nome = nome
        self.contato = contato
        self.email = email
        self.idade = idade
        self.senha = senha  # sempre armazenado como hash

    def to_dict(self):
        return {
            "nome": self.nome,
            "contato": self.contato,
            "email": self.email,
            "idade": self.idade,
            "senha": self.senha,
        }

    def cadastro(self):
        print("\n===== CADASTRO =====")

        self.nome = input("Seu nome completo: ").strip()

        while True:
            email = input("Email: ").strip()
            if not REGEX_EMAIL.match(email):
                print("Email inválido. Tente novamente.")
                continue
            if buscar_usuario_por_email(email):
                print("Já existe uma conta com esse email. Tente outro ou faça login.")
                continue
            self.email = email
            break

        self.contato = input("Contato: ").strip()

        while True:
            try:
                self.idade = int(input("Idade: "))
                break
            except ValueError:
                print("Digite um número válido.")

        while True:
            senha = input("Crie uma senha (mínimo 4 caracteres): ")
            if len(senha) < 4:
                print("Senha muito curta.")
                continue
            self.senha = hash_senha(senha)
            break

        adicionar_usuario(self.to_dict())
        print("Cadastro realizado com sucesso!\n")
        return self
