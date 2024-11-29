# Criando o dicionário com dados de três pessoas
pessoas = {
    "pessoa1": {"nome": "Ana", "idade": 25},
    "pessoa2": {"nome": "Bruno", "idade": 30},
    "pessoa3": {"nome": "Carla", "idade": 22},
}

# Exibindo os dados de todas as pessoas de forma organizada
for chave, dados in pessoas.items():
    print(f"{chave.capitalize()}:")
    print(f"  Nome: {dados['nome']}")
    print(f"  Idade: {dados['idade']}")
    print()
