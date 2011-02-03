# coding=utf-8
import sys
from asker import *

questions = 10

print "Paljonko on 5 + 7"
ans = sys.stdin.readline()
if (int(ans) == addInt(5, 7)):
    print "oikein!"
else:
    print "Väärin!"

