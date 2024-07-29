import xml.etree.ElementTree as E

def xmlStringToJson(xmlString:str)->dict:
    root = E.fromstring(xmlString)

    # root = tree.getroot()
    d={}
    for child in root:
        if child.tag not in d:
            d[child.tag]=[]
        dic={}
        for child2 in child:
            if child2.tag not in dic:
                dic[child2.tag]=child2.text
        d[child.tag].append(dic)
    return(d)