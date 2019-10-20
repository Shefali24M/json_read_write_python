# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:13:40 2019

@author: SHEFALI MANGAL
"""

import json

with open('file.txt') as json_file:
    data = json.load(json_file)
    for p in data['person']:
        print('Name: ' + p['name'])
        print('Hobbies: ' + p['hobbies'])
        print('Roll no: ' + p['roll no'])
       


        
