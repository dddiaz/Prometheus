Prometheus README

Project Prometheus is a Raspberry Pi 2 project.

Concept:
	Create a solution to automatically back up external drives to amazon webservices (S3 and glacier).
	Will be possible by deploying this python3 app to the raspberry pi, and running it through the command line.

Dev Notes:
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
