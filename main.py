def obter_dados_exemplo():
    """
    Estrutura de dados:
    lista de tuplas no formato [("Nome", [notas])].
    """
    alunos = [
        ("Ana", [8.0, 9.5, 7.0]),
        ("Bruno", [5.0, 6.0]),
        ("Carla", []),
    ]
    return alunos


def main():
    alunos = obter_dados_exemplo()
    print("Lista de alunos (estrutura base):")
    print(alunos)


if __name__ == "__main__":
    main()

