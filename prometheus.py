#Project:	Prometheus Cron Job
#By: 		Daniel Diaz 2015
#			www.danieldelvindiaz.com
#Purpose: 	To periodically sync with amazon services
#Note: 		You must add the cron job call in /etc/cron.d
#Python-V: 	3 (Must be called with python3 in Rasberry Pi instead of deafault 2.x)
#TODO:		-test cron job exists
#			-test python installed
#			-test python installer installed
#			-test awscli installed/setup
#			-google cli????
#			-run aws sync


class amazonS3Sync:
	"""
		Implements a class to sync with amazon amazonS3
	"""
	def __init__(self):
		"""
			__init__
		"""
		self.complete = false

	def printSyncStart(self):
		"""
			Print to cron.txt a start sync time
		"""
		f = open('/home/pi/cron.txt','a')
		f.write('Starting sync: ')
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\n')
		f.close()

	def syncToS3(self):
		"""
			Sync to aws s3 with awscli
		"""
		z=1

	def execute(self):
		self.printSyncStart()
		self.syncToS3()

if '__name__' == '__main__':
	import datetime
	backup = amazonS3Sync()
	backup.execute()





