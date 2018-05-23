#!/bin/bash
time=$(($(./.mpcGetTotal)-$(./.mpcGetElapsed)));
status=$(/usr/bin/mpc -h localhost status);
IFS=' [p' read -r status <<< "$status"
echo "content-type: text/html"
echo ""
echo $time
echo "<br>"
echo $status
exit 0

