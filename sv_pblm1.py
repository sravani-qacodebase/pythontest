def xmlfilechnages(x,y):

    import xml.etree.ElementTree as ET
    import datetime
    today = datetime.date.today()
    newdepartdate = (today + datetime.timedelta(days=x)).strftime('%Y%m%d')
    newreturndate = (today + datetime.timedelta(days=y)).strftime('%Y%m%d')
    #print(newdepartdate)
    #print(newreturndate)

    # parsing d#rectly.
    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()
    #print(root)
    # print(root[0][2].tag)
    # print(root[0][2].attrib)
    # for x in root[0][2]:
    #     print(x.tag,x.attrib)
    #     print(x.text)

    # for x in root[0]:
    #     print(x.tag,x.attrib)
    #     print(x.text)

    for i in root[0].findall('TP'):
        depart = i.find('DEPART').text
        #print(depart)
        i.find('DEPART').text = str(newdepartdate)
        i.find('RETURN').text = str(newreturndate)
    tree.write('output.xml')
    #print(x,y)
xmlfilechnages(1,2)







