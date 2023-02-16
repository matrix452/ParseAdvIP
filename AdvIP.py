#Requires xml.etree library 

import xml.etree.ElementTree as ET
file = input('Full Path to file: ')
tree = ET.parse(file)
root = tree.getroot()
usedIPs=[]
availableIPs=[]
for item in root:
    if (item.attrib['mac']=='00:00:00:00:00:00'):
        availableIPs.append(item.attrib['ip'])
    else:
        usedIPs.append(item.attrib['ip'])
