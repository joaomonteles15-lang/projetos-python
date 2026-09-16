def calculadora():
    while True:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))    
        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: não é possível dividir por zero!")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            continue

        print(f"Resultado: {resultado}")

        continuar = input("Quer calcular de novo? (s/n): ").lower()
        if continuar != "s":
            print("Até mais!")
            break

calculadora()