a, b = 91, 101
tablero = []
for i in range(2, 11):
    aux = []
    if i%2==0:
        aux = list(range(a, b))
        aux.reverse()
    else:
        aux = list(range(a, b))
    tablero.append(aux)
    a, b = a-10, b-10
tablero.append(['01, 02, 03, 04, 05, 06, 07, 08, 09, 10'])
for i in tablero:
    print(i)
