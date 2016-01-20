#!/usr/bin/env bash

for j in *ne; do

  # replace three symbols on each line with ^
  sed 's/\^.*/\^/g' $j > $j.ne2
  
  # get rid of those 2x double quotes
  sed 's/\"\"\"\"/\"/g' $j.ne2 > $j.ne3
    
  # delete ^, desired whiteline is created!
  sed 's/\^//' $j.ne3 > whitelined/$j.ne2
  
  # remove empty lines
  sed '/^\s*$/d' whitelined/$j.ne2 > whitelined/$j.ne3
  
  # prepend line counter to file, ignore whitelines
  awk -F'\t' -v OFS='\t' 'NR == 1 {print (NR), $0;  next} {print (NR), $0}' whitelined/$j.ne3 > whitelined/$j.ne

  # remove so called ctrl+m char for carriage returns
  tr -d '\015' < whitelined/$j.ne > whitelined/$j
  
  # replace space 
  #sed 's/ \+ /\t/g' whitelined/$j.x > whitelined/$j
  
  
  # remove some added file extensions along the way
  mv "whitelined/$j" "whitelined/${j//.txt.xml.ne/}"
  
  
  # remove unwanted files
  # rm $j
  rm $j.ne2
  rm $j.ne3
  rm whitelined/$j.ne3
  rm whitelined/$j.ne2
  rm whitelined/$j.ne
  #rm whitelined/$j.x
    
done