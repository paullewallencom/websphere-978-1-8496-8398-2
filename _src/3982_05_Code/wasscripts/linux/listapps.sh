#!/bin/bash
export var=`/var/apps/was8/profiles/appsrv01/bin/wsadmin.sh -username wasadmin -password wasadmin -lang jython -c 'AdminApp.list()'`
export raw_apps=$(echo $var|cut -f 2 -d \')
export parsed_apps=$(echo ${raw_apps} | sed 's/\\n/ /g')
for a in $parsed_apps
do
 echo $a
done