while True:
    try:
        print("Lista de productos en Okidoki Market:")
        print("1. Desodorante: $300")
        print("2. Sopa para uno: $2500")
        print("3.Chocolate: $300")
        print("4. Barra de cereal: $600")
        print("5. Agua mineral grande: $1800")
        account_balance=int(input('Introduce el monto de dinero que tienes en la JUNAEB: '))
    except ValueError:
        print('Por favor ingrese un número entero.')
        continue
    if account_balance >= 300:
        print('Te quedan menos de $300. No puedes hacer mas compras.')
        break
    else:
        while account_balance >= 300:
            desodorant=300
            soup=2500 
            chocolat=1500
            cereal=600
            water=1800
            account_balance=int(input('Introduce el monto de dinero que tienes en la JUNAEB: '))
            while True:
                try:    
                    account_balance=int(input('Introduce el monto de dinero que tienes en la JUNAEB: '))
                except ValueError:
                    print('Por favor ingrese un número entero.')
                    continue
                if account_balance >= 300:
                    print('Te quedan menos de $300. No puedes hacer mas compras.')
                    break
            print(f'tienes ${account_balance} disponibles')
            print("Opciones de compra: ")
            print("1. Desodorante - $300")
            print("2. Sopa para uno - $2500")
            print("3.Chocolate - $300")
            print("4. Barra de cereal - $600")
            print("5. Agua mineral grande - $1800")
            product_choice=int(input('¿Qué producto deseas comprar? (1-5): '))
            try:
                product_choice=int(input('¿Qué producto deseas comprar? (1-5): '))
                if product_choice == 1:
                    if account_balance >= desodorant:
                        account_balance -= desodorant
                        print(f'Has comprado un desodorante. Te quedan ${account_balance}')
                    else:
                       print('No tienes suficiente dinero para comprar este prodcuto.')
                    print(f'Tienes ${account_balance} disponibles.')
                elif product_choice == 2:
                    if account_balance >= soup:
                        account_balance -= soup
                        print(f'Has comprado una sopa para uno. Te quedan ${account_balance}')
                    else:
                        print('No tienes suficiente dinero para comprar este prodcuto.')
                    print(f'Tienes ${account_balance} disponibles.')
                elif product_choice == 3:
                    if account_balance >= chocolat:
                        account_balance -= chocolat
                        print(f'Has comprado un chocolate. Te quedan ${account_balance}')
                    else:
                        print('No tienes suficiente dinero para comprar este prodcuto.')
                    print(f'Tienes ${account_balance} disponibles.')
                elif product_choice == 4:
                    if account_balance >= cereal:
                        account_balance -= cereal
                        print(f'Has comprado una barra de cereal. Te quedan ${account_balance}')
                    else:
                        print('No tienes suficiente dinero para comprar este prodcuto.')
                    print(f'Tienes ${account_balance} disponibles.')
                elif product_choice == 5:
                    if account_balance >= water:
                        account_balance -= water
                        print(f'Has comprado un agua mineral grnade. Te quedan ${account_balance}')
                    else:
                        print('No tienes suficiente dinero para comprar este prodcuto.')
                    print(f'Tienes ${account_balance} disponibles.')
                else:
                    print('Te quedan menos de $300. No puedes hacer mas compras.')
                    print(f'Dinero restante: ${account_balance}')
            except ValueError:
                print('Por favor ingrese un número entero entre el 1 al 5.')
                continue
            



    