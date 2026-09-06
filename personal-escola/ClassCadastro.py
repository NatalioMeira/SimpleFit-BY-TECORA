import hashlib
# essa biblioteca transforma o dado em um valor fixo e praticamente nao da pra reverter para descobrir o original.
import re
# re e usada para procurar, validar e manipular padroes dentro de textos usando expressoes (que seria o regex).
from database import adicionar_usuario, buscar_usuario_por_email

regex_email = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
# ^ ta verificando se o email foi escrito de forma correta, ex: teste gmail.com nao daria certo mas teste@gmail.com daria.
# ↓  transformando a senha em hash (copiei a seta do google pois nao achei uma seta pra usar).
def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()
#                            ↓ o none serve pra nao precisar de credenciais pra chamar um metodo.
class Usuario:
    def __init__(self, nome=None, contato=None, email=None, idade=None, senha=None):
        self.nome = nome
        self.contato = contato
        self.email = email
        self.idade = idade
        self.senha = senha 
        
#        ↓ to_dict serve pra transformar valores em um valor de dicionario (dict) que depois vou colocar em um json.
    def to_dict(self):
        return {"nome": self.nome, "contato": self.contato, "email": self.email, "idade": self.idade, "senha": self.senha}
#        ↓ auto explicativo.
    def cadastro(self):
        print("\n===== CADASTRO =====")
#                                                 ↓ serve para tirar os espacos e quebras de linha na parte de fora do valor.
        self.nome = input("Seu nome completo: ").strip()

        while True:
            email = input("Email: ").strip()
            if not regex_email.match(email):
                print("Email inválido. Tente novamente.")
                continue
            if buscar_usuario_por_email(email):
                print("Já existe uma conta com esse email. Tente outro ou faça login.")
                continue
            self.email = email
            break

        self.contato = input("Contato: ").strip()
#                        ^ definimos como string pois nem todo contato e numerico e mesmo que seja ele seria considerado.
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
