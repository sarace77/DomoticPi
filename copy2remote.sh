#!/bin/bash

SCP=`which scp`

remoteBase='pi@'$1:

prjDir=${remoteBase}./workspace/webiopi
pyDir=${prjDir}/python
webDir=${prjDir}/html
cssDir=${webDir}/css
jsDir=${webDir}/scripts

$SCP *.html $webDir
$SCP css/* $cssDir
$SCP scripts/* $jsDir
$SCP python/* $pyDir 
