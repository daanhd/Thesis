#!/usr/bin/env bash

# voor elke 'plain' tekst, doe:
for i in *ne.txt; do

  # zet text in variabele
  TEXT=$(cat $i)
  
  # curl naar spotlight met variabele
  curl -H "Accept:text/xml" http://spotlight.sztaki.hu:2232/rest/annotate --data-urlencode "text=$TEXT" --data "confidence=0.45" > ../../xml/$i.xml

done