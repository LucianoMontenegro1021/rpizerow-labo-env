
import gpiozero
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

led_rojo = PWMLED(17)
led_azul = PWMLED(27)

R_REF = 10000.0
BETA = 3900.0

GAIN = 1

def main():
	while True:
        	temp_setpoint = read_potentiometer()
        	actual_temp = read_thermistor()
        	control_leds(temp_setpoint, actual_temp)
        	print(f"Setpoint: {temp_setpoint:.2f}°C, Actual: {actual_temp:.2f}°C")
        	time.sleep(1)

def read_potentiometer():
    	value = adc.read_adc(0, gain=GAIN)
    	temperature_setpoint = value * 30.0 / 32767.0
    	return temperature_setpoint

def read_thermistor():
	value = adc.read_adc(1, gain=GAIN)
	resistance = R_REF * (32767.0 / value - 1.0)
	temperature = 1.0 / (1.0 / 298.15 + (1.0 / BETA) * (resistance / R_REF - 1.0)) - 273.15
	return temperature

def control_leds(temp_setpoint, actual_temp):
	difference = actual_temp - temp_setpoint
	max_difference = 5.0
	duty_cycle = min(abs(difference) / max_difference, 1.0)

	if difference > 0:
		led_azul.value = duty_cycle
        	led_rojo.value = 0
    	else:
        	led_rojo.value = duty_cycle
        	led_azul.value = 0


if __name__ == "__main__":
	main()
