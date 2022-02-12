import random
selecciones = ("piedra","papel","tijera") 
print("Bienvenido a Piedra, papel o tijera")
input("Presiona ENTER para jugar")
computadora = random.randint(1,3)
jugador = int(input(f"selecciona 1 para {selecciones[0]} \nseleccione 2 para {selecciones[1]} \nseleccione 3 para {selecciones[2]}\n"))
contador_j = 0
contador_c = 0
while contador_j <= 3 or contador_c <= 3:
	if jugador == 1 and computadora == 1:
		print("Hemos empatado.\nJuguemos de nuevo")
		break
	elif jugador == 2 and computadora == 2:
		print("Hemos empatado.\nJuguemos de nuevo")
		break
	elif jugador == 3 and computadora == 3:
		print("Hemos empatado.\nJuguemos de nuevo")
		break
	elif jugador == 1 and computadora == 3:
		print("Has ganado")
		contador_j = contador_j + 1
		break
	elif jugador == 2 and computadora == 1:
		print("Has ganado")
		contador_j = contador_j + 1
		break
	elif jugador == 3 and computadora == 2:
		print("Has ganado")
		contador_j = contador_j + 1
		break
	elif jugador == 1 and computadora == 2:
		print("Perdiste")
		contador_c = contador_c + 1
		break
	elif jugador == 2 and computadora == 3:
		print("Perdiste")
		contador_c = contador_c + 1
		break
	elif jugador == 3 and computadora == 1:
		print("Perdiste")
		contador_c = contador_c + 1
		break
	else:
		print("Elegiste una opcion incorrecta")
input(f"Vamos \n{contador_j} jugador \n{contador_c} computadora")
