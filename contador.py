def contador (i, f, p):
    print(f'Contagem de {1} ate {f} de {p} em {p}')
     cont = i
     while cont <= f:
         print(f'{cont} ', end='')
         cont += p
    print('Resultado!')


#Programa principal
contador(1, 10, 2)
