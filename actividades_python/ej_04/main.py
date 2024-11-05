import gpiozero
import Adafruit_ADS1x15
import time

# Inicializar la instancia de ADC
sensor_adc = Adafruit_ADS1x15.ADS1115()

# Configuración de los pines GPIO para los LEDs
led_rojo = gpiozero.PWMLED(17)
led_azul = gpiozero.PWMLED(27)

RESISTENCIA_REF = 10000.0  # Resistencia en ohmios del divisor
BETA_TERMISTOR = 3900.0    # Constante Beta del termistor

GANANCIA_ADC = 1

def iniciar():
	while True:
        	setpoint_temp = leer_potenciometro()
        	temp_actual = leer_termistor()
        	ajustar_leds(setpoint_temp, temp_actual)
        	print(f"Setpoint: {setpoint_temp:.2f}°C, Actual: {temp_actual:.2f}°C")
        	time.sleep(1)

def leer_potenciometro():
    	# Leer el valor del potenciometro
    	valor = sensor_adc.read_adc(0, gain=GANANCIA_ADC)
	# Escalar el valor a un rango de 0 a 30 grados Celsius
    	setpoint_temp = valor * 30.0 / 32767.0
    	return setpoint_temp

def leer_termistor():
   	# Leer el valor del termistor
	valor = sensor_adc.read_adc(1, gain=GANANCIA_ADC)
	# Convertir el valor leído del termistor a temperatura en grados Celsius
	resistencia = RESISTENCIA_REF * (32767.0 / valor - 1.0)
	temperatura = 1.0 / (1.0 / 298.15 + (1.0 / BETA_TERMISTOR) * (resistencia / RESISTENCIA_REF - 1.0)) - 273.15
	return temperatura

def ajustar_leds(setpoint_temp, temp_actual):
	diferencia = temp_actual - setpoint_temp
	diferencia_maxima = 5.0
	intensidad = min(abs(diferencia) / diferencia_maxima, 1.0)

	if diferencia > 0:
		# La temperatura actual está por encima del setpoint, activar LED azul
		led_azul.value = intensidad
        	led_rojo.value = 0
    	else:
        	# La temperatura actual está por debajo del setpoint, activar LED rojo
        	led_rojo.value = intensidad
        	led_azul.value = 0

if __name__ == "__main__":
	iniciar()