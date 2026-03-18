"""
Módulo de processamento das notas dos alunos.

As funções serão implementadas de forma incremental em branches separadas.
"""


def classificar_situacao(media):
    """Retorna a situação do aluno com base na média."""
    if media is None:
        return "Sem dados válidos"
    if media < 7.0:
        return "Recuperação"
    return "Aprovado"
