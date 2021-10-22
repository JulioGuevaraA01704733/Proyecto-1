from fpdf import FPDF

def IMC (peso1, estatura1):
    """
    Recibe el peso en kilogramos y la estatura en metros del usuario. Realiza la operación aritmética para la obtención del número que llamamos IMC y devuelve dicho valor.
    Las siglas IMC representan Índice de Masa Corporal, valor de gran utilidad para el análisis de la salud.
    """
    return peso1 / (estatura1*estatura1)

def IMC_ideal (edad1, sexo1):
    """
    Recibe la edad y sexo del usuario -éste último se da en string-, ya que existen dos bases de referencia para determinar el IMC ideal, una para cada sexo. 
    Existen dos rangos en los que es indiferente el sexo, los cuales se ven representados en los primeros condicionales de la función.
    Si ninguno de los dos es el caso, se manipula aritmeticamente el valor de la edad para que, al sumarla con los rangos iniciales,
    resulte en el valor superior e inferior (los cuales varían dependiendo del sexo) del rango correspondiente. Se resuelve para las excepciones con una estructura más
    de condiciones. Finalmente, la función regresa el rango dentro del cual se encuentra el IMC ideal del usuario.
    """
    if edad1 <= 15 :
        return "Dado que estás en una etapa de desarrollo, tu IMC ideal no es establecible."
    elif edad1 >= 65 :
        return "Su IMC ideal está entre 25 y 30."
    else:
        edad_f = (edad1 - 15) // 10
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
    return ""

#TMC representa Tasa Metabólica Basal
def TMC(peso2, estatura2, edad2, sexo2):
    """
    Esta función recibe el peso, la estatura, edad y sexo del usuario. Dependiendo del sexo, decide con qué valores llevar a cabo una operación matemática (la 
    cual emplea las demás variables que recibió la función) que resulta en una aproximación a la cantidad de calorías diarias consumidas por el usuario. 
    EL valor de esta operación es lo que devuelve la función.
    """
    if sexo2 == "mujer" or sexo2 == "Mujer" :
        return 655 + 9.6 * peso2 + 180 * estatura2 - 4.7 * edad2
    else :
        return 66 + 13.7 * peso2 + 500 * estatura2 - 6.75 * edad2
    
def TMC2(peso2, estatura2, edad2, sexo2, ejercicio):
    """
    Esta función mejora la aproximación realizada por la función TMC empleando una variable extra. La función recibe el valor que regresó la variable TMC (por lo que
    podría decirse que también recibe peso, estatura, edad y sexo) y la variable que representa el nivel de ejercicio que realiza el usuario, el cual se describe a través
    de números enteros del 1 al 5, cada uno correspondiente a una descripción particular de la cantidad de ejercicio que se realiza. Con ayuda de una estructura condicional, 
    la función decide cuánto aumentar el valor regresado por la función TMC, con base en el nivel de ejercicio que se indicó.
    """
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
lista_porras = ["¡Échale ganas, haz ejercicio!", "¡Sigue esforzándote!", "¡Wow, haces mucho ejercicio!", "¡Impresionante! ¿ejercicio casi diario? Eres grande","¡Bravo, qué nivel!"]
lista_com = [lista_consejos, lista_porras]

def comentario(decision1, nivel_e):
    """
    Esta función hace uso de un string que da el usuario al ser hecho decidir entre dos opciones y de la variable que representa el nivel de ejercicio que hace
    el usuario, igual que en la función TMC2 (Estas son las variables que recibe). Dependiendo de lo que haya escrito el usuario, la función le asigna un valor 
    u otro a la variable que posteriormente se usará para describir a qué sublista llamar, dentro de la lista_com, la cual se ve compuesta por una lista de consejos
    y otra de porras. Al valor de la variable nivel de ejercicio se le resta uno y el resultado se designa a una nueva variable, para que ésta se alinee con las características
    de los índices de las listas, y se utilice para llamar al elemento correcto de la sublista correspondiente, ya que cada consejo o porra está en orden respectivo
    al nivel de ejercicio. Regresa el elemento correspondiente al nivel de ejercicio de la lista correspondiente a la desición.
    """
    nivel_t = nivel_e - 1 
    if decision1 == "porra" or decision1 == "Porra" or decision1 == "porras" or decision1 == "Porras" or decision1 == "PORRAS" :
        pos_com = 1
    else :
        pos_com = 0
    print(lista_com[pos_com][nivel_t])
    return ""

def rutina(nivel):
    """
    Esta variable recibe el nivel de ejercicio del usuario, para con este decidir si recomendar una rutina de ejercicios. La variable también se usa para determinar
    cuantas repeticiones se harán y cuántos minutos de cardio. Si el nivel de ejercicio es menor a 4, la función regresa una tabla con 6 días de la semana y la cantidad
    de ejercicio a hacer en cada uno. Se usan ciclos while para repetir el proceso hasta completar la tabla.
    """
    if nivel < 4 :
        dia = 1
        tiempo = 15 * nivel
        repeticiones = 10 * nivel
        limite_tiempo = 15 * nivel - 1
        limite_repeticiones = 10 * nivel + 1
        print("Incluimos una rutina que te podría interesar, donde semanalmente trabajas 6 días y descansas 1:")
        while dia < 7 :
            print("Día ", dia, ": ", tiempo, " minutos de cardio y ", repeticiones, " abdominales.")
            if tiempo > limite_tiempo :
                tiempo = tiempo - 10
            else :
                tiempo = tiempo + 10
            if repeticiones < limite_repeticiones :
                repeticiones = repeticiones + 5
            else :
                repeticiones = repeticiones - 5
            dia = dia + 1
    return ""

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
print("¿Qué prefieres, consejo o porras?")
decision = str(input())
print("Tu IMC es de","%.2f" % IMC(peso, estatura))
print(IMC_ideal(edad, sexo))
print("Consumes alrededor de","%.2f" % TMC2(peso, estatura, edad, sexo, nivel_ejercicio), "calorías diarias.")
print(comentario(decision, nivel_ejercicio))
print(rutina(nivel_ejercicio))
#En esta sección se imprimen todas las preguntas que le piden al usuario las variables que se utilizarán, además de posteriormente imprimir lo que devuelve cada función
pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', '', 12)
pdf.cell(200, 10, 'Reporte', ln=1)
pdf.cell(250, 10, str(IMC(peso, estatura)), ln=2)
pdf.cell(200, 10, str(IMC_ideal(edad, sexo)), ln=3)
pdf.cell(200, 10, str(TMC2(peso, estatura, edad, sexo, nivel_ejercicio)), ln=4)
pdf.cell(200, 10, str(comentario(decision, nivel_ejercicio)), ln=5)
pdf.cell(200, 10, str(rutina(nivel_ejercicio)), ln=6)
pdf.output('ReporteCalculadoraIMC.pdf', 'F')
#Para generar un pdf con lo que regresan las funciones
