import time
import datetime

startTime = time.time()
lastTime = startTime
lap = 1
"""
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lap, totalTime, lapTime), end='')
		lap += 1
		lastTime = time.time()
except KeyboardInterrupt:
	print("\nTotal: ", totalTime)
	print('\nDone')

timeformat = '{:02d}:{:02d}'.format(mins, secs)
print(timeformat, end='\r')
"""



try:
	while True:
		dt = datetime.datetime.now()
		print('{:02d}:{:02d}'.format(dt.minute, dt.second), end='\r')
except KeyboardInterrupt:
	print("\nDone")