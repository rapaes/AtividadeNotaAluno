from processamento import validar_notas


def main():
    notas_exemplo = [8.0, "abc", 7.5, None, 10]
    notas_validas = validar_notas(notas_exemplo)

    print("Validação de notas (exemplo simples):")
    print("Notas originais:", notas_exemplo)
    print("Notas válidas  :", notas_validas)


if __name__ == "__main__":
    main()

