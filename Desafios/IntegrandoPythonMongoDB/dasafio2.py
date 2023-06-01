from pymongo import MongoClient

# Conecta ao banco de dados MongoDB
client = MongoClient('<URL de conexão ao MongoDB>')

# Cria um banco de dados
db = client['meu_banco']

# Define uma coleção chamada 'bank' para armazenar documentos de clientes
collection = db['bank']

# Insere documentos com a estrutura mencionada
documento1 = {
    'cliente_id': 1,
    'nome': 'João',
    'idade': 30
}

documento2 = {
    'cliente_id': 2,
    'nome': 'Maria',
    'idade': 25
}

documento3 = {
    'cliente_id': 3,
    'nome': 'Pedro',
    'idade': 35
}

collection.insert_many([documento1, documento2, documento3])

# Recupera informações com base nos pares de chave e valor
resultado = collection.find({'idade': {'$gte': 30}})  # Recupera documentos com idade igual ou superior a 30

print("Documentos encontrados:")
for documento in resultado:
    print(documento)
