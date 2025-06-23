def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            else:
                print("Por favor, digite 1 para sim ou 0 para não.")
        except ValueError:
            print("Entrada inválida. Digite apenas 1 ou 0.")
while True:
    Carl = float(input('voce ligou o carro? 1 para sim e 0 para não:'))
    if Carl == 1:
        print('você ligou o carro')
        seta = float(input('você utilizou a seta? digite 1 para sim e 0 para não:'))
        if seta == 1:
            print('você utilizou a seta')
            Volante = float(input('Você girou o volante? digite 1 para sim e 0 para não:'))
            if Volante == 1:
                print('você girou o volante junto com a seta')
            elif Volante == 0:
                print('você não girou o volante')
        elif seta == 0:
            print('você não utilizou a seta')
    elif Carl == 0:
        print('você não ligou o carro')
    else: 
        print('opção inválida')
       