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

#Steps
# 1 - pip install awscli
# 2 - run "aws configure" frm the command line
# 3 - enter the crendentials retireved from you aws iam profile
#       -see http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html
#       - make sure user has these credentials:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::your-s3-bucket",
                "arn:aws:s3:::your-s3-bucket/*"
            ]
        }
    ]
}


TODO:
potentially add shortcut to auto install python 3