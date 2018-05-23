#!/bin/bash
totTime=$(./.mpcGetTotal)
elapsTime=$(./.mpcGetElapsed)
echo "content-type: text/html"
echo ""
echo $elapsTime
echo "<br>"
echo $totTime
exit 0
