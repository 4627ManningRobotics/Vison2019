import queue
import threading
import time
import json
import math

class Strip_Handler:

	def __init__(self, queue_size):
		#using a queue to store unfiltered data
		self.strip_queue = queue.Queue(queue_size)
		self.strip_data = queue.Queue(queue_size)

	def put(self, message):
		if(self.strip_queue.full()):
			self.ball_queue.get(2)
			self.ball_queue.put(message, 2)
		else:
			self.ball_queue.put(message, 2)

	def get(self):
		if(self.strip_queue.empty()):
			pass
		else:
			return self.stip_data.get(2)

	def loop(self):
		while True:
			if(self.strip_queue.empty()):
				time.sleep(0.0003)
			else:
				message = self.strip_queue.get(2)
				for key in message:
					if key == "Distance": #Y isn't the actual why, its the displacment from the object
						dist = message[key]
						message["Y"] = dist * math.sin(message["Angle"])
						message["X"] = dist * math.cos(message["Angle"])
				self.strip_data.put(m)
				time.sleep(0.0001)



