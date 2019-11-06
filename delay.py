from random import randint
import datetime
from time import sleep

class Delay:
	def simple_delay_by_sleep(self, seconds):
		"""
		This method creates a simple delay by sleeping for 'x' seconds
		"""
		sleep(seconds)
		return

	def cpu_intensive_delay(self, seconds):
		"""
		This method creates a delay of 'x' seconds. This may not be exact 'x' seconds, but will be. very close.
		"""

		# Take the start time into a variable.
		start_time = datetime.datetime.now()

		print ("Strting at: {}".format(start_time))

		while (True):

			# Generate two random integers and do some calculations. This is just to induce some load on the CPU
			a = randint(100000, 9999999)
			b = randint(100000, 9999999)
			c = a*b
			d = a/b

			# Check time. If we pass 'x' seconds, exit.
			if self.get_the_time_difference(start_time) > seconds:
				print ("Exiting at: {}".format(datetime.datetime.now()))
				break

		return

	def get_the_time_difference (self,start_time):
		"""
		Take start time parameter. Get current time and return the difference in seconds.
		"""
		end_time = datetime.datetime.now()
		delta = end_time - start_time
		return delta.total_seconds()
