"""Module containing the data types needed for the module to work"""
from typing import Iterable
from xml.etree.ElementTree import Element

from ._utils import get_unique_and_repeated_sub_elements, \
    get_xml_element_attributes_as_dict, add_common_sub_elements


class XmlListElement(list):
    """An XML List element"""

    def __init__(self, items: Iterable):
        super().__init__()

        for item in items:
            # items without SubElements return False as __nonzero__method is not defined on Element
            if item:
                unique_elements_map, repeated_elements = get_unique_and_repeated_sub_elements(item)

                if len(repeated_elements) == 0:
                    # append a dict
                    self.append(XmlDictElement(item))
                else:
                    # append a list
                    repeated_elements = add_common_sub_elements(
                        elements=repeated_elements, common_sub_elements=unique_elements_map.values())
                    self.append(XmlListElement(repeated_elements))

            elif item.text:
                # append a text/number
                text = item.text.strip()
                if text:
                    self.append(text)


class XmlDictElement(dict):
    """An XML dict element"""

    def __init__(self, xml_element: Element):
        super().__init__()
        self.update(get_xml_element_attributes_as_dict(xml_element))

        unique_root_elements_map, repeated_root_elements = get_unique_and_repeated_sub_elements(xml_element)

        if len(repeated_root_elements) > 0:
            repeated_root_elements = add_common_sub_elements(
                elements=repeated_root_elements, common_sub_elements=unique_root_elements_map.values())
            unique_tags = set([element.tag for element in repeated_root_elements])

            self.update(
                {tag: XmlListElement(filter(lambda x: x.tag == tag, repeated_root_elements))
                 for tag in unique_tags})
        else:
            for item in xml_element:
                item_attributes_dict = get_xml_element_attributes_as_dict(item)

                # if the item has sub elements
                if item:
                    unique_elements_map, repeated_elements = get_unique_and_repeated_sub_elements(item)

                    if len(repeated_elements) == 0:
                        value = XmlDictElement(item)
                    else:
                        unique_tags = set([sub_element.tag for sub_element in repeated_elements])
                        value = {
                            tag: XmlListElement(filter((lambda x: x.tag == tag), repeated_elements))
                            for tag in unique_tags
                        }

                    value.update(item_attributes_dict)

                    # if item has attributes but no sub elements
                elif len(item_attributes_dict) > 0:
                    if item.text:
                        item_attributes_dict['_value'] = item.text

                    value = item_attributes_dict

                # if item has no attributes and no sub elements
                else:
                    value = item.text

                self.update({item.tag: value})
