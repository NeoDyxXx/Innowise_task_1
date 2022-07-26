import xml.etree.ElementTree as ET

class XMLSaver:
    def __call__(self, result_list: list, path_of_file: str):
        xml_data = ET.Element('data')

        for item in result_list:
            xml_item = ET.SubElement(xml_data, 'item')
            
            for i in range(item.__len__()):
                xml_item.set('property' + str(i), str(item[i]))

        str_data = ET.tostring(xml_data)
        print(type(str_data))
        with open(path_of_file + '.xml', 'w') as file:
            file.write(str(str_data)[2:-1])