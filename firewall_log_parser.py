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
traffic = {}
lista, printlist = [], []

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
    
def make_list_from_dict(d, li):
    for i, j in d.items():
        for k, l in j.items():
            for m, n in l.items(): 
                li.append((i, k, m, n))
    li.sort(key=lambda tup: tup[1])
    li.sort(key=lambda tup: tup[3], reverse=True)

def make_formatted_printlist(li, prntli):
    for i, l in enumerate(li):
        prntli.append([' '] * 60)
        for ind, char in enumerate(l[0]): prntli[i][ind] = char
        for ind, char in enumerate(l[1]): prntli[i][ind+34] = char
        for ind, char in enumerate(l[2]): prntli[i][ind+39] = char
        for ind, char in enumerate(`l[3]`): prntli[i][ind+43] = 'hitcount = ' + char
        
def print_connections_list(li):
    for l in li: print ''.join(l)


# Go trough the logs line by line        
for line in log.splitlines():
    if len(line) < 1: continue
    line = line.strip()
    process_data(process_line(line), traffic)

make_list_from_dict(traffic, lista)
make_formatted_printlist(lista, printlist)
print_connections_list(printlist)