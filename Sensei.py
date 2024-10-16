#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
from datetime import datetime
import time
import warnings
import json
import os

KANJI_SRC = 'KanjiCSV.csv'
JSON_DB = 'renshuu.json'
GOTIT_CODES = ['4','44','f']
REPORT_DEFAULT = False

warnings.simplefilter(action='ignore', category=FutureWarning)

if not os.path.isfile(KANJI_SRC):
    print(f'ERROR: File \'{KANJI_SRC}\' is missing. Please put this file in the same folder as Sensei.py')
    exit()

if not os.path.isfile(JSON_DB):
    dbStart = {"entries" : []}
    dbStart = json.dumps(dbStart)
    with open(JSON_DB,'w') as file:
        file.writelines(dbStart)

df = pd.read_csv(KANJI_SRC)


df.index = np.arange(1,len(df)+1)


start = int(input('Kanji start: '))
end = int(input('Kanji end: '))
dfs = df.loc[start:end,:]

dfs = dfs.sample(frac=1)


wrong = pd.DataFrame(columns=dfs.columns)

current = 1
print('\n')
while(len(dfs)!=0):
    for (row,rowSeries) in dfs.iterrows():
        if current > end-start+1:
            input(f'{rowSeries[0]}')
        else:
            input(f'{rowSeries[0]} \t\t({current}/{end-start+1})')
        print(f'{rowSeries[1]}')
        gotit = input('Correct?: ')
        print('\n')
        if gotit in GOTIT_CODES:            
            dfs.drop(row,inplace=True)
        else:
            if row not in wrong.index:
                wrong.loc[row,:] = rowSeries
        current += 1
        




wrong.sort_index(inplace=True)


kwrong = []
wrongList = []
for (row,rowSeries) in wrong.iterrows():
    kwrong.append(f'{row}\t{rowSeries[0]} :\t{rowSeries[1]}\n')
    wrongList.append(row)


ct = datetime.now()
time_stamp = f'{ct.year}-{ct.month}-{ct.day}--{ct.hour}_{ct.minute}_{ct.second}'


L1 = [
    f'Date and time: {str(ct)}\n',
    f'Kanji start: {start}\n',
    f'Kanji end: {end}\n\n',
    f'Number of Kanji: {end-start+1}\n',
    f'Correct: {(end-start+1) - len(wrong)}\n',
    f'Wrong: {len(wrong)}\n',
    f'---------------------\n'
    f'Kanji you got wrong:\n\n'
]

L2 = [
    '\n\n',
    '~~~THE END~~~\n\n',
    'Thank you for using Sensei CLI\n',
    'Based on "The Kodansha Kanji Learner\'s Course" by Andrew Scott Conning, 2013\n\n',
    'Created by Sheikh Bilal Ahmad\n',
    'Date: 16-10-2024'
]


createRep = input('\n\nCreate report? (y/n): ')

if createRep == 'y' or createRep == 'Y' or REPORT_DEFAULT:
    with open(f'Kanji-Report-{time_stamp}.txt','w',encoding='utf-8') as file:
        file.writelines(L1)
        file.writelines(kwrong)
        file.writelines(L2)

for l in L1:
    print(l)

for k in kwrong:
    print(k)

for l in L2:
    print(l)

with open(JSON_DB,'r') as tfile:
    t = json.load(tfile)

new_entry = {
    'time': str(datetime.now()),
    'Kanji_start': start,
    'Kanji_end': end,
    'Number_of_Kanji': end-start+1,
    'Correct': (end-start+1) - len(wrong),
    'Wrong': len(wrong),
    'Wrong_list': wrongList
}

t['entries'].append(new_entry)
beut = json.dumps(t,indent=4)

with open(JSON_DB,'w') as fi:
    fi.write(beut)


print('\n\n~~~THE END~~~')