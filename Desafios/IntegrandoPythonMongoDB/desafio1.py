from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria uma instância de engine para se conectar ao banco de dados SQLite
engine = create_engine('sqlite:///banco.db', echo=True)

# Cria uma sessão para executar as operações no banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Cria uma classe base declarativa para definir as tabelas
Base = declarative_base()

# Define a classe Cliente
class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Cliente(id={self.id}, nome='{self.nome}', idade={self.idade})"

# Define a classe Conta
class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer)
    saldo = Column(Integer)

    def __repr__(self):
        return f"Conta(id={self.id}, cliente_id={self.cliente_id}, saldo={self.saldo})"

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Insere dados mínimos para manipulação
cliente1 = Cliente(nome='João', idade=30)
cliente2 = Cliente(nome='Maria', idade=25)
cliente3 = Cliente(nome='Pedro', idade=35)

conta1 = Conta(cliente_id=1, saldo=1000)
conta2 = Conta(cliente_id=2, saldo=500)
conta3 = Conta(cliente_id=3, saldo=2000)

session.add_all([cliente1, cliente2, cliente3, conta1, conta2, conta3])
session.commit()

# Executa métodos de recuperação de dados
clientes = session.query(Cliente).all()
contas = session.query(Conta).all()

print("Clientes:")
for cliente in clientes:
    print(cliente)

print("Contas:")
for conta in contas:
    print(conta)
