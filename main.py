import xml.etree.ElementTree as ET
import json

xml_file = "test_data.xml"
json_file = "test.json"


def xml_converter(file):

    result = []
    tree = ET.parse(file)
    root = tree.getroot()

    for element in root:
        element_dict = {}
        for subelement in element:
            element_dict[subelement.tag] = subelement.text

            replacement(subelement)

        result.append(element_dict)

    return result


def replacement(subelement):
    if subelement.text == "YOUR_FIRST_NAME":
        subelement.text = "Olya"
    elif subelement.text == "YOUR_LAST_NAME":
        subelement.text = "Kovalenko"
    elif subelement.text == "YOUR_YYYY":
        subelement.text = "1987"
    elif subelement.text == "YOUR_Month":
        subelement.text = "May"
    elif subelement.text == "YOUR_DD":
        subelement.text = "02"
    elif subelement.text == "YOUR_COMPANY":
        subelement.text = "Lohika"
    elif subelement.text == "YOUR_PROJECT":
        subelement.text = "Funny project"
    elif subelement.text == "YOUR_ROLE":
        subelement.text = "Easter bunny"
    elif subelement.text == "YOUR_ROOM":
        subelement.text = "Kitchen"
    elif subelement.text == "YOUR_HOBBY":
        subelement.text = "Travelling"


def create_json(element_dict):
    with open(json_file, 'w') as file:
        file.write(json.dumps(element_dict, indent=4, sort_keys=True))


def main():
    print(xml_converter(xml_file))

    action = xml_converter(xml_file)

    print(json.dumps(action, indent=4, sort_keys=True))

    create_json(action)


if __name__ == '__main__':
    main()




