__author__ = 'danieldiaz'

#Project:	Prometheus Cron Job
#By: 		Daniel Diaz 2015
#Web:		www.danieldelvindiaz.com
#Purpose: 	To periodically sync with amazon services
#Note: 		You must add the cron job call in /etc/cron.d
#Python-V: 	3 (Must be called with python3 in Rasberry Pi instead of deafault 2.x)

import datetime
import subprocess

if __name__ == '__main__':
    print("Welcome to Prometheus")
    print("Project By: www.danieldelvindiaz.com")
