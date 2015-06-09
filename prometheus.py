__author__ = 'danieldiaz'

#Project:	Prometheus Cron Job
#By: 		Daniel Diaz 2015
#Web:		www.danieldelvindiaz.com
#Purpose: 	To periodically sync with amazon services
#Note: 		You must add the cron job call in /etc/cron.d
#Python-V: 	3 (Must be called with python3 in Rasberry Pi instead of deafault 2.x)

#Notes: hey u have seens the ospath join stuff in the django, ref that

import datetime
import subprocess

class install:
    """
    Make sure necessary packages are installed
    Note if this file is running, then python 3 is already installed
    """
    def __init__(self):
        self.setup = False

    def install_aws_s3(self):
        ##NEED SUDO!
        print("Please make sure you have an aws acct,and an aws bucket setup.")
        print("Also make sure you have installed the amazong web services cli")
        print("Type help at the prompt for instructions.")
        pass

class prometheus_prompt:
    """
    prometheus prompt using prompt.py
    """
    def __init__(self):
        self.command = ""

    def menu(self):
        print("\tPlease select an option:\n" + \
              "\t\tGlacier: Backup folder/drive to Amazon Glacier\n" + \
              "\t\tSimple: Backup folder/drive to Amazon S3\n" + \
              "\t\tScheduled: Create Scheduled Backup \n" +\
              "\t\tHelp: help \n" +\
              "\t\tQuit: Quit \n" +\
              "")

    def get_command(self):
        command = input("Please enter your command: ")
        if (command != ""):
            command = command.lower()
            command = command[0]
        else:
            #user didnt enter anything so quit
            command = "q"
        self.command = command
        return command

    def handle_command(self):
        if (self.command == 'q'):
            return
        elif (self.command == 'h'):
            print("http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html")
            #run aws script
        else:
            self.aws_command()

    def aws_command(self):
        s = aws_sync()
        s.sync_start()
        return

class aws_sync:
    def __init__(self):
        self.log = logger()
        #self.source_folder = "/mnt/usb"
        self.source_folder = r'/Users/danieldiaz/Library/Mobile\ Documents/com\~apple\~CloudDocs/Dev/Work/Prometheus/test_folder'
        self.dest_folder = "s3://prometheus-bucket-raspberry-pi"

    def sync_start(self):
        self.log.log_start()
        self.sync()
        return

    def sync(self):
        command = "aws s3 ls " + self.dest_folder
        return_code = subprocess.call(command,shell=True)
        command = "aws s3 sync " + self.source_folder + " " + self.dest_folder
        return_code = subprocess.call(command,shell=True)
        command = "aws s3 ls " + self.dest_folder
        return_code = subprocess.call(command,shell=True)
        #return_code = subprocess.call("aws s3 ls s3://prometheus-bucket-raspberry-pi",shell=True)
        #return_code1 = subprocess.call("aws s3 sync /mnt/usb s3://prometheus-bucket-raspberry-pi",shell=True)
        #return_code2 = subprocess.call("aws s3 ls s3://prometheus-bucket-raspberry-pi",shell=True)
        #print("Return Code", return_code,return_code1,return_code2)
        return

class logger:
    #TODO: log file should be passed in with ospath maybe?
    def log_start(self):
        #f = open('/Users/danieldiaz/Desktop/log.txt','a')
        f = open(r'/Users/danieldiaz/Library/Mobile Documents/com~apple~CloudDocs/Dev/Work/Prometheus/test_folder/test.txt','a')
        f.write("Starting Sync: ")
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.write('\n')
        f.close()








if __name__ == '__main__':
    print("Welcome to Prometheus")
    print("Project By: www.danieldelvindiaz.com")
    #setup
    i = install()
    i.install_aws_s3()
    # prompt
    p = prometheus_prompt()
    while p.command != "q":
        p.menu()
        p.get_command()
        p.handle_command()











