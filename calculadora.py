while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    print('Selecione uma operação:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação')

    escolhido = int(input('Escolha: '))

    if escolhido == 1:
        resultado = n1 + n2
        print(f'Resultado: {resultado}')

    elif escolhido == 2:
        resultado = n1 - n2
        print(f'Resultado: {resultado}')

    elif escolhido == 3:
        if n2 == 0:
            print('Não é possível dividir por zero!')
        else:
            resultado = n1 / n2
            print(f'Resultado: {resultado}')

    elif escolhido == 4:
        resultado = n1 * n2
        print(f'Resultado: {resultado}')

    else:
        print('Opção inválida!')

    repetir = input(
        'Digite 1 para continuar ou qualquer tecla para sair: '
    )

    if repetir != '1':
        print('Encerrando programa...')
        break
