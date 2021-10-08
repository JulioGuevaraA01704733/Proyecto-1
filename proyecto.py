def IMC (peso1, estatura1):
    return peso1 / (estatura1*estatura1)

def IMC_ideal (edad1, sexo1):
    if edad1 <= 15 :
        return "Dado que estás en una etapa de desarrollo, tu IMC ideal no es establecible."
    elif edad1 >= 65 :
        return "Su IMC ideal está entre 25 y 30."
    else:
        if sexo1 == "hombre" or sexo1 == "Hombre" :
            ideal_inf = 19
            ideal_sup = 24
        elif sexo1 == "mujer" or sexo1 == "Mujer" :
            if edad1 == 16 :
                return "Tu IMC ideal está entre 19 y 24."
            elif edad1 == 17 or edad1 == 18 :
                return "Tu IMC ideal está entre 20 y 25."
            elif edad1 >= 45 and edad1 <= 54 :
                return "Tu IMC ideal está entre 23 y 28."
            elif edad1 >= 55 and edad1 <= 64 :
                return "Tu IMC ideal está entre 24 y 29."
            else:
                ideal_inf = 21
                ideal_sup = 26
        ideal_inf = ideal_inf + edad_f
        ideal_sup = ideal_sup + edad_f
        print("Tu IMC ideal está entre ", ideal_inf, " y ", ideal_sup)

#TMC representa Tasa Metabólica Basal
def TMC(peso2, estatura2, edad2, sexo2):
    if sexo2 == "mujer" or sexo2 == "Mujer" :
        return 655 + 9.6 * peso2 + 180 * estatura2 - 4.7 * edad2
    else :
        return 66 + 13.7 * peso2 + 500 * estatura2 - 6.75 * edad2
    
def TMC2(peso2, estatura2, edad2, sexo2, ejercicio):
    if ejercicio == 1:
        return (TMC(peso2, estatura2, edad2, sexo2) * 1.2)
    elif ejercicio == 2 :
        return (TMC(peso2, estatura2, edad2, sexo2) * 1.375)
    elif ejercicio == 3 :
        return (TMC(peso2, estatura2, edad2, sexo2) * 1.55)
    elif ejercicio == 4 :
        return (TMC(peso2, estatura2, edad2, sexo2) * 1.72)
    elif ejercicio == 5 :
        return (TMC(peso2, estatura2, edad2, sexo2) * 1.9)

lista_consejos = ["Puedes intentar caminar y/o trotar una vez por semana.", "Esfuérzate por ser constante.", "Procura consumir las calorías necesarias.", "Mantén un balance entre descanso y trabajo", "Sé conciente de la capacidad de tu cuerpo."]

def consejo(nivel_e):
    nivel_t = nivel_e - 1 
    print("Toma un consejo: ", lista_consejos[nivel_t])

print("Hola, esta es tu calculadora de IMC.")
print("¿Cuál es tu peso en kilogramos?")
peso = float(input())
print("¿Cuál es tu estatura en metros?")
estatura = float(input())
print("¿Cuál es tu sexo, hombre o mujer?")
sexo = str(input())
print("¿Cuál es tu edad?")
edad = int(input())
print("Indica tu nivel de ejercicio: \n 1 si haces poco ejercicio o nulo \n 2 si haces ejercicio ligero de 1 a 3 días de la semana \n 3 si ejercicio moderado, de 3 a 5 días a la semana \n 4 si haces ejercicio de 6 a 7 días a la semana \n 5 si entrenas diariamente mañana y tarde")
nivel_ejercicio = int(input())
print("Tu IMC es de","%.2f" % IMC(peso, estatura))
print(IMC_ideal(edad, sexo))
print("Consumes alrededor de","%.2f" % TMC2(peso, estatura, edad, sexo, nivel_ejercicio), "calorías diarias.")
print(consejo(nivel_ejercicio))
