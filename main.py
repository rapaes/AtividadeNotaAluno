from processamento import calcular_media, validar_notas


def main():
    notas_exemplo = [8.0, "abc", 7.5, None, 10]
    notas_validas = validar_notas(notas_exemplo)
    media = calcular_media(notas_validas)

    print("Cálculo de média (exemplo simples):")
    print("Notas originais:", notas_exemplo)
    print("Notas válidas  :", notas_validas)
    print("Média          :", media)


if __name__ == "__main__":
    main()

