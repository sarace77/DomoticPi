#!/bin/bash

SCP=`which scp`

remoteBase='pi@'$1:

localPyDir=python
localWebDir=html
localCssDir=${localWebDir}/css
localjsDir=${localWebDir}/scripts

prjDir=${remoteBase}./DomoticPi
pyDir=${prjDir}/${localPyDir}
webDir=${prjDir}/${localWebDir}
cssDir=${prjDir}/${localCssDir}
jsDir=${prjDir}/${localjsDir}

$SCP config $prjDir
$SCP ${localWebDir}/*.html $webDir
$SCP ${localCssDir}/*.css $cssDir
$SCP ${localjsDir}/*.js $jsDir
$SCP ${localPyDir}/*.py $pyDir 
