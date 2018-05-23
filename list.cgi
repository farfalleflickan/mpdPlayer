#!/bin/bash
readarray -t status_array <<< "$(/usr/bin/mpc -h localhost playlist)"
name=$(/usr/bin/mpc -h localhost -p 8999 status)
echo "content-type: text/html"
echo ""
echo "<html>"
echo "<head>"
echo -e "<title>Dario Rostirolla</title>\n<meta charset='UTF-8'>\n<meta name='description' content='Dario Rostirolla'>\n<meta name='keywords' content='HTML, CSS'>\n<meta name='author' content='Dario Rostirolla'>\n<link rel='icon' type='image/png' href='img/favicon.png'/>\n<link rel='stylesheet' type='text/css' href='https://dariorostirolla.se/music/music.css'>"
echo "</head>"
echo "<body>"
echo "<ul>"
newIndex=0;
currentlyPlaying=0;
IFS=" [p" read -r name <<< "$name"
for ((i=0; i<${#status_array[@]}; i++)); do
    newIndex=$i;
    if [ "${status_array[i]}" == "$name" ]; then
	newIndex=$((newIndex-2))
	break;
    fi
done
j=0;

if [ $newIndex == -2 ]; then
	j=2;
	newIndex=$((newIndex+2));
elif [ $newIndex == -1 ]; then
	j=1;
	newIndex=$((newIndex+1))
fi
k=1;
z=0;
for ((i=$newIndex; i<${#status_array[@]}; i++, j++)); do
	if [ $j == 2 ]; then
		echo "<li class='songList' id='currentlyPlaying'>"
		((z++));
	else
		echo "<li class='songList'>"
		if [ $z == 1 ]; then
			echo -n $k;
			echo -n " ";
			((k++));
		fi
	fi
	echo ${status_array[i]}
	echo "</li>"
done
echo "</ul>"
echo "</body>"
echo "</html>"
exit 0
