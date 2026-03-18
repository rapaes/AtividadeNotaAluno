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
