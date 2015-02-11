#!/bin/bash
touch csv1
touch csv2
touch csv3
for i in `ls csv*`
do
  for j in `seq 1 10` 
  do
    export LINE=$RANDOM
    for k in `seq 1 4`
    do
      export LINE=$RANDOM,$LINE
     done
     echo $LINE >> $i
   done
done
