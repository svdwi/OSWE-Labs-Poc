#!/bin/bash
# Generate String Script 

 
if [[ $# -eq 0 ]] ; then
echo "Usage: $0 Filename Lines "
exit 0
else
crunch 8 8  abcdefghijklmnopqrstuvwxyz0123456789  -c $2 > $1
echo "---------------------------------------------------------"
echo "Output Filename saved in : `pwd`/$1"
echo "---------------------------------------------------------"

fi
 
