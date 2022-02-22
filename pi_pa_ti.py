import random

print("Bienvenido a Piedra, papel o tijera")
input("Presiona ENTER para jugar")

selecciones = ("piedra","papel","tijera") 
def reglas(seleccion_j,seleccion_c):
	
	resultado = ""
	contador_j = 0
	contador_c = 0
	while contador_j <= 3 or contador_c <= 3:
		
		if seleccion_j == seleccion_c:
			resultado = "Hemos empatado jueguemos de nuevo"
			return resultado
		elif seleccion_j == 1 and seleccion_c == 3:
			resultado = "Has ganado"
			contador_j = contador_j + 1
			return resultado, contador_j
		elif seleccion_j == 2 and seleccion_c == 1:
			resultado = "Has ganado"
			contador_j = contador_j + 1
			return resultado, contador_j
		elif seleccion_j == 3 and seleccion_c == 2:
			resultado = "Has ganado"
			contador_j = contador_j + 1
			return resultado, contador_j
		elif seleccion_j == 1 and seleccion_c == 2:
			resultado = "Has perdido"
			contador_c = contador_c + 1
			return resultado, contador_c
		elif seleccion_j == 2 and seleccion_c == 3:
			resultado = "Has perdido"
			contador_c = contador_c + 1
			return resultado, contador_c
		elif seleccion_j == 3 and seleccion_c == 1:
			resultado = "Has perdido"
			contador_c = contador_c + 1
			return resultado, contador_c
		else:
			resultado = "Has seleccionado una opcion incorrecta"
		pass

print(reglas(int(input(f"selecciona 1 para {selecciones[0]} \nseleccione 2 para {selecciones[1]} \nseleccione 3 para {selecciones[2]}\n")),random.randint(1,3)))
