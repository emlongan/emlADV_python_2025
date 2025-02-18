"""
    Homework 5.4: sort_dod.py
    Author: Em Longan
    Last modified: 02/18/2025
"""
import json

def by_mean_temp(arg):
    return int(dod[arg]['mean_temp'])

fh = open('weny_dod_tiny.json')
dod = json.load(fh)

keys = sorted(dod, key=by_mean_temp)

for key in keys:
    print(f'{key}:  {dod[key]}')