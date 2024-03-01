nom = input('Entre votre nom \n')
age = input('Entre votre age\n')
if age != 0:
    next_age = int(age) + 1
    print(f'Tu tappelles',{nom},'et ton prochain age est: ',{next_age})
else:
    print('erreur')
