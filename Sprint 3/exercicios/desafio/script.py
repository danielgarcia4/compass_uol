# leitura do arquivo csv
with open("actors.csv", "r") as arquivo:
    linhas = arquivo.readlines()

# PERGUNTA 1

n_filmes = {}  # dicionário para armazenar o nome e numero de filmes dos atores

for linha in linhas[1:]:  # Ignorar o cabeçalho
    dados = linha.strip().rsplit(",", 5)  # rsplit para tratar o nome com ,
    nome_ator = dados[0]
    n_filmes[nome_ator] = int(dados[2].strip())

# buscando o ator com mais filmes
max_filmes_ator = max(n_filmes, key=n_filmes.get)
n_max_filmes = n_filmes[max_filmes_ator]

# escrevendo resultado no arquivo
with open("etapa-1.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(
        f"O ator/atriz com mais filmes é {max_filmes_ator} ({n_max_filmes} filmes)\n"
    )


# PERGUNTA 2

acm_gross = 0
for linha in linhas[1:]:
    dados = linha.strip().rsplit(",", 5)
    valor_gross = float(dados[5])
    acm_gross += valor_gross

media_gross = acm_gross / (len(linhas) - 1)

with open("etapa-2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(
        f"Média de receita de bilheteria bruta dos principais filmes: {media_gross:.2f}\n"
    )

# PERGUNTA 3

avarage_receita = 0  # para armazenar o maior avarage
avarage_ator = None  # para armazenar o nome do ator com maior avarage

for linha in linhas[1:]:
    dados = linha.strip().rsplit(",", 5)
    if float(dados[3]) > avarage_receita:
        avarage_receita = float(dados[3])
        avarage_ator = dados[0]

with open("etapa-3.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(
        f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é {avarage_ator}.\n"
    )

# PERGUNTA 4

aparicoes_filmes = {}  # Dicionário para contar as aparições dos filmes

for linha in linhas[1:]:
    dados = linha.strip().rsplit(",", 5)

    if dados[4] in aparicoes_filmes:
        aparicoes_filmes[dados[4]] += 1
    else:
        aparicoes_filmes[dados[4]] = 1

# Ordenação por quantidade de aparições e depois pelo nome
sorted_filmes = sorted(aparicoes_filmes.items(), key=lambda x: (-x[1], x[0]))

with open("etapa-4.txt", "w") as arquivo:
    for index, (filme, count) in enumerate(sorted_filmes):
        arquivo.write(
            f"{index+1} - O filme {filme} aparece {count} vez(es) no dataset\n"
        )

# QUESTÃO 5

total_gross = {}

for linha in linhas[1:]:
    dados = linha.strip().rsplit(",", 5)
    ator = dados[0].replace('"', "")  # para remover as aspas do Robert
    total_gross[ator] = float(dados[1])

# os dados já estão ordenados, mas farei o sorted para manter o padrão
sorted_gross = sorted(total_gross.items(), key=lambda x: (-x[1], x[0]))

with open("etapa-5.txt", "w") as arquivo:
    for ator, receita_total in sorted_gross:
        arquivo.write(f"{ator} - {receita_total:.2f}\n")
