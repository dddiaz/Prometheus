#Project Prometheus Cron Job
#By: Daniel Diaz 2015
#Purpose: To periodically sync with amazon services

#Note you must add the cron job call in /etc/cron.d

#testing python cron job
f = open('/home/pi/cron.txt','a')
f.write('test\n')
f.close()