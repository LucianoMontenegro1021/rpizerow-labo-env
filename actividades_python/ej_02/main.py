from gpiozero import LED
from signal import pause

led1 = LED(13)
led2 = LED(19)
led3 = LED(26)

led1.blink(on_time=1, off_time=1, n=None, background=True)
led2.blink(on_time=0.5, off_time=0.5, n=None, background=True)
led3.blink(on_time=0.25, off_time=0.25, n=None, background=True)

pause()
