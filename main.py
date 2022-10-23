#ejercicio 1
import math
def area_circulo():
     Radio = float(input("Dime el radio de un círculo:\n")) 
     Area = math.pi*(Radio*Radio)
     return 'El área de un circulo de radio {} es de {} unidades cuadradas.'.format(Radio, Area)

print (area_circulo())
#ejercicio2
def lee_numero():
    return int(input("Introduce un número: "))
 
def mayor(a,b,c):
    if a>b and a>c:
        return a
    if b>c:
        return b
    else:   
        return c
 
valores=[]
for i in range(3):
    valores.append(lee_numero())
 
print(f"El número con mayor valor de los tres es el {mayor(valores[0], valores[1],valores[2])}")

# ejercicio 3
def imc():
    IMC = peso / (altura*altura)

    if IMC<18.5:
        return "Bajo Peso"
    elif IMC>=18.5 and IMC<=25:
        return "Peso Saludable"
    elif IMC>=30:
        return "Obesidad"
    return "Sobrepeso"
    
print("Vamos a calcular tu índice de masa corporal. ")
peso = int(input("introduce tu peso en kilogramos: "))
altura = round(float(input("introduce tu altura: ")), 2)
print(imc())
