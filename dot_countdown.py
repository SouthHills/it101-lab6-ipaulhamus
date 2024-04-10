from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]

s = 10

timer = [
G, G, G, G, G, G, G, G,
G, G, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X
]

sense.set_pixels(timer)

for i in range(0, 10):
    sleep(1)
    timer[i] = R
    sense.set_pixels(timer)


for i in range(0, 10):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
        

