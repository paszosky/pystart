import math
import time
x = 0.0

while True:
	print((" " * int(41 + math.sin(x) * 40)), "Przerwa do 20:10")
	x += 0.03
	time.sleep(0.05)
