from processamento import calcular_media, validar_notas, classificar_situacao, processar_alunos, gerar_relatorio_txt

def obter_dados_exemplo():
    """
    Estrutura de dados:
    lista de tuplas no formato [("Nome", [notas])].
    """
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
    resultado = processar_alunos(alunos)

    print("Alunos processados:")
    for aluno in resultado["alunos_processados"]:
        print(aluno)

    print("\nAlunos em recuperação:")
    for aluno in resultado["em_recuperacao"]:
        print(aluno)

    print("\nTop Student:")
    print(resultado["top_student"])
    notas_exemplo = [8.0, "abc", 7.5, None, 10]
    notas_validas = validar_notas(notas_exemplo)
    media = calcular_media(notas_validas)


if __name__ == "__main__":
    main()

