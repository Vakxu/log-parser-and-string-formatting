# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:52:28 2015

@author: vaxaren
"""

log = '''Mar 02 2015 08:54:14 asa : %ASA-6-302015: Built outbound UDP connection 1956246 for outside:8.8.8.8/53 (8.8.8.8/53) to wifi:10.20.0.100/43965 (52.1.119.182/43965)
Mar 02 2015 08:54:47 asa : %ASA-6-302015: Built outbound UDP connection 1956248 for outside:8.8.8.8/53 (8.8.8.8/53) to wifi:10.20.0.100/35309 (52.1.119.182/35309)
Mar 02 2015 08:54:47 asa : %ASA-6-302015: Built outbound UDP connection 1956249 for outside:8.8.8.8/161 (8.8.8.8/161) to wifi:10.20.0.100/35310 (52.1.119.182/35309)
Mar 02 2015 08:54:47 asa : %ASA-6-302013: Built outbound TCP connection 1956250 for outside:212.10.212.59/443 (212.10.212.59/443) to wifi:10.20.0.100/43500 (52.1.119.182/43500)
Mar 02 2015 08:55:23 asa : %ASA-6-302013: Built inbound TCP connection 1956358 for outside:10.10.62.62/56360 (10.10.62.62/56360) to identity:52.1.119.182/22 (52.1.119.182/22)
Mar 02 2015 08:57:28 asa : %ASA-6-302013: Built outbound TCP connection 1956389 for outside:10.79.62.93/80 (10.79.62.93/80) to wifi:10.20.0.249/64162 (52.1.119.182/64162)'''

def process_line(l):
    data = {}
    words = l.split()
    direction = words[8]
    if direction == 'outbound':
        outip = words[14]
        inip = words[16].lstrip('wifi:')
    elif direction == 'inbound':
        outip = words[17]
        inip = words[14].strip('()')
    outip, inip = outip.strip('()').split('/'), inip.split('/')
    data['outip'] =  outip[0]
    data['outport'] = outip[1]
    data['inip'] = inip[0]
    data['inport'] = inip[1]
    data['protocol'] = words[9]
    return data
    
def process_data(d, stats):
    connection, outport, proto = d['inip'] + ' - ' + d['outip'], d['outport'], d['protocol']
    stats[connection] = stats.get(connection, {})
    connports = stats[connection]
    connports[outport] = connports.get(outport, {})
    connportproto = connports[outport]
    connportproto[proto] = connportproto.get(proto, 0) + 1
    
traffic = {}


for line in log.splitlines():
    if len(line) < 1: continue
    line = line.strip()
    process_data(process_line(line), traffic)

lista = []

for i, j in traffic.items():
    for k, l in j.items():
        for m, n in l.items():
            outp = i
            while len(outp) < 30: outp = outp + ' '
            outp = outp + k
            while len(outp) < 35: outp = outp + ' '
            outp = outp + m
            while len(outp) < 40: outp = outp + ' '
            outp = outp + 'hitcount = ' + str(n)
            lista.append((i, k, m, n))

lista.sort(key=lambda tup: tup[1])
lista.sort(key=lambda tup: tup[3], reverse=True)

printlist = []
for indx, i in enumerate(lista):
    printlist.append([' '] * 60)
    for ind, char in enumerate(i[0]): printlist[indx][ind] = char
    for ind, char in enumerate(i[1]): printlist[indx][ind+34] = char
    for ind, char in enumerate(i[2]): printlist[indx][ind+39] = char
    for ind, char in enumerate(`i[3]`): printlist[indx][ind+43] = 'hitcount = ' + char

for item in printlist:
    print ''.join(item)
