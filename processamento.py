"""
Módulo de processamento das notas dos alunos.

As funções serão implementadas de forma incremental em branches separadas.
"""


def validar_notas(lista_notas):
    """Retorna apenas as notas válidas (numéricas) de uma lista."""
    notas_validas = []
    if lista_notas is None:
        return notas_validas

    for valor in lista_notas:
        try:
            nota = float(valor)
            notas_validas.append(nota)
        except (TypeError, ValueError):
            # ignora valores que não são números
            pass

    return notas_validas


def calcular_media(notas_validas):
    """Calcula a média das notas válidas. Se não tiver notas, retorna None."""
    if not notas_validas:
        return None

    soma = 0.0
    for nota in notas_validas:
        soma = soma + nota

    quantidade = len(notas_validas)
    media = soma / quantidade
    return media


def classificar_situacao(media):
    """Retorna a situação do aluno com base na média."""
    if media is None:
        return "Sem dados válidos"
    if media < 7.0:
        return "Recuperação"
    return "Aprovado"


def processar_alunos(lista_alunos):
    """
    Recebe uma lista de tuplas no formato:
    [("Nome", [notas]), ("Outro Nome", [notas]), ...]

    Retorna um dicionário com:
      - alunos_processados: lista de dicts com nome, media, situacao
      - em_recuperacao: lista dos alunos em recuperação
      - top_student: dict com o aluno de maior média (ou None)
    """
    alunos_processados = []
    em_recuperacao = []
    top_student = None

    for nome, notas in lista_alunos:
        notas_validas = validar_notas(notas)
        media = calcular_media(notas_validas)
        situacao = classificar_situacao(media)

        aluno_info = {
            "nome": nome,
            "media": media,
            "situacao": situacao,
        }
        alunos_processados.append(aluno_info)

        if situacao == "Recuperação":
            em_recuperacao.append(aluno_info)

        if media is not None:
            if top_student is None or media > top_student["media"]:
                top_student = aluno_info

    resultado = {
        "alunos_processados": alunos_processados,
        "em_recuperacao": em_recuperacao,
        "top_student": top_student,
    }
    return resultado


def gerar_relatorio_txt(dados_processados, nome_arquivo="resultado.txt"):
    """
    Gera um arquivo .txt com:
      - todos os alunos (nome, média, situação)
      - alunos em recuperação
      - top student
    """
    linhas = []

    linhas.append("RELATÓRIO DE DESEMPENHO ACADÊMICO")
    linhas.append("================================")
    linhas.append("")

    alunos = dados_processados.get("alunos_processados", [])
    em_rec = dados_processados.get("em_recuperacao", [])

    # Resumo
    linhas.append("Resumo:")
    linhas.append("--------------------------------")
    linhas.append("Total de alunos       : " + str(len(alunos)))
    linhas.append("Alunos em recuperação : " + str(len(em_rec)))
    linhas.append("")

    # Lista de alunos
    linhas.append("Alunos (médias e situações):")
    linhas.append("--------------------------------")
    for aluno in alunos:
        nome = aluno["nome"]
        media = aluno["media"]
        situacao = aluno["situacao"]

        if isinstance(media, (int, float)):
            media_str = "{:.2f}".format(media)
        else:
            media_str = "N/A"

        linhas.append("Aluno: " + nome)
        linhas.append("  Média   : " + media_str)
        linhas.append("  Situação: " + situacao)
        linhas.append("")

    # Alunos em recuperação
    linhas.append("================================")
    linhas.append("Alunos em Recuperação:")
    linhas.append("--------------------------------")
    if not em_rec:
        linhas.append("Nenhum aluno em recuperação.")
    else:
        for aluno in em_rec:
            nome = aluno["nome"]
            media = aluno["media"]
            if isinstance(media, (int, float)):
                media_str = "{:.2f}".format(media)
            else:
                media_str = "N/A"
            linhas.append(nome + " - Média: " + media_str)

    linhas.append("")

    # Top Student
    linhas.append("================================")
    linhas.append("Top Student:")
    linhas.append("--------------------------------")
    top = dados_processados.get("top_student")
    if top is None:
        linhas.append("Nenhum Top Student (sem médias válidas).")
    else:
        nome = top["nome"]
        media = top["media"]
        if isinstance(media, (int, float)):
            media_str = "{:.2f}".format(media)
        else:
            media_str = "N/A"
        linhas.append("Nome : " + nome)
        linhas.append("Média: " + media_str)

    # Salvar arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            arquivo.write(linha + "\n")
