#!/bin/bash

test_scripts=`ls *.py`

for script in $test_scripts
do
   python3 $script -v
done
