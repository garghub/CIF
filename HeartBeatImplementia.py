# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:02:31 2019

@author: G2
"""

from HeartBeatBug import HeartBeatBug

objHeartBeat = HeartBeatBug()
resp = 'duck'
leng = 4
print('If operation is alive, respond:', resp, 'in', leng, 'characters')
print(objHeartBeat.Respond(resp, leng),'\n')

resp = 'hat'
leng = 3
print('If operation is alive, respond:', resp, 'in', leng, 'characters')
print(objHeartBeat.Respond(resp, leng),'\n')

resp = 'duck'
leng = 2048
print('If operation is alive, respond:', resp, 'in', leng, 'characters')
print(objHeartBeat.Respond(resp, leng),'\n')

print('If operation is alive, respond:', resp, 'in', leng, 'characters')
print(objHeartBeat.ChecknRespond(resp, leng),'\n')