#!/usr/bin/env bash
WEB_PATH='/var/www/jobsentry'
cd $WEB_PATH
/usr/local/bin/scrapy crawl lagou --logfile /var/www/log/lagou.log