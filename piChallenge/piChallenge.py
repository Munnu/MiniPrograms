#-------------------------------------------------------------------------------
# Name:        piChallenge
# Purpose:      I found this question on SO and I decided to give it a try.
#               pi takes long to calculate, I would assume it works because it
#               can find pi to the fourth decimal place. Of course, series solns
#               take longer to calculate based on proximity.
#
#               The question: Given that Pi can be estimated using the function
#               4 * (1 - 1/3 + 1/5 - 1/7 + ...) with more terms giving greater
#               accuracy, write a function that calculates Pi to an accuracy of
#               5 decimal places.
#
# Author:      Munnu
#
# Created:     01/09/2013
# Copyright:   (c) Munnu 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
count = 0
addedValues = 0
result = 0
i = 1
while result != 3.14159:
    if i % 2 == 1:
        if count % 2 != 0:
            addedValues = addedValues + (float(-1)/i)
        else:
            addedValues = addedValues + (float(1)/i)
        count += 1
    i += 1
    result = round((4 * addedValues), 5)
    print "This is result", result
print "This is result", result, addedValues, "This is addedValues"