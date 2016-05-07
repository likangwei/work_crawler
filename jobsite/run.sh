#!/usr/bin/env bash
netstat -anp 2>/dev/null|grep ":9955"|awk '{print $7}'|awk -F "/" '{print $1}'|xargs kill -9
sleep 3

WEBPATH="/var/www/jobsentry/jobsite/"
cd $WEBPATH
python manage.py migrate
python manage.py runfcgi method=threaded host=127.0.0.1 port=9955