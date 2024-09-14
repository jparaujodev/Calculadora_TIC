import time
def Calculadora():
    while True:
        print("Seja bemvindo a calculadora simpes!")
        print()
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("S. para sair")
        operacao = input("Selecione um opção ou digite 'S' para sair.")

        if operacao  == 'S' or operacao == 's':
            print("obrigado por utilizar a calculadora")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("comando inválido! Tente novamente")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("segundo número: "))


        if operacao == '1':
            resultado = numero_1 + numero_2
            print(f'O resultado da soma deu: {resultado}')
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print(f'O resultado da subtração deu: {resultado}')
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print(f'O resultado da multiplicação deu: {resultado}')
        else: 
            if numero_2 == 0:
                print('divisões por zero não são possiveis')
                time.sleep(1.5)
                continue
            else:
                resultado = numero_1 / numero_2
                time.sleep(2)
                print('calculando...')
            print(f'O resultado da divisão deu: {resultado}')
            
Calculadora()