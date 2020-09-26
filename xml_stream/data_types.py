"""Module containing the data types needed for the module to work"""
import copy
from typing import Iterable
from xml.etree.ElementTree import Element

from ._utils import get_unique_and_repeated_sub_elements, get_xml_element_attributes_as_dict


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
                    for repeated_element in repeated_elements:
                        # in order not to lose the text
                        if repeated_element.text:
                            repeated_element.set('_value', repeated_element.text)

                        for _, unique_element in unique_elements_map.items():
                            repeated_element.append(copy.deepcopy(unique_element))

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

            # if item has attributes but n sub elements
            elif len(item_attributes_dict) > 0:
                if item.text:
                    item_attributes_dict['_value'] = item.text

                value = item_attributes_dict

            # if item has no attributes and no sub elements
            else:
                value = item.text

            self.update({item.tag: value})

