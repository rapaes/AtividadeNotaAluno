from processamento import classificar_situacao


def main():
    exemplos = [None, 5.5, 7.0, 9.0]

    print("Classificação de situação (exemplos):")
    for media in exemplos:
        situacao = classificar_situacao(media)
        print("Média:", media, "-> Situação:", situacao)


if __name__ == "__main__":
    main()

