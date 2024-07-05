
from gpiozero import LED, Buzzer
from signal import pause

buzzer = Buzzer(22)

led_rojo = LED(19)

led_verde = LED(26)

led_azul = LED(13)

while True:
	orden = input("Ingresar una orden, buzz o rgb")
	if orden == "rgb":
		opcion = input("Elegir entre "red", "green" o "blue".")
	elif orden == "buzz":
		opcion = input("Elegir entre on u off")

	if orden == "buzz":
		if opcion == "on":
			buzzer.on()
		elif opcion == "off":
			buzzer.off()


	elif orden == "rgb":
		if opcion == "red":
			led_rojo.toggle()
		elif opcion == "green":
			led_verde.toggle()
		elif opcion == "blue".
			led_azul.toggle()

pasue()

