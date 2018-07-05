# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np

df = pd.read_csv('flouricao.csv')
data = df.values

usrdict = {}
for x in data:
    if not usrdict.get(x[2]):
        usrdict[x[2]] = []
    usrdict[x[2]].append((x[1],x[3],x[4]))

with open('out.tsv', 'w') as f:
    for x in usrdict.keys():
        f.write("\"")
        f.write(x.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding, errors='replace'))
        f.write('"\t')
        #f.write((str(usrdict[x][0][0])).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding, errors='replace'))
        f.write(str(len(usrdict[x])))
        f.write('\t')
        likes = [int(y[2]) for y in usrdict[x] if str(y[2]).isdigit()]
        likes0 = likes.count(0)/float(len(likes))
        f.write(str(likes0))
        f.write('\t')
        likes1 = likes.count(1)/float(len(likes))
        f.write(str(likes1))
        f.write('\t')
        likes2 = likes.count(2)/float(len(likes))
        f.write(str(likes2))
        f.write('\t')
        likes3 = likes.count(3)/float(len(likes))
        f.write(str(likes3))
        f.write('\t')
        likes4 = likes.count(4)/float(len(likes))
        f.write(str(likes4))
        f.write('\t')
        likes5 = likes.count(5)/float(len(likes))
        f.write(str(likes5))
        f.write('\t')
        likes6 = likes.count(6)/float(len(likes))
        f.write(str(likes6))
        f.write('\t')
        likes7 = likes.count(7)/float(len(likes))
        f.write(str(likes7))
        f.write('\n')