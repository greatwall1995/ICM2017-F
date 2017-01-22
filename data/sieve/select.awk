#!/bin/awk -f
BEGIN {}
FNR > 1{print int($8), (int($13) == 1) || (int($14) == 1) || (int($16) == 1) || (int($19) == 1), ((int($13) == 2) && (int($14) == 2) && (int($16) == 2) && (int($19) == 2)), int($64), int($65), int($67) == 1, int($67) == 2, int($82), int($83), int($103)}
END{}
