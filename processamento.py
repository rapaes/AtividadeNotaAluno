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
