
import time
import pigpio

sq = 13

square = []

square.append(pigpio.pulse(1<<sq, 0, 4))
square.append(pigpio.pulse(0, 1<<sq, 4))

pi = pigpio.pi()

pi.set_mode(sq, pigpio.OUTPUT)
pi.wave_add_generic(square)

wid = pi.wave_create()
print("Here")
if wid >= 0:
    pi.wave_send_repeat(wid)
    time.sleep(1)
    pi.wave_tx_stop()
    pi.wave_delete(wid)

pi.stop()
