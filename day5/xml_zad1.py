# xml
# xml używa tagów
# <?xml version="1.0" encoding="UTF-8"?>
# <note>
#   <to>Tove</to>
#   <from>Jani</from>
#   <heading>Reminder</heading>
#   <body>Don't forget me this weekend!</body>
# </note>

from xml.dom import minidom

root = minidom.Document()  # # <?xml version="1.0" ?>
xml = root.createElement('root')  # <root>
root.appendChild(xml)  # </root>

productChild = root.createElement('product')  # <product
productChild.setAttribute("name", "RAJ")  # name="RAJ"/>
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent='\t')
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="RAJ"/>
# </root>
