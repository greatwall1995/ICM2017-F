#!/bin/awk -f
BEGIN {}
int($9) == 1 {print $1, $2, $3, $5,  $6,  $7,  $10}
END{}
