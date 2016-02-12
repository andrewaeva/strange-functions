# -*-coding:utf-8-*-
import json

import pandas as pd
import r2pipe as r2

dataframe = pd.DataFrame(columns=['name_function', 'opcodes'])
r2p = r2.open('example')
r2p.cmd('aaa')
afl = json.loads(r2p.cmd('aflj'))
functionNamesArray = []
opcodesArray = []

for i in xrange(len(afl)):
    functionNamesArray.append(str(afl[i]['name']))
    opcodes = ""
    for offset in json.loads(r2p.cmd('pdj @' + str(afl[i]['name']))):
        try:
            opcodes += ':' + offset['opcode']
        except KeyError:
            pass
    opcodesArray.append(opcodes)

dataframe = pd.DataFrame({'name_function': functionNamesArray,
                          'opcodes': opcodesArray})
dataframe.to_csv('dataset.csv')
