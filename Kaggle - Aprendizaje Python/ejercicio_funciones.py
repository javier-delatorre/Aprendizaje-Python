
# Utilizar una funcion que calcule los metros cuadrados de una habitacion y se creara 
# otra funcion que calcule la suma de los metros cuadrados de toda una casa segun la cantidad de los cuartos, 
# la segunda funcion sera para sumar los metros cuadrados de 5 habitaciones
def calculo_metros_cuadrados(metros_lineales_1, metros_lineales_2):
    metros_cuadrados = metros_lineales_1 * metros_lineales_2
    return(metros_cuadrados)

def calculo_habitaciones(h1_1,h1_2,h2_1,h2_2,h3_1,h3_2,h4_1,h4_2,h5_1,h5_2):
    m1 = calculo_metros_cuadrados(h1_1, h1_2)
    m2 = calculo_metros_cuadrados(h2_1, h2_2)
    m3 = calculo_metros_cuadrados(h3_1, h3_2)
    m4 = calculo_metros_cuadrados(h4_1, h4_2)
    m5 = calculo_metros_cuadrados(h5_1, h5_2)
    suma_total = m1 + m2 + m3 + m4 + m5
    return(suma_total)