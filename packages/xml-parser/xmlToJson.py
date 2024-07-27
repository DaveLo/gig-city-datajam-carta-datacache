import xml.etree.ElementTree as E
tree = E.parse('routeXml.xml')
root = tree.getroot()
d={}
for child in root:
    if child.tag not in d:
        d[child.tag]=[]
    dic={}
    for child2 in child:
        if child2.tag not in dic:
            dic[child2.tag]=child2.text
    d[child.tag].append(dic)
print(d)