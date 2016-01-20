#!/usr/bin/env bash
# script on dbpedia spotlight .xml.ne files
set -eu # stop on error
#  loop on all .xml.ne files
for i in *.xml.ne; do
#  extract second column
  cut -f2 $i > $i.new
#  escape every double quote
  perl -pe 's/"/\\"/g;' $i.new > $i.new2
#  replace white lines with char ^  
  awk '!NF{$0="^"}1' $i.new2 > $i.new3
#  replace newline with space
  awk '$1=$1' ORS=' ' $i.new3 > $i.txt
#  remove tmp files
  rm $i.new
  rm $i.new2
  rm $i.new3

#  add commands EOF
  #echo "\" --data \"confidence=0.5\" --data \"support=20\" > "$i.xml >> $i.txt 
#  add commands BOF

#  move to txt folder
mv $i.txt ../plain_txt/$i.txt
   
done
