# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:12:30 2019

@author: SHEFALI MANGAL
"""

import json

data = {}
data['person'] = []
data['person'].append({
    'name': 'Shefali',
    'hobbies':'reading',
    'roll no': '45'
})
data['person'].append({
    'name': 'Palak',
    'hobbies': 'Dancing',
    'roll no': '10'
})
data['person'].append({
    'name': 'Babita',
    'hobbies': 'singing',
    'roll no': '12'
})
with open('file.txt', 'w') as outfile:
    json.dump(data, outfile)