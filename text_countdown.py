from sense_emu import SenseHat
from time import sleep

sense_emulator = SenseHat()

counter = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
red_val = 148
green_val = 108 

for count in counter:
    sleep(1)
    if count == 0:
        sense_emulator.show_letter('0', [128, 0, 128])
    else:
        sense_emulator.show_letter(f'{count}', [red_val, green_val, 0])
        red_val = red_val + 10
        green_val = green_val - 10