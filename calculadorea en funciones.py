def leer_int_teclado(mensaje):
    leer_en_teclado = int(input(mensaje))
    return leer_en_teclado

def suma(a,b):
    resultado_de_suma= a+b
    return resultado_de_suma

def resta(a,b):
    resultado_de_resta= a-b
    return resultado_de_resta

def multiplicacion (a,b):
    resultado_de_multiplicacion= a*b
    return resultado_de_multiplicacion

def division (a,b):
    resultado_de_divisiona= a/b
    return resultado_de_division

operaciones_disponibles=["Suma = 1" , "Resta = 2" , "Multiplicacion = 3 ", "Division = 4"]
for valor in operaciones_disponibles:
 print(valor)

operacion = leer_int_teclado("seleccione una operacion:")
a = leer_int_teclado("seleccione un numero a:")
b = leer_int_teclado("seleccione un numero b:")

if operacion == 1 :
    
    resultado_suma = suma(a,b)
    print(resultado_suma)

elif operacion == 2 :
    resultado_resta= resta(a,b)
    print(resulatado_resta)

elif  operacion== 3:
    resultado_multiplicacion= multiplicacion(a,b)
    print(resulado_multiplicacion)

elif  operacion== 4:         
    resultado_division= division(a,b)
    print(resultado_division)
