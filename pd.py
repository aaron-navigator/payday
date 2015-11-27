#!/usr/bin/python
import time

today = time.strftime("%d")

NotPayday = 'Depressed '
Drunk = 'cult classic'
if today == 30 or today == 15:
        print 'Payday in full effect. You better be ' + Drunk
else:
        print NotPayday + Drunk
