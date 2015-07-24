#!usr/bin/python
__author__ = 'xiaoyazi'
"""Happy coding"""

import pcapy

devs = pcapy.findalldevs()
print devs

cap = pcapy.open_live('en1', 65536, 1, 0)
count = 1
while count:
    (header, payload) = cap.next()
    print count
    count += 1