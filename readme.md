# Calculadora IMC

## Julio Eugenio Guevara A01704733

"""

Algoritmo para cacular el Índice de Masa Corporal (IMC) de una persona, el rango recomendado de IMC, y  las calorías aproximadas que se utilizan en un día;  a partir de su peso, sexo, edad, estatura y nivel de actividad física.

Guía para TMB:

http://gymvirtual.com/como-calcular-las-calorias-que-necesitas/

E(O)= Imprimir preguntas ¿Cuál es tu peso, sexo, edad, estatura?

Proceso: 
1. Leer y registrar respuestas como variables
2. Efectuar cálculo para definir el IMC. Peso en kg / (altura en metros)**2
3. Si IMC<x , entonces
  Imprimir("Estás en el rango de peso bajo con un IMC de ")
  Imprimir(IMC)
  si IMC>=x y IMC<=y , entonces
  Imprimir("Estás en el rango de peso normal con un IMC de ")
  Imprimir (IMC)
  etc.
  
  
4. Si género=mujer, entonces

    Si edad<x, entonces
    
    Imprimir("Tu indice de masa coporal ideal es entre x y z")
    
    Si edad>=x y edad<=x, entonces
    
    Imprimir("Tu indice de masa coporal ideal es entre x y z")
    
    etc.
    
    
    Si no, entonces
    
    Si edad<=x, entonces
    
    Imprimir("Tu indice de masa coporal ideal es entre x y z")
    
    Si edad>=x y edad<=x, entonces
    
    Imprimir("Tu indice de masa coporal ideal es entre x y z")
    
    etc.
    
    
E(F)= Impresión de tu IMC y rango recomendado.

"""


print("Hola, esta es tu calculadora de IMC.")

print("¿Cuál es tu peso en kilogramos?")

peso = float(input())

print("¿Cuál es tu estatura en metros?")

estatura = float(input())

IMC = peso / (estatura*estatura)

print("Tu IMC es de ","%.2f" % IMC)
