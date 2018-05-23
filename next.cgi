#!/bin/bash
saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS
loopNum=${parm[0]}

if [[ -z $loopNum ]]; then
	/usr/bin/mpc -h localhost next
else
	for (( temp=0; temp<$loopNum; temp++)); do
		/usr/bin/mpc -h localhost next
	done
fi
