listproduct="""
Lista de productos en Okidoki Market:
1. Desodorante: $300
2. Sopa para uno: $2500
3.Chocolate: $300
4. Barra de cereal: $600
5. Agua mineral grande: $1800"""
optionsbuy="""
Opciones de compra:
1. Desodorante          - $300
2. Sopa para uno        - $2500
3.Chocolate             - $300
4. Barra de cereal      - $600
5. Agua mineral grande  - $1800
"""
#precios de los productos
prices={
    1: 300,
    2: 2500,
    3: 300,
    4: 600,
    5: 1800,
}
#solicitar el monto de dinero disponible
while True:
    try:
        print(listproduct)
        account_balance=int(input('Introduce el monto de dinero que tienes en la JUNAEB: '))
        if account_balance < 0:
            print('Por favor ingresa un numero positivo.')
        else:
            break
    except ValueError:
        print('Por favor ingrese un número entero.')
#Ciclo de Compras
while account_balance >= 300:
    print(f'Tienes ${account_balance} disponibles.')
    print(optionsbuy)
    try:
        product_choice = int(input('¿Qué producto deseas comprar? (1-5): '))
        if product_choice in prices:
            if account_balance >= prices[product_choice]:
                account_balance -= prices[product_choice]
                print(f'Has comprado el producto. Te quedan ${account_balance}')
            else:
                print('No tienes suficiente dinero para comprar este producto.')
        else:
            print('Opción inválida. Por favor ingrese un número entre 1 y 5.')
    except ValueError:
        print('Por favor ingrese un número entero entre 1 y 5.')
# Mensaje final si no se puede hacer más compras
if account_balance < 300:
    print('Te quedan menos de $300. No puedes hacer más compras.')
    print(f'Dinero restante: ${account_balance}')