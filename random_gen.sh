touch set1
touch set2 
touch set3
for f in `ls set*`
do
  for j in `seq 1 1000`
  do
    echo $RANDOM >> $f
  done
done
