from processamento import gerar_relatorio_txt, processar_alunos


def obter_dados_exemplo():
    alunos = [
        ("Ana", [8.0, 9.5, 7.0]),
        ("Bruno", [5.0, 6.0]),
        ("Carla", []),
        ("Diego", [10, "abc", 9.0]),
        ("Eduarda", [7.0, 7.5, 8.0]),
    ]
    return alunos


def main():
    alunos = obter_dados_exemplo()
    dados = processar_alunos(alunos)

    print("Resumo no console:")
    for aluno in dados["alunos_processados"]:
        print(aluno)

    gerar_relatorio_txt(dados)
    print("\nRelatório 'resultado.txt' gerado na pasta do projeto.")


if __name__ == "__main__":
    main()

