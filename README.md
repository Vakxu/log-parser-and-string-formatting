# log-parser-and-string-formatting
Short script to parse a log file and print the results in a nice way

reads logs line by line that are formatted in this way:
'''Mar 02 2015 08:54:14 asa : %ASA-6-302015: Built outbound UDP connection 1956246 for outside:8.8.8.8/53 (8.8.8.8/53) to wifi:10.20.0.100/43965 (52.1.119.182/43965)
Mar 02 2015 08:54:47 asa : %ASA-6-302015: Built outbound UDP connection 1956248 for outside:8.8.8.8/53 (8.8.8.8/53) to wifi:10.20.0.100/35309 (52.1.119.182/35309)
Mar 02 2015 08:54:47 asa : %ASA-6-302015: Built outbound UDP connection 1956249 for outside:8.8.8.8/161 (8.8.8.8/161) to wifi:10.20.0.100/35310 (52.1.119.182/35309)
Mar 02 2015 08:54:47 asa : %ASA-6-302013: Built outbound TCP connection 1956250 for outside:212.10.212.59/443 (212.10.212.59/443) to wifi:10.20.0.100/43500 (52.1.119.182/43500)
Mar 02 2015 08:55:23 asa : %ASA-6-302013: Built inbound TCP connection 1956358 for outside:10.10.62.62/56360 (10.10.62.62/56360) to identity:52.1.119.182/22 (52.1.119.182/22)
Mar 02 2015 08:57:28 asa : %ASA-6-302013: Built outbound TCP connection 1956389 for outside:10.79.62.93/80 (10.79.62.93/80) to wifi:10.20.0.249/64162 (52.1.119.182/64162)'''

And prints them in this format:
10.20.0.100 - 8.8.8.8             53   UDP hitcount = 2                
10.20.0.100 - 8.8.8.8             161  UDP hitcount = 1                
10.10.62.62 - 52.1.119.182        22   TCP hitcount = 1                
10.20.0.100 - 212.10.212.59       443  TCP hitcount = 1                
10.20.0.249 - 10.79.62.93         80   TCP hitcount = 1 
