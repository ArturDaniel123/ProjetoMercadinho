print("BEM VINDO AO SUPERMERCADO ZERO INFLACAO")
print('-' * 100)

while True:
    iniciar = input("Para iniciar suas compras, tecle 1: ")

    if iniciar == "1":
        break
    else:
        print("Caractere errado. Tente novamente")

print('-' * 100)
print("Qual secao voce deseja acesar?")
print("1: Frutas")
print("2: Verduras")
print("3: Lanches")
print("4: Padaria")
print("5: Bebidas")

secao = input("Tecle o numero da secao: ")
print('-' * 100)
print('-' * 100)

frutas = {"banana": 7.99, "maca": 5.99, "pera": 4.99, "melancia": 9.99,
          "uva": 4.59, "uva verde": 3.99,
          "manga": 7.99, "melao": 6.90, "mamao": 6.50,
          "abobora": 12.90, "kiwi": 6.90, "tomate": 4.90}
verduras = {"alface": 6.99, "agriao": 11.99, "Brocolis": 5.80, "Coentro": 4.90,
            "Couve": 10.99, "Couve-flor": 12.99, "Espinafre": 9.99}
lanches = {"Cheetos": 4.59, "Treloso": 2.99, "Baconzitos": 6.99,
           "Ruffles": 7.90, "Bokus": 1.80, "Pipos": 3.50}
padaria = {"Pao": 0.90, "Queijo": 4.00, "Presunto": 7.99,
           "Salsicha": 4.50, "Mortadela": 2.99, "Salgado": 2.50}
bebidas = {"Coca cola": 3.50, "Skol": 3.90, "Nova Schin": 4.00, "Brahma": 4.50,
           "Guarana": 2.99, "Pepsi": 3.29, "Sprite": 2.90,
           "Vodka": 12.99, "Fanta uva": 3.00,
           "Fanta laranja": 3.00, "Dolly": 2.00}

if secao == "1":
    print("Voce escolheu a secao de FRUTAS.")
    print(f"Frutas disponiveis: {', '.join(frutas.keys())}")

    while True:
        escolha = input(
            "Escolha qual(is) produto(s) voce deseja (separe por virgula): ")

        escolha = escolha.lower().split(",")

        frutas_invalidas = []
        frutas_validas = []
        escolha = [x.strip() for x in escolha]

        for x in escolha:
            if x in frutas:
                x = x.strip()
            if x not in frutas:
                frutas_invalidas.append(x)
            else:
                frutas_validas.append(x)

        if len(frutas_invalidas) > 0:
            print(
                f'Fruta(s) {', '.join(frutas_invalidas)} indisponivel(is). Tente novamente.')
        else:
            print('Voce escolheu:')
            for x in frutas_validas:
                print(f'{x} : R$ {frutas[x]}')
            break

elif secao == '2':
    print("Voce escolheu a secao de VERDURAS.")
    print(f"Verduras disponiveis: {', '.join(verduras.keys())}")

    while True:
        escolha2 = input(
            "Escolha qual(is) produto(s) voce deseja (separe por virgula): ")

        escolha2 = escolha2.lower().split(",")

        verduras_invalidas = []
        verduras_validas = []
        escolha2 = [x.strip() for x in escolha2]

        for x in escolha2:
            if x in verduras:
                x = x.strip()
            if x not in verduras:
                verduras_invalidas.append(x)
            else:
                verduras_validas.append(x)

        if len(verduras_invalidas) > 0:
            print(
                f'Verduras(s) {', '.join(verduras_invalidas)} indisponivel(is). Tente novamente.')
        else:
            print('Voce escolheu:')
            for x in verduras_validas:
                print(f'{x} : R$ {verduras[x]}')
            break
