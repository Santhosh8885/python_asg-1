from urllib.request import urlopen
from xml.etree.ElementTree import parse
url = urlopen('https://www.w3schools.com/xml/simple.xml')
xml_doc = parse(url)
root = xml_doc.getroot()
# print(root[0][0].text)
for child in root:
    for i in child:
        if(i.tag == 'name' or i.tag == 'price'):
            print(i.tag,i.text)