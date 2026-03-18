from processamento import processar_alunos


def obter_dados_exemplo():
    alunos = [
        ("Ana", [8.0, 9.5, 7.0]),
        ("Bruno", [5.0, 6.0]),
        ("Carla", []),
        ("Diego", [10, "abc", 9.0]),
    ]
    return alunos


def main():
    alunos = obter_dados_exemplo()
    resultado = processar_alunos(alunos)

    print("Alunos processados:")
    for aluno in resultado["alunos_processados"]:
        print(aluno)

    print("\nAlunos em recuperação:")
    for aluno in resultado["em_recuperacao"]:
        print(aluno)

    print("\nTop Student:")
    print(resultado["top_student"])


if __name__ == "__main__":
    main()

