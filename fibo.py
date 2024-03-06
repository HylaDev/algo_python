def fibo_num_position(nombre):
    a = 0
    b = 1
    position = 1
    while b <= int(nombre):
        a = b
        b = a + b
        position = position + 1
        print(a,b,position)
    if b == nombre:
        return f'Le nombre {nombre} se trouve à la position {position}'
    else:
        return f'Le nombre {nombre} ne se trouve pas dans la suite de fibo'


def main():
    
    while True:
        print('1. Afficher la position')
        print('2. Afficher le nombre à cette position')
        print('3. Exit')

        choix = input('Entrer votre choix')

        if choix == '1':
            nombre = input('Entrez le nombre \n')
            print(fibo_num_position(nombre))
        elif choix == '2':
            pass
        elif choix == '3':
            break


if __name__ == '__main__':
    main()
