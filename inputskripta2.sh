#! /bin/bash
mkdir nameinput
touch "nameinput/nameprog2.txt"

read -p "Enter your name: " NAME
read -p "Enter your last name: " LASTNAME


echo "$NAME$LASTNAME" > nameinput/nameprog2.txt


cp nameinput/nameprog.txt /home/slytren/Desktop/
echo "Created nameinput/nameprog2.txt"

python3 -u textread2.py